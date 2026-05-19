# OpenVideoCommons Launch Note 001

Status: public draft

## Why This Project Exists

Video AI is moving quickly, but much of the real knowledge about open video models is still fragmented:

- Which models actually run on consumer hardware?
- What hardware profiles work in practice?
- Which prompts expose temporal failures?
- Which setup paths are reproducible?
- What fails, and why?

OpenVideoCommons exists to build a transparent, community-powered evaluation layer for open video AI.

We are not starting by claiming that volunteer computers can immediately train a frontier video model. That would be the wrong first promise.

We are starting with something smaller and more useful:

> Measure open video AI on real machines, publish reproducible records, and build trust before training.

Our route is:

```text
First we measure. Then we improve. Then we train.
```

## What We Are Doing First

The first milestone is **Benchmark Round 001**.

The goal is to collect lightweight smoke-test records across real hardware:

- NVIDIA GPUs.
- Apple Silicon.
- AMD/ROCm.
- CPU-only environments.
- Workstations and laptops.

The first target is not model quality. The first target is contributor onboarding and hardware visibility.

We want to answer:

- Can contributors install and run the local tooling?
- Can the CLI detect useful hardware metadata?
- Which environments need manual overrides?
- What setup friction appears on real machines?

## What A First Contribution Looks Like

You do not need to run a heavy video model to make the first useful contribution.

Run:

```bash
python -m ovc doctor
python -m ovc create-smoke-result \
  --github YOUR_GITHUB_USERNAME \
  --output results/benchmark/smoke-test/YOUR_GITHUB_USERNAME.json
python -m ovc validate results/benchmark/smoke-test/YOUR_GITHUB_USERNAME.json
```

If hardware detection misses your GPU or memory, use manual overrides:

```bash
python -m ovc create-smoke-result \
  --github YOUR_GITHUB_USERNAME \
  --gpu "RTX 4090" \
  --vram-gb 24 \
  --ram-gb 64 \
  --output results/benchmark/smoke-test/YOUR_GITHUB_USERNAME-rtx4090.json
```

Then open a pull request or share the result in a GitHub issue.

## Current Project State

As of this launch note:

- CI is passing.
- GitHub Discussions are enabled.
- Launch issues are open.
- The CLI supports hardware detection, smoke-test records, validation, and report generation.
- The first generated community report exists.
- The project has initial records for Apple Silicon and a bootstrap Wan2.1 example.

Current milestone:

```text
10 benchmark runners
5 hardware profiles
Community Benchmark Report 001
```

## What We Are Not Doing Yet

We are deliberately not starting with:

- Large-scale distributed training.
- Token incentives or compute mining.
- Copyright-unclear video datasets.
- Claims about matching closed frontier models.
- A complex central task server.

Those decisions are intentional. The project needs trust before scale.

## Who We Are Looking For

We are looking for:

- People with NVIDIA GPUs.
- People with Apple Silicon.
- People with AMD/ROCm setups.
- CPU-only users willing to test the baseline flow.
- Engineers who care about reproducible evaluation.
- Researchers who care about benchmark design.
- Creators who compare local video models.

The first ask is small: run the smoke-test flow and tell us what worked or failed.

## How To Help

Start here:

- Repository: https://github.com/Geminipo/OpenVideoCommons
- First issue: `Validate the sample benchmark flow on your machine`
- First report: `reports/community-benchmark-report-001.md`
- Early notes: `reports/early-smoke-test-notes-001.md`
- Operating plan: `docs/OPERATING_PLAN.md`

OpenVideoCommons is an experiment in building video AI infrastructure in the open.

If the benchmark network works, we can move toward model adapters, prompt evaluation, data governance, fine-tuning recipes, and eventually community-trained open video foundation models.

But first:

```text
Measure.
Improve.
Train.
```
