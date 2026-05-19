# OpenVideoCommons

**The global open lab for video AI.**

OpenVideoCommons is an open coordination layer for video AI: transparent benchmarks, reproducible evaluation records, dataset curation workflows, fine-tuning recipes, distributed contribution tasks, and eventually community-trained open video foundation models.

Our route is intentionally simple:

> First we measure. Then we improve. Then we train.

We are not starting with large-scale distributed training. We are starting with the part every serious open video model needs first: credible, reproducible, community-powered evaluation on real consumer hardware.

## Benchmark Round 001 Is Open

We are looking for the first contributors to validate OpenVideoCommons on real machines.

Your first contribution can be small:

```bash
git clone https://github.com/Geminipo/OpenVideoCommons.git
cd OpenVideoCommons
python -m unittest discover -s tests
python -m ovc doctor
python -m ovc detect-hardware
python -m ovc validate results/benchmark/wan2.1/example-contributor-local.json
python -m ovc create-smoke-result \
  --github YOUR_GITHUB_USERNAME \
  --output results/benchmark/smoke-test/YOUR_GITHUB_USERNAME.json
```

Then open an issue or discussion with:

- Your operating system and Python version.
- Your CPU/GPU or Apple Silicon hardware.
- Whether the CLI worked.
- Any friction, error, or setup confusion.

The first public milestone is simple: **10 benchmark runners, 5 hardware profiles, and Community Benchmark Report 001.**

See [docs/OPERATING_PLAN.md](docs/OPERATING_PLAN.md) for the 30/60/90 day execution plan.

Read [Launch Note 001](reports/launch-note-001.md) for the public project rationale and first contribution path.

## First Contribution: Hardware Smoke Test

The easiest way to help is to submit a hardware smoke-test record. This does **not** run a heavy video model.

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

If auto-detection misses your hardware, add manual fields:

```bash
python -m ovc create-smoke-result \
  --github YOUR_GITHUB_USERNAME \
  --gpu "RTX 4090" \
  --vram-gb 24 \
  --ram-gb 64 \
  --output results/benchmark/smoke-test/YOUR_GITHUB_USERNAME-rtx4090.json
```

Open a pull request with the generated JSON, or paste your `doctor` output into issue #1.

## Why This Exists

Video AI is becoming a major creative and scientific infrastructure. Today, much of that infrastructure is concentrated inside a small number of closed labs with private data, private evaluations, and private training systems.

OpenVideoCommons exists to build the missing open layer:

- Real-world benchmarks across consumer GPUs, CPUs, operating systems, and model versions.
- Reproducible result records with hardware, software, prompt, output, and log hashes.
- Transparent reports that help builders understand which open video models work, fail, and improve.
- Community workflows for data curation, fine-tuning recipes, and eventually coordinated model training.

## What We Are Building First

The first milestone is the **Open Video Model Observatory**: a community benchmark network for open video models.

The MVP should let contributors:

1. Run a local benchmark task.
2. Produce a standardized result JSON file.
3. Submit the result through GitHub.
4. See accepted results included in public reports.

The first implementation is deliberately lightweight. It uses a local CLI and file-based result submissions before introducing any central task server.

## Founder

OpenVideoCommons is initiated by [Geminipo](https://github.com/Geminipo).

## Quick Start

This repository currently ships a minimal Python CLI scaffold with no third-party runtime dependencies.

```bash
python -m ovc --help
python -m ovc doctor
python -m ovc detect-hardware
python -m ovc create-result \
  --model wan2.1 \
  --prompt-set motion-basic-v1 \
  --generation-time-sec 312 \
  --output results/benchmark/sample-result.json
python -m ovc validate results/benchmark/sample-result.json
python -m ovc create-smoke-result \
  --github YOUR_GITHUB_USERNAME \
  --gpu "RTX 4090" \
  --vram-gb 24 \
  --ram-gb 64 \
  --output results/benchmark/smoke-test/YOUR_GITHUB_USERNAME-rtx4090.json
python -m ovc generate-report \
  --results-dir results/benchmark \
  --title "Community Benchmark Report 001" \
  --output reports/community-benchmark-report-001.md
```

Run the test suite:

```bash
python -m unittest discover -s tests
```

## Contribution Paths

You can participate even before distributed training exists:

- **Runner:** run benchmarks on local hardware and submit result records.
- **Evaluator:** review generated videos and score quality, safety, and failure modes.
- **Engineer:** improve the CLI, model adapters, schemas, validators, and report tooling.
- **Researcher:** design prompt sets, metrics, evaluation methods, and public reports.
- **Curator:** help define legal, traceable, high-quality video data workflows.
- **Model Hacker:** contribute LoRA recipes, inference optimizations, adapters, and failure analyses.
- **Guardian:** review license, safety, abuse, privacy, and governance risks.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the first contribution loop.

## Repository Map

```text
ovc/                 Minimal OpenVideoCommons CLI package.
schemas/             Versioned JSON schemas for contribution records.
prompts/             Prompt sets used for benchmark tasks.
results/             Community-submitted benchmark records.
reports/             Public benchmark reports and monthly updates.
docs/                Manifesto, roadmap, governance, and design notes.
tests/               Unit tests for the CLI and schemas.
```

## Project Principles

- **Transparent over impressive:** reproducible evidence matters more than inflated claims.
- **Consumer hardware first:** the first benchmark network should reflect real machines.
- **No token, no speculation:** this is not a crypto or compute-mining project.
- **Legal by design:** no copyright-unclear data enters official datasets.
- **Verifiable contribution:** every accepted task should produce a record that can be checked.
- **Small tasks, global impact:** ordinary contributors should be able to help without owning a data center.

## Roadmap

- **Phase 0:** Manifesto, governance, CLI scaffold, result schema, first prompt set.
- **Phase 1:** Community benchmark submissions for open video models on real hardware.
- **Phase 2:** Public reports, dashboards, repeated prompt sets, human review workflow.
- **Phase 3:** Distributed data curation tasks: captioning, OCR, ASR, deduplication, quality scoring.
- **Phase 4:** Fine-tuning recipes, LoRA registry, reproducible model improvement experiments.
- **Phase 5:** Community-coordinated distillation, training experiments, and open model releases.

Read the fuller [roadmap](docs/ROADMAP.md).

## Non-Goals

To stay credible, the project explicitly does not start by:

- Claiming we can immediately train a Sora-class model on volunteer PCs.
- Accepting unlicensed or unverifiable video data.
- Building a token, mining economy, or speculative reward system.
- Treating unverifiable benchmark uploads as trusted data.
- Optimizing for hype before repeatable contribution.

## License

Code is released under the [MIT License](LICENSE). Benchmark records, reports, and documentation license choices should be revisited before the first public dataset or report release.
