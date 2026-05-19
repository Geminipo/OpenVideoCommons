# RFC 0001: Benchmark Result Records

Status: draft

## Context

OpenVideoCommons needs a contribution format that is simple enough for early GitHub pull requests and strict enough to support future verification.

## Proposal

Use versioned JSON files as the first benchmark result record format.

Each record should include:

- Schema version.
- Task id.
- Contributor GitHub handle.
- Model name and version.
- Prompt set name and version.
- Hardware metadata.
- Software metadata.
- Run status and duration.
- Artifact hashes or references.
- Verification status.

## Why Not a Server First?

A central task server is useful later, but it creates operational complexity too early. File-based submissions let the community validate the workflow, schema, review process, and report format before adding infrastructure.

## Verification Levels

- `self_reported`: submitted by a contributor, not independently reviewed.
- `reviewed`: checked by a maintainer or reviewer.
- `accepted`: included in public reports.
- `rejected`: not accepted, with reason documented when safe.

## Open Questions

- Should generated artifacts be stored externally, by hash only, or through Git LFS?
- Should hardware detection be expanded with optional GPU-specific probes?
- What fields should become required after Phase 1?
