# Outreach Playbook

The goal is not broad promotion first. The goal is to recruit specific people to perform specific actions.

## First Outreach Goal

Recruit 10 people to run the smoke-test flow:

```bash
git clone https://github.com/Geminipo/OpenVideoCommons.git
cd OpenVideoCommons
python -m unittest discover -s tests
python -m ovc doctor
python -m ovc detect-hardware
python -m ovc validate results/benchmark/wan2.1/example-contributor-local.json
python -m ovc create-smoke-result --github YOUR_GITHUB_USERNAME --output /tmp/ovc-smoke.json
```

## Target Contributor Profiles

- People running Wan2.1, HunyuanVideo, CogVideoX, Open-Sora, or ComfyUI video workflows locally.
- Owners of RTX 3060, RTX 4090, Apple Silicon, AMD/ROCm, and high-VRAM workstation GPUs.
- Hugging Face Spaces builders working on video generation or video understanding demos.
- Researchers or engineers interested in evaluation, reproducibility, and open benchmarks.
- Creators who actively compare local video models.

## Direct Message Template

```text
Hi, I am launching OpenVideoCommons, a community benchmark network for open video AI.

We are starting small: collect reproducible benchmark and smoke-test results for open video models on real consumer hardware.

If you have a GPU or Apple Silicon machine, would you be open to running the first smoke-test flow and sharing feedback?

Repo: https://github.com/Geminipo/OpenVideoCommons
```

## Follow-Up Template

```text
Thanks for taking a look.

The first contribution does not require running a heavy video model yet. The current ask is just to validate the local CLI flow and report your hardware:

python -m unittest discover -s tests
python -m ovc doctor
python -m ovc detect-hardware
python -m ovc validate results/benchmark/wan2.1/example-contributor-local.json
python -m ovc create-smoke-result --github YOUR_GITHUB_USERNAME --output /tmp/ovc-smoke.json

If anything fails, that failure is useful. We want the first benchmark network to reflect real machines, not ideal lab setups.
```

## Public Post Template

```text
OpenVideoCommons Benchmark Round 001 is open.

We are looking for the first 10 people to test the local CLI flow on real machines:

- NVIDIA GPUs
- Apple Silicon
- AMD/ROCm
- CPU-only environments

Goal: 10 benchmark runners, 5 hardware profiles, and Community Benchmark Report 001.

Repo: https://github.com/Geminipo/OpenVideoCommons
```

## Tracking Table

| Person / Project | Platform | Hardware | Ask | Status | Follow-up Date | Notes |
| --- | --- | --- | --- | --- | --- | --- |
|  | GitHub / X / HF / Discord |  | Smoke test / benchmark / review | Not contacted |  |  |

## Outreach Rules

- Ask for one concrete action.
- Do not overclaim training ambitions.
- Treat failures as contributions.
- Thank every respondent.
- Convert repeated confusion into docs or issues.
- Do not spam large communities before the first 5 direct contributors respond.
