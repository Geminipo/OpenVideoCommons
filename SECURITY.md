# Security Policy

OpenVideoCommons handles benchmark records, model tooling, and eventually data curation workflows. Trust and safety are part of the core infrastructure.

## Reporting Issues

For now, open a private security advisory on GitHub once the repository is public. If that is not available, contact the maintainer through the GitHub profile listed in the README.

Please do not publicly disclose exploitable issues before maintainers have had a reasonable chance to respond.

## In Scope

- Unsafe command execution in CLI tooling.
- Result validation bypasses that could poison public reports.
- Malicious benchmark artifacts or links.
- Privacy leaks in submitted records.
- Data provenance or license issues that could affect official datasets.

## Out of Scope

- Unsupported local model execution environments.
- Third-party model vulnerabilities outside this repository.
- Speculative reward, mining, or token integrations, which are not part of this project.

## Safety Defaults

- Do not include private paths, secrets, API keys, or personal files in benchmark logs.
- Do not upload private or sensitive videos.
- Do not submit generated content that targets real private individuals without consent.
