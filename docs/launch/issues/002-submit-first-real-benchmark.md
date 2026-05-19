# Submit the first real Wan2.1 benchmark record

Labels: `benchmark`, `model-adapter`, `help wanted`

## Goal

Create the first real, reproducible benchmark record for Wan2.1 using `motion-basic-v1`.

## Scope

This issue is not asking for a full automated model adapter yet. A careful manually generated result record is enough for the first contribution.

## Steps

1. Run Wan2.1 locally using one or more prompts from `prompts/motion-basic-v1.json`.
2. Generate a result JSON file with:

```bash
python -m ovc create-result \
  --github YOUR_GITHUB_USERNAME \
  --model wan2.1 \
  --model-version MODEL_OR_CHECKPOINT_VERSION \
  --model-source https://github.com/Wan-Video/Wan2.1 \
  --prompt-set motion-basic-v1 \
  --prompt-set-version 1.0.0 \
  --generation-time-sec SECONDS \
  --output results/benchmark/wan2.1/YOUR_GITHUB_USERNAME-HARDWARE.json
```

3. Validate the result:

```bash
python -m ovc validate results/benchmark/wan2.1/YOUR_GITHUB_USERNAME-HARDWARE.json
```

4. Open a pull request.

## Acceptance Criteria

- The JSON result validates.
- The record includes enough hardware and software context to reproduce the run.
- No private paths, secrets, or sensitive local files are included.
