# Operating Plan

This plan turns OpenVideoCommons from a published repository into a working open-source project with real contributors, benchmark records, and public reports.

## Operating Thesis

The first stage is not about training a frontier video model. The first stage is about proving that a global community can create trusted, reproducible, useful evaluation records for open video AI.

The operating loop is:

```text
Clear task -> contributor action -> validated record -> public recognition -> report -> more contributors
```

If this loop works, the project earns the right to expand into model adapters, data curation, fine-tuning recipes, and eventually coordinated training experiments.

## Positioning

Primary message:

> OpenVideoCommons is building the global open benchmark network for video AI.

Call to action:

> Help us benchmark open video models on real consumer hardware.

Avoid early claims that volunteer PCs can immediately train frontier video models. That may be a long-term research direction, but it is not the first credible milestone.

## 30 Day Plan: Make The Project Alive

Goal: get the first real contributors and prove the benchmark contribution loop.

Targets:

- 100 GitHub stars.
- 10 GitHub issues.
- 3 external pull requests.
- 5 real benchmark or smoke-test records.
- 3 hardware profiles.
- 3-5 active contributors.
- 1 mini report update.

Week 1 actions:

- Enable GitHub Discussions.
- Create labels from `docs/launch/LABELS.md`.
- Create the first 6 issues from `docs/launch/issues/`.
- Create the first discussion from `docs/launch/DISCUSSIONS.md`.
- Publish the short launch announcement from `docs/launch/ANNOUNCEMENT.md`.
- Ask 10 people with GPUs or Apple Silicon to run the smoke-test flow.

Week 2 actions:

- Reply to every issue and discussion within 24 hours.
- Convert repeated setup friction into `good first issue` tasks.
- Improve hardware detection if multiple contributors report missing metadata.
- Publish a short progress update: contributors, hardware profiles, test results.

Week 3 actions:

- Select the first official model adapter target.
- Draft `docs/evaluation/human-rubric-v1.md`.
- Ask for reviewers who can help evaluate generated video outputs.
- Start collecting first real benchmark result PRs.

Week 4 actions:

- Generate and publish `reports/community-benchmark-report-001.md`.
- Thank every contributor by GitHub handle.
- Summarize what worked, what failed, and what the next benchmark round needs.

## 60 Day Plan: Make Contributions Repeatable

Goal: turn one-off attention into a repeatable contribution process.

Targets:

- 300 GitHub stars.
- 10 external PRs.
- 20 benchmark records.
- 8 hardware profiles.
- 1 external maintainer candidate.
- Report 001 with real community data.

Execution themes:

- Make `ovc detect-hardware` more useful across NVIDIA, Apple Silicon, and AMD/ROCm.
- Add a first model adapter workflow or documented manual benchmark recipe.
- Add a human evaluation rubric.
- Improve generated reports with success rates and grouped summaries.
- Create a contributor recognition section in reports.

Community roles:

- Runner: runs benchmarks and submits result records.
- Reviewer: checks result validity and reproducibility.
- Prompt Designer: improves benchmark prompt sets.
- Engineer: improves CLI, schema, adapters, and report tooling.
- Safety/Data Guardian: reviews privacy, licensing, abuse, and provenance concerns.

## 90 Day Plan: Form A Small Open Lab

Goal: evolve from a founder-led repository into a small open-source project with visible working groups.

Targets:

- 800 GitHub stars.
- 25 external PRs.
- 50 benchmark records.
- 20 contributors.
- 5 recurring contributors.
- At least one model team, researcher, or well-known builder engages with the project.

Deliverables:

- `Community Benchmark Report 001` final version.
- One repeatable model adapter or benchmark recipe.
- Human evaluation rubric v1.
- License RFC for docs, reports, records, prompts, and future datasets.
- Working group structure:
  - Benchmark Working Group.
  - Model Adapter Working Group.
  - Safety and Data Governance Working Group.

## Weekly Operating Rhythm

Monday: progress update.

- New benchmark records.
- New contributors.
- Hardware profiles covered.
- Current blockers.
- This week's help requests.

Wednesday: technical question.

- Prompt design.
- Evaluation methods.
- Hardware detection.
- Model adapter trade-offs.
- Report methodology.

Friday: contributor call.

- Ask for specific hardware profiles.
- Promote good first issues.
- Thank merged contributors.
- Highlight one useful failure or lesson.

## Outreach Strategy

Start narrow. Do not ask "the world" to join. Ask specific people to do specific actions.

First 10 outreach targets:

- People running Wan2.1, HunyuanVideo, CogVideoX, or Open-Sora locally.
- ComfyUI video workflow authors.
- Hugging Face video demo builders.
- Owners of RTX 3060, RTX 4090, Apple Silicon, and high-VRAM workstation GPUs.
- Researchers or engineers who care about evaluation and reproducibility.

Message template:

```text
Hi, I am launching OpenVideoCommons, a community benchmark network for open video AI.

We are starting small: collect reproducible benchmark and smoke-test results for open video models on real consumer hardware.

If you have a GPU or Apple Silicon machine, would you be open to running the first benchmark flow and sharing feedback?

Repo: https://github.com/Geminipo/OpenVideoCommons
```

## Success Metrics

Activity metrics:

- Stars.
- Issues.
- Pull requests.
- Discussions.
- External contributors.

Trust metrics:

- Valid benchmark records.
- Hardware profiles covered.
- Reproducible failures documented.
- Reports published.
- Review turnaround time.

Quality metrics:

- Test pass rate.
- Schema validity.
- Report clarity.
- Safety and license review coverage.

## Risks And Mitigations

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The project sounds too ambitious | People dismiss it as hype | Lead with benchmark network, not frontier training |
| Contributors do not know what to do | No real activity | Keep issues small, concrete, and labeled |
| Benchmark records are not trustworthy | Reports lose credibility | Require schema validation, logs, and review status |
| Data licensing becomes messy | Legal and trust risk | Do not accept training data until governance is ready |
| It attracts token/mining narratives | Serious contributors leave | Explicitly reject token and mining incentives |
| Founder becomes bottleneck | Project stalls | Recruit reviewers and working group leads by Day 90 |

## Immediate Checklist

- [ ] Enable GitHub Discussions.
- [ ] Create labels from `docs/launch/LABELS.md`.
- [ ] Create 6 launch issues from `docs/launch/issues/`.
- [ ] Create the first discussion: "Introduce yourself and your hardware".
- [ ] Post the short launch announcement.
- [ ] Ask 10 target contributors to run the smoke test.
- [ ] Publish the first weekly progress update.
