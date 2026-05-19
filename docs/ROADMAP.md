# Roadmap

This roadmap keeps the project credible by sequencing the work from easiest to verify to hardest to coordinate.

## Phase 0: Project Foundation

Goal: make the project understandable, trustworthy, and runnable.

Deliverables:

- Public README and manifesto.
- Contribution guide.
- Governance draft.
- Result schema.
- Minimal CLI.
- First prompt set.
- Unit tests for schema validation.

Exit criteria:

- A contributor can generate and validate a benchmark result locally.
- The project can explain what it does not do yet.

## Phase 1: Open Video Model Observatory

Goal: collect reproducible benchmark records from real consumer machines.

Deliverables:

- Model adapter interface.
- Support for one open video model family.
- Hardware and software metadata capture.
- Result submission workflow through pull requests.
- Review checklist for accepted results.

Exit criteria:

- At least 10 accepted community result records.
- At least 5 hardware profiles represented.
- At least 1 public mini-report.

## Phase 2: Public Reports and Human Evaluation

Goal: turn raw records into useful ecosystem knowledge.

Deliverables:

- Report generator.
- Human evaluation rubric.
- Failure taxonomy.
- Prompt set versioning.
- Public leaderboard or static dashboard.

Exit criteria:

- Monthly report cadence.
- Repeatable benchmark set.
- Clear distinction between machine metrics and human ratings.

## Phase 3: Distributed Data Curation

Goal: add small, verifiable data tasks that do not require centralized training.

Task types:

- Video metadata extraction.
- Caption review.
- ASR/OCR validation.
- Scene boundary checks.
- Deduplication.
- Quality and safety review.
- License and provenance verification.

Exit criteria:

- Every accepted data artifact has provenance, license metadata, and reviewer status.
- No training dataset admits unverifiable source material.

## Phase 4: Fine-Tuning and LoRA Recipes

Goal: help open video models improve through reproducible community experiments.

Deliverables:

- Recipe format.
- LoRA registry.
- Evaluation-before-and-after workflow.
- Model card extension for community experiments.

Exit criteria:

- Community recipes can be reproduced by independent contributors.
- Improvements are measured against public prompt sets.

## Phase 5: Community Training Experiments

Goal: attempt coordinated training, distillation, or reinforcement experiments only after the trust layer exists.

Candidate approaches:

- Distillation from open models.
- Domain-specific video understanding models.
- Federated or loosely coordinated fine-tuning.
- Small foundation model experiments with transparent data.

Exit criteria:

- Clear compute plan.
- Clear data license plan.
- Clear verification and safety plan.
- Public model card and release process.
