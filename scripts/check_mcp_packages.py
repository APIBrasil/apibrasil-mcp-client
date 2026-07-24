#!/usr/bin/env python3
"""
Guard de CI: garante que todo pacote npm usado como ponte nas configs deste
repositorio realmente existe no registry.

Foi a ausencia desta checagem que deixou um pacote-ponte inexistente
(`@modelcontextprotocol/server-sse-client`) espalhado por dezenas de arquivos.

O teste extrai os pacotes usados apos `-y` (forma JSON `"-y","<pkg>"` e forma
shell `npx -y <pkg>` / `Args: -y <pkg>`) e roda `npm view <pkg> version` em cada
um. Se um pacote nao existir (404), o CI falha. Assim, reintroduzir um pacote
inexistente em qualquer config quebra a build.
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Toda ponte referenciada nas configs deve existir no npm publico.
ALLOWLIST: set[str] = set()

PKG_NAME_RE = re.compile(r"^(?:@[a-z0-9][a-z0-9._-]*/)?[a-z0-9][a-z0-9._-]*$")
JSON_ARG_RE = re.compile(r'"-y"\s*,\s*"([^"]+)"')
SHELL_ARG_RE = re.compile(r"-y\s+([^\s\"'`]+)")


def _iter_text_files() -> list[Path]:
    files: list[Path] = []
    for pattern in ("*.md", "*.json"):
        for path in REPO_ROOT.rglob(pattern):
            if ".git" in path.parts or "node_modules" in path.parts:
                continue
            files.append(path)
    return files


def _extract_packages() -> set[str]:
    packages: set[str] = set()
    for path in _iter_text_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in JSON_ARG_RE.findall(text) + SHELL_ARG_RE.findall(text):
            candidate = match.strip()
            if PKG_NAME_RE.match(candidate) and candidate not in ALLOWLIST:
                packages.add(candidate)
    return packages


def main() -> int:
    packages = _extract_packages()

    if not packages:
        print("Nenhum pacote npm de ponte encontrado para verificar.")
        return 0

    print(f"Verificando {len(packages)} pacote(s) no npm: {', '.join(sorted(packages))}")
    missing: list[str] = []
    for pkg in sorted(packages):
        result = subprocess.run(
            ["npm", "view", pkg, "version"],
            capture_output=True,
            text=True,
            shell=(sys.platform == "win32"),
        )
        if result.returncode != 0:
            missing.append(pkg)
            print(f"   [FALHA] {pkg} - nao encontrado no registry")
        else:
            print(f"   [OK]    {pkg}@{result.stdout.strip()}")

    if missing:
        print(f"\n[FALHA] Pacote(s) inexistente(s): {', '.join(missing)}")
        return 1

    print("\n[OK] Todos os pacotes de ponte existem no npm.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
