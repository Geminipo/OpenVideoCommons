# Improve generated benchmark reports

Labels: `reports`, `cli`, `good first issue`

## Goal

Improve the current report generator:

```bash
python -m ovc generate-report \
  --results-dir results/benchmark \
  --title "Community Benchmark Report 001" \
  --output reports/community-benchmark-report-001.md
```

## Useful Improvements

- Group rows by model.
- Add success-rate summaries.
- Add average runtime by hardware profile.
- Preserve human-written sections when regenerating a report.
- Add a `--min-verification-status` option.

## Acceptance Criteria

- Tests cover the new behavior.
- The generated report remains readable in plain Markdown.
- Invalid result records are skipped or reported clearly.
