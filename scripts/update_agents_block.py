#!/usr/bin/env python3
"""Insere ou atualiza o bloco gerenciado em AGENTS.md sem apagar o restante."""

# Feito por: https://github.com/GabrielPazBR/

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path


START = "<!-- agente-de-projeto:start -->"
END = "<!-- agente-de-projeto:end -->"
PLACEHOLDER = re.compile(r"__[A-Z0-9_]+__")


def unmanaged_hash(content: str) -> str:
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    unmanaged = pattern.sub("", content).strip().replace("\r\n", "\n")
    return hashlib.sha256(unmanaged.encode("utf-8")).hexdigest()


def merge(existing: str, block: str) -> str:
    if block.count(START) != 1 or block.count(END) != 1:
        raise ValueError("o bloco renderizado deve conter um par de marcadores")
    placeholders = sorted(set(PLACEHOLDER.findall(block)))
    if placeholders:
        raise ValueError(f"o bloco ainda contém placeholders: {placeholders}")
    if existing.count(START) != existing.count(END):
        raise ValueError("AGENTS.md contém marcadores incompletos")
    if existing.count(START) > 1:
        raise ValueError("AGENTS.md contém blocos gerenciados duplicados")

    rendered = block.strip()
    if START in existing:
        begin = existing.index(START)
        finish = existing.index(END, begin) + len(END)
        return existing[:begin] + rendered + existing[finish:]
    if existing.strip():
        return existing.rstrip() + "\n\n" + rendered + "\n"
    return rendered + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument("block_file", type=Path)
    args = parser.parse_args()

    root = args.workspace.expanduser().resolve()
    block_path = args.block_file.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"workspace inexistente: {root}")
    if not block_path.is_file():
        parser.error(f"bloco inexistente: {block_path}")

    agents_path = root / "AGENTS.md"
    if agents_path.is_file():
        raw = agents_path.read_bytes()
        existing = raw.decode("utf-8").replace("\r\n", "\n")
        newline = "\r\n" if b"\r\n" in raw else "\n"
    else:
        existing = ""
        newline = "\n"

    block = block_path.read_text(encoding="utf-8")
    baseline = unmanaged_hash(existing)
    merged = merge(existing, block)
    if unmanaged_hash(merged) != baseline:
        raise RuntimeError("o conteúdo externo ao bloco seria alterado")

    agent_dir = root / ".agent"
    agent_dir.mkdir(parents=True, exist_ok=True)
    (agent_dir / "agents-unmanaged.sha256").write_text(
        baseline + "\n", encoding="utf-8", newline="\n"
    )
    agents_path.write_bytes(merged.replace("\n", newline).encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
