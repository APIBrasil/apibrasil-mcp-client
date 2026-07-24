#!/usr/bin/env python3
"""
Guard de CI: valida os links relativos de markdown do repositorio.

Percorre todos os `.md`, extrai os links `[texto](destino)` (ignorando blocos de
codigo) e, para destinos locais (nao http/mailto/ancora), confere se o arquivo ou
diretorio-alvo existe. Links externos (http/https) nao sao verificados aqui.

Pega quebras como uma pasta `conceitos/credenciais/` referenciada mas inexistente.
"""
from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "#")


def _iter_md_files() -> list[Path]:
    return [
        p
        for p in REPO_ROOT.rglob("*.md")
        if ".git" not in p.parts and "node_modules" not in p.parts
    ]


def _links_outside_code(text: str) -> list[str]:
    """Coleta os destinos de link, pulando linhas dentro de blocos ``` ```."""
    targets: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        targets.extend(LINK_RE.findall(line))
    return targets


def main() -> int:
    broken: list[str] = []
    checked = 0

    for md in _iter_md_files():
        text = md.read_text(encoding="utf-8", errors="replace")
        for raw in _links_outside_code(text):
            target = raw.strip()
            if target.startswith(SKIP_PREFIXES):
                continue
            # remove ancora e querystring
            path_part = target.split("#", 1)[0].split("?", 1)[0].strip()
            if not path_part:
                continue
            checked += 1
            resolved = (md.parent / path_part).resolve()
            if not resolved.exists():
                rel = md.relative_to(REPO_ROOT).as_posix()
                broken.append(f"{rel} -> {target}")

    if broken:
        print(f"[FALHA] {len(broken)} link(s) relativo(s) quebrado(s):")
        for item in broken:
            print(f"   - {item}")
        return 1

    print(f"[OK] {checked} link(s) relativo(s) verificado(s), nenhum quebrado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
