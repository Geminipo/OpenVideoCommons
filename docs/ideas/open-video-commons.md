# OpenVideoCommons

## Problem Statement

How might we let global contributors participate in open video AI progress without pretending that volunteer PCs can immediately train frontier-scale video models?

## Recommended Direction

OpenVideoCommons should begin as the global open lab for video AI: a benchmark and contribution network that measures open video models on real machines, publishes transparent reports, and gradually expands into data curation, fine-tuning recipes, and community training experiments.

The strongest initial wedge is the Open Video Model Observatory. It gives contributors a concrete first action: run a benchmark, submit a standardized result, and become part of a public report.

## Key Assumptions to Validate

- [ ] Contributors with consumer GPUs will run benchmarks if setup is simple and recognition is visible.
- [ ] Open video model teams value transparent third-party community benchmarks.
- [ ] File-based GitHub submissions are enough to validate the workflow before a task server exists.
- [ ] Public reports create more momentum than raw benchmark data alone.
- [ ] Strict legal and verification boundaries increase trust rather than slowing the community too much.

## MVP Scope

The MVP includes:

- Project manifesto.
- Contribution guide.
- Result schema.
- Minimal CLI.
- First prompt set.
- Sample result.
- Tests.

The MVP does not need:

- A central server.
- Distributed training.
- Token incentives.
- A polished dashboard.
- Support for many video models.

## Not Doing

- Training a frontier video model first, because the trust and data layers are not ready.
- Accepting arbitrary video uploads as training data, because licensing and safety must be designed first.
- Building a token economy, because it would undermine credibility with researchers and open-source developers.
- Supporting every model immediately, because one reliable adapter is better than many broken ones.

## Open Questions

- Which model should be the first official adapter?
- What is the minimum prompt set that produces useful failure signals?
- Should generated videos be stored in Git LFS, external object storage, or only referenced by hashes?
- What license should govern code, documentation, benchmark records, and reports?
