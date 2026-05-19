# Validate the sample benchmark flow on your machine

Labels: `good first issue`, `benchmark`, `cli`

## Goal

Help us confirm that the bootstrap CLI works across different machines.

## Steps

```bash
git clone https://github.com/Geminipo/OpenVideoCommons.git
cd OpenVideoCommons
python -m unittest discover -s tests
python -m ovc detect-hardware
python -m ovc validate results/benchmark/wan2.1/example-contributor-local.json
python -m ovc create-smoke-result \
  --github YOUR_GITHUB_USERNAME \
  --output results/benchmark/smoke-test/YOUR_GITHUB_USERNAME.json
python -m ovc generate-report \
  --results-dir results/benchmark \
  --title "Community Benchmark Report 001" \
  --output /tmp/ovc-report.md
```

## Please Report

- Operating system.
- Python version.
- CPU/GPU summary.
- Whether `create-smoke-result` produced a valid JSON file.
- Any command that failed.
- Any setup friction.

## Acceptance Criteria

- The contributor posts the command output summary.
- Any reproducible failure gets a follow-up bug issue.
