# Repository Hygiene

Use this to keep the GitHub repository discoverable and ready for contributors.

## Recommended Repository Metadata

Description:

```text
The global open lab for video AI: transparent benchmarks, reproducible evaluation, and community-powered open video model progress.
```

Topics:

```text
video-ai
open-source
benchmark
generative-ai
computer-vision
evaluation
community
open-video
```

Homepage:

```text
https://github.com/Geminipo/OpenVideoCommons
```

## Automation

Run the `Repository Hygiene` workflow from GitHub Actions.

If the default `GITHUB_TOKEN` cannot update metadata or topics, create a fine-grained personal access token with repository administration permissions and save it as:

```text
REPO_ADMIN_TOKEN
```

Then rerun the workflow.

## Manual Fallback

If automation is blocked:

1. Open repository `Settings`.
2. Edit the description.
3. Add the topics listed above.
4. Disable Wiki unless the project decides to use it.
5. Keep Issues, Actions, and Discussions enabled.
