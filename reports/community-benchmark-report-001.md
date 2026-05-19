# Community Benchmark Report 001

Status: draft

## Purpose

This report will summarize the first accepted OpenVideoCommons benchmark submissions for open video models on real consumer hardware.

The first report should answer:

- Which hardware profiles were tested?
- Which open video model versions were tested?
- Which prompt sets were used?
- What succeeded, failed, or produced partial output?
- What setup details were required for reproduction?
- What failure modes appeared repeatedly?

## Methodology

Benchmark records are accepted only when they:

- Validate against the benchmark result schema.
- Include model, prompt set, hardware, software, runtime, and verification status.
- Remove secrets, private paths, and sensitive local information.
- Can be reviewed through a public pull request.

## Current Results

| Model | Hardware | Prompt Set | Status | Runtime | Contributor |
| --- | --- | --- | --- | --- | --- |
| wan2.1 | local bootstrap example | motion-basic-v1 | self-reported | 312s | example-contributor |

## Observations

This section should be filled after real community submissions arrive.

## Known Limits

- The bootstrap sample is not an accepted community benchmark.
- Human quality scoring is not implemented yet.
- Generated video artifact storage is not finalized.

## Next Actions

- Recruit the first 10 benchmark runners.
- Collect at least 5 hardware profiles.
- Add the first reviewed result records.
- Define a human evaluation rubric.
