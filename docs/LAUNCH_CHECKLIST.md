# Launch Checklist

Use this checklist to publish OpenVideoCommons from a local bootstrap repository to GitHub.

## Repository Setup

- [ ] Create a public GitHub repository under `Geminipo/OpenVideoCommons`.
- [ ] Add a short description: `The global open lab for video AI.`
- [ ] Add topics: `video-ai`, `open-source`, `benchmark`, `generative-ai`, `computer-vision`, `community`.
- [x] Add an initial MIT license for code.
- [ ] Choose long-term licenses for docs, reports, benchmark records, and future datasets.
- [ ] Add repository social preview image after the first visual identity pass.

## First Push

After creating the remote repository:

```bash
git remote add origin https://github.com/Geminipo/OpenVideoCommons.git
git add .
git commit -m "feat: bootstrap OpenVideoCommons"
git push -u origin main
```

## GitHub Project Hygiene

- [ ] Run the `Launch Operations` workflow from the GitHub Actions tab to create labels and first issues.
- [ ] Confirm the `Weekly Operations` workflow is enabled for Monday check-ins.
- [ ] Enable GitHub Discussions.
- [ ] Add issue labels: `good first issue`, `benchmark`, `schema`, `docs`, `governance`, `model-adapter`, `safety`, `data`.
- [ ] Create pinned issues for first benchmark contributors.
- [ ] Create a discussion thread: `Introduce yourself and your hardware`.
- [ ] Protect `main` once the first external contributor appears.

Launch assets:

- Issue drafts: `docs/launch/issues/`
- Label list: `docs/launch/LABELS.md`
- Discussion starters: `docs/launch/DISCUSSIONS.md`
- Announcement copy: `docs/launch/ANNOUNCEMENT.md`
- Local launch helper: `python scripts/print_launch_tasks.py`

## First Public Milestone

- [ ] Recruit 10 benchmark runners.
- [ ] Collect at least 5 hardware profiles.
- [ ] Validate every submitted result against the schema.
- [ ] Publish `reports/community-benchmark-report-001.md`.

## Announcement Draft

Short version:

> I am launching OpenVideoCommons: the global open lab for video AI. We start with transparent benchmarks for open video models on real consumer hardware. First we measure. Then we improve. Then we train.

Call to action:

> If you have a GPU, run a benchmark. If you do not, help review prompts, docs, safety, and evaluation methods.
