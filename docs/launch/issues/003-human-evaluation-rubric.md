# Define the first human evaluation rubric

Labels: `benchmark`, `research`, `safety`, `help wanted`

## Goal

Draft a simple scoring rubric for human review of generated video outputs.

## Suggested Dimensions

- Prompt adherence.
- Temporal consistency.
- Object persistence.
- Motion naturalness.
- Visual artifacts.
- Safety concerns.

## Proposed Scale

Use a 1-5 score for each dimension:

- 1: unusable or severely broken.
- 2: major issues.
- 3: mixed but informative.
- 4: mostly successful.
- 5: strong result.

## Deliverable

Create `docs/evaluation/human-rubric-v1.md` with:

- Scoring definitions.
- Reviewer instructions.
- Examples of failure modes.
- Notes on bias, safety, and subjectivity.

## Acceptance Criteria

- The rubric is clear enough for two reviewers to use independently.
- It separates quality failures from safety concerns.
- It does not require paid tools or private datasets.
