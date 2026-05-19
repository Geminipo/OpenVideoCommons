from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    print("OpenVideoCommons launch operations")
    print()
    print("1. In GitHub, open Actions -> Launch Operations -> Run workflow.")
    print("2. Keep create_labels=true and create_issues=true.")
    print("3. Enable Discussions in repository settings.")
    print()
    print("If you need to create issues manually, use these drafts:")
    print()
    for path in sorted((ROOT / "docs" / "launch" / "issues").glob("*.md")):
        title = path.read_text(encoding="utf-8").splitlines()[0].removeprefix("# ").strip()
        print(f"- {title}: {path.relative_to(ROOT)}")
    print()
    print("Labels:")
    print(f"- {(ROOT / 'docs' / 'launch' / 'LABELS.md').relative_to(ROOT)}")
    print()
    print("Discussion starters:")
    print(f"- {(ROOT / 'docs' / 'launch' / 'DISCUSSIONS.md').relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
