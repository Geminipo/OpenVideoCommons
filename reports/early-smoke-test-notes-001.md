# Early Smoke-Test Notes 001

Status: waiting for more records

## Purpose

This note will summarize early smoke-test feedback for Benchmark Round 001 before the first full community benchmark report.

The goal is to learn whether contributors can:

- Install the project.
- Run `python -m ovc doctor`.
- Generate a smoke-test result.
- Validate the result JSON.
- Share useful hardware metadata.

## Current Snapshot

| Metric | Current | Target |
| --- | ---: | ---: |
| Smoke-test / benchmark records | 2 | 10 |
| Hardware profiles | 2 | 5 |
| External contributors | 0 | 5 |

## Early Observations

- Apple Silicon detection works on the initial local test machine.
- Manual hardware overrides are available for contributors whose hardware is not detected automatically.
- The project still needs NVIDIA, AMD/ROCm, and CPU-only smoke-test records.

## Wanted Hardware Profiles

- NVIDIA RTX 3060 / 4060 / 4090.
- Apple M-series machines.
- AMD/ROCm setups.
- CPU-only Linux.
- Windows with Python 3.10+.

## How To Contribute A Smoke-Test Record

```bash
git clone https://github.com/Geminipo/OpenVideoCommons.git
cd OpenVideoCommons
python -m pip install -e .
python -m ovc doctor
python -m ovc create-smoke-result \
  --github YOUR_GITHUB_USERNAME \
  --output results/benchmark/smoke-test/YOUR_GITHUB_USERNAME.json
python -m ovc validate results/benchmark/smoke-test/YOUR_GITHUB_USERNAME.json
```

## Next Update Trigger

Publish this note when the project reaches either:

- 5 smoke-test records, or
- 3 distinct hardware profiles, or
- the first external pull request with a valid result record.
