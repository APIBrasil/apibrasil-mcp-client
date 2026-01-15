from __future__ import annotations

from pathlib import Path

TREE_BEGIN = "<!-- BEGIN:REPO_TREE -->"
TREE_END = "<!-- END:REPO_TREE -->"
INDEX_BEGIN = "<!-- BEGIN:AUTO_INDEX -->"
INDEX_END = "<!-- END:AUTO_INDEX -->"


def _iter_top_level_dirs(repo_root: Path) -> list[Path]:
    return sorted(
        [
            p
            for p in repo_root.iterdir()
            if p.is_dir() and not p.name.startswith(".") and p.name != "scripts"
        ],
        key=lambda p: p.name.lower(),
    )


def _build_tree(repo_root: Path) -> str:
    """
    Generates a folder-only tree with unicode connectors:
    apibrasil-mcp-client
    ├── chatbots-ai
    │   ├── botpress
    ...
    """

    root_name = repo_root.name
    lines: list[str] = [f"{root_name}"]

    categories = _iter_top_level_dirs(repo_root)
    count_cats = len(categories)

    for i, category_dir in enumerate(categories):
        is_last_cat = (i == count_cats - 1)
        prefix_cat = "└── " if is_last_cat else "├── "
        
        lines.append(f"{prefix_cat}{category_dir.name}")

        child_dirs = sorted(
            [p for p in category_dir.iterdir() if p.is_dir() and not p.name.startswith(".")],
            key=lambda p: p.name.lower(),
        )
        count_children = len(child_dirs)
        
        base_indent = "    " if is_last_cat else "│   "

        for j, child_dir in enumerate(child_dirs):
            is_last_child = (j == count_children - 1)
            prefix_child = "└── " if is_last_child else "├── "
            lines.append(f"{base_indent}{prefix_child}{child_dir.name}")

    return "\n".join(lines)


def _extract_title_and_description(readme_path: Path) -> tuple[str, str]:
    """
    Returns (title, description) from a README:
    - title: first markdown heading
    - description: first non-empty paragraph line after the heading (best-effort)
    """

    try:
        raw = readme_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        raw = readme_path.read_text(encoding="utf-8", errors="replace")

    lines = [ln.rstrip() for ln in raw.splitlines()]

    title = readme_path.parent.name
    title_idx = None
    for i, ln in enumerate(lines):
        s = ln.strip()
        if s.startswith("#"):
            title = s.lstrip("#").strip()
            title_idx = i
            break

    desc = ""
    if title_idx is not None:
        in_code = False
        for ln in lines[title_idx + 1 :]:
            s = ln.strip()
            if not s:
                if desc:
                    break
                continue
            if s.startswith("```"):
                in_code = not in_code
                continue
            if in_code:
                continue
            if s.startswith("#"):
                continue
            if s.startswith(">"):
                continue
            # keep it compact
            desc = s
            break

    # cap for readability
    if len(desc) > 160:
        desc = desc[:157].rstrip() + "..."

    return title, desc


def _path_link(repo_root: Path, target: Path) -> str:
    rel = target.relative_to(repo_root).as_posix()
    return f"./{rel}"


def _build_auto_index(repo_root: Path) -> str:
    """
    Auto index grouped by top-level category:
    - includes category-level README.md (if exists)
    - includes 1-level deep subfolders' README.md
    - includes relevant JSON configs (category level + settings.json in subfolders)
    """

    lines: list[str] = []

    for category_dir in _iter_top_level_dirs(repo_root):
        category_link = _path_link(repo_root, category_dir)
        lines.append(f"- **[{category_dir.name}]({category_link})**")

        # Category-level README.md (sometimes it's a real entry like Typebot/n8n/etc.)
        category_readme = category_dir / "README.md"
        if category_readme.exists():
            title, desc = _extract_title_and_description(category_readme)
            readme_link = _path_link(repo_root, category_readme)
            suffix = f" — {desc}" if desc else ""
            lines.append(f"  - [{title}]({readme_link}){suffix}")

        # Category-level JSON configs (ex: claude_desktop_config.json)
        for p in sorted(
            [p for p in category_dir.iterdir() if p.is_file() and p.suffix.lower() == '.json'],
            key=lambda x: x.name.lower(),
        ):
            p_link = _path_link(repo_root, p)
            lines.append(f"  - [`{p.name}`]({p_link})")

        # 1-level deep integrations
        child_dirs = sorted(
            [p for p in category_dir.iterdir() if p.is_dir() and not p.name.startswith(".")],
            key=lambda p: p.name.lower(),
        )
        for child_dir in child_dirs:
            readme = child_dir / "README.md"
            if not readme.exists():
                continue

            title, desc = _extract_title_and_description(readme)
            readme_link = _path_link(repo_root, readme)
            suffix = f" — {desc}" if desc else ""

            settings = child_dir / "settings.json"
            extra = ""
            if settings.exists():
                extra = f" ([settings]({_path_link(repo_root, settings)}))"

            lines.append(f"  - [{title}]({readme_link}){suffix}{extra}")

        lines.append("")  # blank line between categories

    # remove trailing blank line
    while lines and not lines[-1].strip():
        lines.pop()

    return "\n".join(lines).rstrip()

def _replace_between_markers(
    text: str, *, begin: str, end: str, replacement: str, code_fence: str | None = None
) -> str:
    if begin not in text or end not in text:
        raise SystemExit(f"Markers not found in README.md. Expected {begin!r} and {end!r}.")

    before, rest = text.split(begin, 1)
    _old_block, after = rest.split(end, 1)

    middle: list[str] = []
    if code_fence is not None:
        middle.extend([f"```{code_fence}", replacement.rstrip(), "```"])
    else:
        middle.append(replacement.rstrip())

    new_block = "\n".join([begin, *middle, end])

    # Keep surrounding content as-is
    return before.rstrip() + "\n\n" + new_block + after


def main() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    readme_path = repo_root / "README.md"

    if not readme_path.exists():
        raise SystemExit("README.md not found at repository root.")

    original = readme_path.read_text(encoding="utf-8")
    tree = _build_tree(repo_root)
    updated = _replace_between_markers(
        original, begin=TREE_BEGIN, end=TREE_END, replacement=tree, code_fence="text"
    )

    index = _build_auto_index(repo_root)
    updated = _replace_between_markers(
        updated, begin=INDEX_BEGIN, end=INDEX_END, replacement=index, code_fence=None
    )

    if updated != original:
        readme_path.write_text(updated, encoding="utf-8", newline="\n")
        print("README.md updated (auto index + repo tree refreshed).")
    else:
        print("README.md already up to date (no changes).")


if __name__ == "__main__":
    main()

