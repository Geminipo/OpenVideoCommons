# Improve hardware metadata detection

Labels: `good first issue`, `cli`, `benchmark`

## Goal

Improve `python -m ovc detect-hardware` so benchmark records capture more useful local hardware metadata.

Status: first implementation shipped for NVIDIA `nvidia-smi` and Apple Silicon `system_profiler` detection. Further improvements are welcome.

## Suggested Starting Points

Pick one environment:

- NVIDIA GPUs through `nvidia-smi`.
- Apple Silicon through `system_profiler`.
- AMD/ROCm through available local tools.

## Constraints

- Do not add required third-party dependencies.
- Detection should fail gracefully.
- Avoid collecting serial numbers, usernames, private paths, or sensitive device identifiers.

## Acceptance Criteria

- Unit tests cover the parser for the selected hardware source.
- Missing tools do not crash the CLI.
- README examples still work.

## Follow-Up Ideas

- Add AMD/ROCm detection.
- Detect CUDA and Torch versions in `detect_software`.
- Add a `--verbose` mode that explains which hardware probes ran.
- Let contributors opt into manually overriding GPU or RAM fields.
