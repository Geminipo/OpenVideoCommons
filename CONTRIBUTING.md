# Contributing to OpenVideoCommons

OpenVideoCommons is designed around small, verifiable contributions. You do not need to train a model to help.

## First Contribution Loop

The first loop is intentionally simple:

1. Pick a benchmark task or prompt set.
2. Run the local CLI.
3. Validate the generated result file.
4. Submit the result as a pull request.
5. Get reviewed, accepted, and included in a public report.

## Local Setup

Use Python 3.10 or newer.

```bash
python -m unittest discover -s tests
python -m ovc --help
```

No third-party dependencies are required for the initial CLI scaffold.

## Submitting Benchmark Results

For the first benchmark round, you can submit a lightweight hardware smoke-test result without running a video model:

```bash
python -m ovc create-smoke-result \
  --github YOUR_GITHUB_USERNAME \
  --output results/benchmark/smoke-test/YOUR_GITHUB_USERNAME.json
python -m ovc validate results/benchmark/smoke-test/YOUR_GITHUB_USERNAME.json
```

If automatic hardware detection misses your GPU or memory, add manual overrides:

```bash
python -m ovc create-smoke-result \
  --github YOUR_GITHUB_USERNAME \
  --gpu "RTX 4090" \
  --vram-gb 24 \
  --ram-gb 64 \
  --output results/benchmark/smoke-test/YOUR_GITHUB_USERNAME-rtx4090.json
```

Place benchmark results under:

```text
results/benchmark/<model>/<github-user>-<hardware-slug>.json
```

Example:

```text
results/benchmark/wan2.1/alice-rtx4090.json
```

Before opening a pull request, run:

```bash
python -m ovc validate results/benchmark/wan2.1/alice-rtx4090.json
python -m unittest discover -s tests
```

## Result Quality Expectations

Accepted benchmark records should include:

- Model name and model version when known.
- Prompt set name and prompt set version.
- Hardware summary.
- Operating system and Python version.
- Runtime duration.
- Success or failure status.
- Output hash when a video artifact exists.
- Log hash when logs are available.
- Reproducible command or notes.

## What Not To Submit

Please do not submit:

- Copyright-unclear videos as training data.
- Private, personal, or sensitive videos.
- Result files that cannot be reproduced.
- Claims about hardware performance without logs or configuration details.
- Token, mining, or speculative reward proposals.

## Review Priorities

Maintainers should prioritize:

- Reproducibility.
- Schema validity.
- Clear provenance.
- Safe and legal data handling.
- Small pull requests that are easy to verify.

## Communication Norms

OpenVideoCommons should feel ambitious and careful at the same time. Be direct about technical limits, kind to new contributors, and strict about evidence.
