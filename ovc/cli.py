from __future__ import annotations

import argparse
import json
import platform
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

SCHEMA_VERSION = "0.1.0"


class ValidationError(ValueError):
    """Raised when a benchmark result does not satisfy the minimum schema."""


def detect_hardware() -> dict[str, Any]:
    hardware = {
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor() or None,
        "cpu": platform.processor() or platform.machine(),
        "gpu": None,
        "vram_gb": None,
        "ram_gb": None,
    }
    hardware.update(_detect_nvidia_gpu())
    if platform.system() == "Darwin" and not hardware.get("gpu"):
        hardware.update(_detect_apple_chip())
    return hardware


def parse_nvidia_smi(output: str) -> dict[str, Any]:
    rows = []
    for line in output.splitlines():
        parts = [part.strip() for part in line.split(",")]
        if len(parts) < 2 or not parts[0]:
            continue
        try:
            vram_gb = round(float(parts[1]) / 1024, 1)
        except ValueError:
            vram_gb = None
        rows.append({"name": parts[0], "vram_gb": vram_gb})

    if not rows:
        return {}

    detected: dict[str, Any] = {
        "gpu": "; ".join(row["name"] for row in rows),
    }
    vram_values = [row["vram_gb"] for row in rows if row["vram_gb"] is not None]
    if vram_values:
        detected["vram_gb"] = max(vram_values)
    return detected


def parse_apple_chip(output: str) -> dict[str, Any]:
    chip = _match_first(output, r"Chip:\s*(.+)")
    memory = _match_first(output, r"Memory:\s*([0-9]+(?:\.[0-9]+)?)\s*GB")
    detected: dict[str, Any] = {}
    if chip:
        detected["gpu"] = f"{chip} integrated GPU"
    if memory:
        detected["ram_gb"] = float(memory)
    return detected


def detect_software() -> dict[str, Any]:
    return {
        "python": platform.python_version(),
        "os": platform.system(),
        "os_release": platform.release(),
        "cuda": None,
        "torch": None,
    }


def _detect_nvidia_gpu() -> dict[str, Any]:
    try:
        result = subprocess.run(
            ["nvidia-smi", "--query-gpu=name,memory.total", "--format=csv,noheader,nounits"],
            check=False,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (OSError, subprocess.TimeoutExpired):
        return {}
    if result.returncode != 0:
        return {}
    return parse_nvidia_smi(result.stdout)


def _detect_apple_chip() -> dict[str, Any]:
    try:
        result = subprocess.run(
            ["system_profiler", "SPHardwareDataType"],
            check=False,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (OSError, subprocess.TimeoutExpired):
        return {}
    if result.returncode != 0:
        return {}
    return parse_apple_chip(result.stdout)


def _match_first(text: str, pattern: str) -> str | None:
    match = re.search(pattern, text)
    if not match:
        return None
    return match.group(1).strip()


def create_result(args: argparse.Namespace) -> dict[str, Any]:
    status = "success" if args.success else "failed"
    hardware = detect_hardware()
    _apply_hardware_overrides(hardware, args)
    return {
        "schema_version": SCHEMA_VERSION,
        "task_id": args.task_id or f"benchmark-{uuid4().hex[:12]}",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "contributor": {
            "github": args.github,
        },
        "model": {
            "name": args.model,
            "version": args.model_version,
            "source": args.model_source,
        },
        "prompt_set": {
            "name": args.prompt_set,
            "version": args.prompt_set_version,
        },
        "hardware": hardware,
        "software": detect_software(),
        "run": {
            "status": status,
            "generation_time_sec": args.generation_time_sec,
            "command": args.command or " ".join(sys.argv),
            "notes": args.notes or "",
        },
        "artifacts": {
            "output_hash": args.output_hash,
            "log_hash": args.log_hash,
            "output_uri": args.output_uri,
        },
        "verification": {
            "status": "self_reported",
            "reviewers": [],
        },
    }


def create_smoke_result(args: argparse.Namespace) -> dict[str, Any]:
    smoke_args = argparse.Namespace(
        github=args.github,
        model="smoke-test",
        model_version="cli-hardware-detection",
        model_source="https://github.com/Geminipo/OpenVideoCommons",
        prompt_set="motion-basic-v1",
        prompt_set_version="1.0.0",
        task_id=args.task_id,
        generation_time_sec=0.0,
        output_hash=None,
        log_hash=None,
        output_uri=None,
        command="python -m ovc detect-hardware",
        notes=args.notes or "Smoke-test record for local hardware detection.",
        success=True,
        gpu=args.gpu,
        vram_gb=args.vram_gb,
        ram_gb=args.ram_gb,
    )
    return create_result(smoke_args)


def _apply_hardware_overrides(hardware: dict[str, Any], args: argparse.Namespace) -> None:
    if getattr(args, "gpu", None):
        hardware["gpu"] = args.gpu
    if getattr(args, "vram_gb", None) is not None:
        hardware["vram_gb"] = args.vram_gb
    if getattr(args, "ram_gb", None) is not None:
        hardware["ram_gb"] = args.ram_gb


def validate_result(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    required_top_level = [
        "schema_version",
        "task_id",
        "contributor",
        "model",
        "prompt_set",
        "hardware",
        "software",
        "run",
        "artifacts",
        "verification",
    ]
    for key in required_top_level:
        if key not in data:
            errors.append(f"Missing required field: {key}")

    if data.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")

    _require_nested(errors, data, ["contributor", "github"])
    _require_nested(errors, data, ["model", "name"])
    _require_nested(errors, data, ["prompt_set", "name"])
    _require_nested(errors, data, ["prompt_set", "version"])
    _require_nested(errors, data, ["hardware", "platform"])
    _require_nested(errors, data, ["software", "python"])
    _require_nested(errors, data, ["run", "status"])
    _require_nested(errors, data, ["run", "command"])
    _require_nested(errors, data, ["verification", "status"])

    status = _get_nested(data, ["run", "status"])
    if status not in {"success", "failed", "partial", None}:
        errors.append("run.status must be one of: success, failed, partial")

    verification = _get_nested(data, ["verification", "status"])
    if verification not in {"self_reported", "reviewed", "accepted", "rejected", None}:
        errors.append("verification.status must be one of: self_reported, reviewed, accepted, rejected")

    generation_time = _get_nested(data, ["run", "generation_time_sec"])
    if generation_time is not None and not isinstance(generation_time, (int, float)):
        errors.append("run.generation_time_sec must be a number or null")

    return errors


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValidationError("Top-level JSON value must be an object")
    return data


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, sort_keys=True)
        handle.write("\n")


def load_benchmark_results(root: Path) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    if not root.exists():
        return results

    for path in sorted(root.rglob("*.json")):
        try:
            data = load_json(path)
        except (OSError, json.JSONDecodeError, ValidationError):
            continue
        if not validate_result(data):
            results.append(data)
    return results


def generate_report(results: list[dict[str, Any]], title: str = "Community Benchmark Report") -> str:
    lines = [
        f"# {title}",
        "",
        "Status: generated",
        "",
        "## Summary",
        "",
        f"- Benchmark records: {len(results)}",
        f"- Models covered: {_count_unique(results, ['model', 'name'])}",
        f"- Hardware profiles: {_count_hardware_profiles(results)}",
        f"- Contributors: {_count_unique(results, ['contributor', 'github'])}",
        "",
        "## Results",
        "",
        "| Model | Hardware | Prompt Set | Status | Runtime | Contributor |",
        "| --- | --- | --- | --- | --- | --- |",
    ]

    if results:
        for result in sorted(results, key=_result_sort_key):
            lines.append(
                "| "
                + " | ".join(
                    [
                        _markdown_cell(_get_nested(result, ["model", "name"]) or "unknown"),
                        _markdown_cell(_hardware_label(result)),
                        _markdown_cell(_get_nested(result, ["prompt_set", "name"]) or "unknown"),
                        _markdown_cell(_get_nested(result, ["run", "status"]) or "unknown"),
                        _markdown_cell(_runtime_label(_get_nested(result, ["run", "generation_time_sec"]))),
                        _markdown_cell(_get_nested(result, ["contributor", "github"]) or "unknown"),
                    ]
                )
                + " |"
            )
    else:
        lines.append("| No valid records found | - | - | - | - | - |")

    lines.extend(
        [
            "",
            "## Notes",
            "",
            "This report is generated from validated benchmark result JSON files.",
        ]
    )
    return "\n".join(lines) + "\n"


def _require_nested(errors: list[str], data: dict[str, Any], path: list[str]) -> None:
    value = _get_nested(data, path)
    if value in (None, ""):
        errors.append(f"Missing required field: {'.'.join(path)}")


def _get_nested(data: dict[str, Any], path: list[str]) -> Any:
    current: Any = data
    for key in path:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def _count_unique(results: list[dict[str, Any]], path: list[str]) -> int:
    return len({value for result in results if (value := _get_nested(result, path))})


def _count_hardware_profiles(results: list[dict[str, Any]]) -> int:
    return len({_hardware_label(result) for result in results if _hardware_label(result) != "unknown"})


def _hardware_label(result: dict[str, Any]) -> str:
    gpu = _get_nested(result, ["hardware", "gpu"])
    if gpu:
        return str(gpu)
    platform_name = _get_nested(result, ["hardware", "platform"])
    return str(platform_name or "unknown")


def _runtime_label(value: Any) -> str:
    if isinstance(value, (int, float)):
        return f"{value:.1f}s"
    return "unknown"


def _markdown_cell(value: Any) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def _result_sort_key(result: dict[str, Any]) -> tuple[str, str, str]:
    return (
        str(_get_nested(result, ["model", "name"]) or ""),
        str(_get_nested(result, ["hardware", "gpu"]) or _get_nested(result, ["hardware", "platform"]) or ""),
        str(_get_nested(result, ["contributor", "github"]) or ""),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ovc",
        description="OpenVideoCommons local contribution tooling.",
    )
    subparsers = parser.add_subparsers(dest="command_name", required=True)

    subparsers.add_parser("detect-hardware", help="Print detected local hardware and software metadata.")

    create = subparsers.add_parser("create-result", help="Create a self-reported benchmark result JSON file.")
    create.add_argument("--github", default="anonymous", help="GitHub username for the contribution record.")
    create.add_argument("--model", required=True, help="Model name, for example wan2.1.")
    create.add_argument("--model-version", default="", help="Model version or checkpoint identifier.")
    create.add_argument("--model-source", default="", help="Model source URL or repository.")
    create.add_argument("--prompt-set", required=True, help="Prompt set name.")
    create.add_argument("--prompt-set-version", default="1.0.0", help="Prompt set version.")
    create.add_argument("--task-id", default="", help="Optional stable task id.")
    create.add_argument("--generation-time-sec", type=float, default=None, help="Generation duration in seconds.")
    create.add_argument("--output-hash", default=None, help="Hash of generated output artifact.")
    create.add_argument("--log-hash", default=None, help="Hash of run log artifact.")
    create.add_argument("--output-uri", default=None, help="URI of generated output artifact.")
    create.add_argument("--command", default="", help="Reproducible command used for the run.")
    create.add_argument("--notes", default="", help="Free-form run notes.")
    create.add_argument("--success", action=argparse.BooleanOptionalAction, default=True, help="Whether the run succeeded.")
    _add_hardware_override_args(create)
    create.add_argument("--output", required=True, type=Path, help="Path to write the result JSON.")

    smoke = subparsers.add_parser("create-smoke-result", help="Create a lightweight hardware smoke-test result JSON file.")
    smoke.add_argument("--github", default="anonymous", help="GitHub username for the contribution record.")
    smoke.add_argument("--task-id", default="", help="Optional stable task id.")
    smoke.add_argument("--notes", default="", help="Free-form run notes.")
    _add_hardware_override_args(smoke)
    smoke.add_argument("--output", required=True, type=Path, help="Path to write the result JSON.")

    validate = subparsers.add_parser("validate", help="Validate a benchmark result JSON file.")
    validate.add_argument("path", type=Path, help="Path to result JSON.")

    report = subparsers.add_parser("generate-report", help="Generate a Markdown benchmark report from result JSON files.")
    report.add_argument("--results-dir", type=Path, default=Path("results/benchmark"), help="Directory containing benchmark result JSON files.")
    report.add_argument("--title", default="Community Benchmark Report", help="Markdown report title.")
    report.add_argument("--output", required=True, type=Path, help="Path to write the Markdown report.")

    return parser


def _add_hardware_override_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--gpu", default=None, help="Override detected GPU label, for example 'RTX 4090'.")
    parser.add_argument("--vram-gb", type=float, default=None, help="Override detected GPU VRAM in GB.")
    parser.add_argument("--ram-gb", type=float, default=None, help="Override detected system RAM in GB.")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command_name == "detect-hardware":
        print(json.dumps({"hardware": detect_hardware(), "software": detect_software()}, indent=2, sort_keys=True))
        return 0

    if args.command_name == "create-result":
        result = create_result(args)
        errors = validate_result(result)
        if errors:
            for error in errors:
                print(f"error: {error}", file=sys.stderr)
            return 1
        write_json(args.output, result)
        print(f"Wrote benchmark result to {args.output}")
        return 0

    if args.command_name == "create-smoke-result":
        result = create_smoke_result(args)
        errors = validate_result(result)
        if errors:
            for error in errors:
                print(f"error: {error}", file=sys.stderr)
            return 1
        write_json(args.output, result)
        print(f"Wrote smoke-test result to {args.output}")
        return 0

    if args.command_name == "validate":
        try:
            data = load_json(args.path)
        except (OSError, json.JSONDecodeError, ValidationError) as error:
            print(f"error: {error}", file=sys.stderr)
            return 1
        errors = validate_result(data)
        if errors:
            for error in errors:
                print(f"error: {error}", file=sys.stderr)
            return 1
        print(f"Valid benchmark result: {args.path}")
        return 0

    if args.command_name == "generate-report":
        results = load_benchmark_results(args.results_dir)
        report = generate_report(results, title=args.title)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(report, encoding="utf-8")
        print(f"Wrote benchmark report with {len(results)} records to {args.output}")
        return 0

    parser.error("Unknown command")
    return 2
