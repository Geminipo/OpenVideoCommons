from __future__ import annotations

import argparse
import json
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

SCHEMA_VERSION = "0.1.0"


class ValidationError(ValueError):
    """Raised when a benchmark result does not satisfy the minimum schema."""


def detect_hardware() -> dict[str, Any]:
    return {
        "platform": platform.platform(),
        "machine": platform.machine(),
        "processor": platform.processor() or None,
        "cpu": platform.processor() or platform.machine(),
        "gpu": None,
        "vram_gb": None,
        "ram_gb": None,
    }


def detect_software() -> dict[str, Any]:
    return {
        "python": platform.python_version(),
        "os": platform.system(),
        "os_release": platform.release(),
        "cuda": None,
        "torch": None,
    }


def create_result(args: argparse.Namespace) -> dict[str, Any]:
    status = "success" if args.success else "failed"
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
        "hardware": detect_hardware(),
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
    create.add_argument("--output", required=True, type=Path, help="Path to write the result JSON.")

    validate = subparsers.add_parser("validate", help="Validate a benchmark result JSON file.")
    validate.add_argument("path", type=Path, help="Path to result JSON.")

    return parser


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

    parser.error("Unknown command")
    return 2
