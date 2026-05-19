# First Issues

Create these GitHub issues after launch to help contributors start quickly.

## Good First Issues

### Validate the sample benchmark flow on your machine

Labels: `good first issue`, `benchmark`

Run:

```bash
python -m ovc detect-hardware
python -m ovc validate results/benchmark/wan2.1/example-contributor-local.json
```

Report your OS, Python version, and any setup friction.

### Improve hardware metadata detection

Labels: `good first issue`, `cli`

The current CLI reports basic platform information only. Add optional GPU detection for one environment, such as `nvidia-smi`, Apple Silicon, or ROCm, without making it a required dependency.

### Review the first prompt set

Labels: `good first issue`, `prompt-set`

Review `prompts/motion-basic-v1.json` and suggest prompts that better test temporal consistency, motion, camera movement, and object persistence.

## Benchmark Issues

### Submit the first real Wan2.1 benchmark record

Labels: `benchmark`, `model-adapter`

Run a reproducible Wan2.1 benchmark using `motion-basic-v1`, generate a result JSON file, validate it, and open a pull request.

### Define the first human evaluation rubric

Labels: `benchmark`, `research`, `safety`

Draft a simple 1-5 scoring rubric for generated video quality, temporal consistency, prompt adherence, artifacts, and safety concerns.

## Infrastructure Issues

### Add JSON Schema validation support

Labels: `schema`, `cli`

The current validator is a minimal standard-library checker. Add optional JSON Schema validation while keeping the CLI usable without network access.

### Generate a Markdown report from benchmark records

Labels: `reports`, `cli`

Improve the existing report generator:

```bash
python -m ovc generate-report \
  --results-dir results/benchmark \
  --title "Community Benchmark Report 001" \
  --output reports/community-benchmark-report-001.md
```

Useful next improvements include grouping by model, adding success-rate summaries, and preserving human-written report sections.

## Governance Issues

### Choose content and data licenses

Labels: `governance`, `data`, `safety`

Recommend licenses for documentation, reports, benchmark records, prompt sets, and future datasets. Explain trade-offs for open research and commercial reuse.
