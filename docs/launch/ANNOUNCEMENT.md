# Launch Announcement

## Short Post

I am launching **OpenVideoCommons**: the global open lab for video AI.

We are starting with transparent benchmarks for open video models on real consumer hardware.

First we measure. Then we improve. Then we train.

If you have a GPU, help run benchmarks. If you do not, help with prompts, documentation, evaluation, safety, and data governance.

Repository: https://github.com/Geminipo/OpenVideoCommons

## Longer Post

Video AI is becoming one of the most important creative and scientific infrastructures of the next decade. But too much of that infrastructure is being built behind closed doors: private data, private evaluation, private training systems, and private failure analysis.

OpenVideoCommons is an attempt to build the missing open layer.

We are not starting by claiming that volunteer PCs can immediately train a frontier video model. We are starting with the part every serious open model needs first: credible measurement.

The first milestone is the **Open Video Model Observatory**:

- Run open video model benchmarks on real consumer machines.
- Submit standardized result records.
- Publish transparent community reports.
- Build trust before training.

This project is for:

- GPU owners who want to contribute useful benchmark data.
- Engineers who want reproducible open video model tooling.
- Researchers who care about transparent evaluation.
- Creators who want to understand which open video models really work.
- Safety and data contributors who want video AI to develop in the open.

No token. No mining. No speculative reward system.

Just open infrastructure, reproducible records, and global contribution.

Repository: https://github.com/Geminipo/OpenVideoCommons

## Call To Action

Start here:

```bash
git clone https://github.com/Geminipo/OpenVideoCommons.git
cd OpenVideoCommons
python -m unittest discover -s tests
python -m ovc detect-hardware
python -m ovc validate results/benchmark/wan2.1/example-contributor-local.json
```

Then introduce your hardware in GitHub Discussions or open an issue using the benchmark template.
