#!/usr/bin/env python3
"""Valida os artefatos persistentes gerados por agente-de-projeto."""

# Feito por: https://github.com/GabrielPazBR/

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path


START = "<!-- agente-de-projeto:start -->"
END = "<!-- agente-de-projeto:end -->"
PLACEHOLDER = re.compile(r"__[A-Z0-9_]+__")
ESSENTIAL_AGENTS_POINTERS = (
    ".agent/profile.yaml",
    ".agent/manifest.yaml",
    ".agent/instructions/gemini.md",
    ".agent/instructions/linguagem-usuario.md",
    "mempalace instructions",
    "RTK",
)


def read_text(path: Path, issues: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        issues.append(f"arquivo não está em UTF-8: {path}")
    except OSError as exc:
        issues.append(f"não foi possível ler {path}: {exc}")
    return ""


def top_level_mapping_value(content: str, section: str, key: str) -> str | None:
    in_section = False
    for raw_line in content.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        if indent == 0:
            in_section = stripped == f"{section}:"
            continue
        if in_section and indent == 2 and stripped.startswith(f"{key}:"):
            value = stripped.split(":", 1)[1].strip()
            return value.strip("\"'")
    return None


def unmanaged_agents_hash(content: str) -> str:
    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END),
        flags=re.DOTALL,
    )
    unmanaged = pattern.sub("", content).strip().replace("\r\n", "\n")
    return hashlib.sha256(unmanaged.encode("utf-8")).hexdigest()


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    args = parser.parse_args()

    root = args.workspace.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"workspace inexistente: {root}")

    issues: list[str] = []
    warnings: list[str] = []
    required = [
        root / "AGENTS.md",
        root / ".agent/manifest.yaml",
        root / ".agent/profile.yaml",
        root / ".agent/skill-sources.lock.yaml",
        root / ".agent/agents-unmanaged.sha256",
        root / ".agent/instructions/gemini.md",
        root / ".agent/instructions/linguagem-usuario.md",
        root / ".agent/memory",
    ]
    for path in required:
        if not path.exists():
            issues.append(f"ausente: {path}")

    agents_path = root / "AGENTS.md"
    agents = read_text(agents_path, issues) if agents_path.is_file() else ""
    if agents:
        if agents.count(START) != 1 or agents.count(END) != 1:
            issues.append("AGENTS.md deve conter um único bloco agente-de-projeto")
        if agents.find(START) > agents.find(END):
            issues.append("marcadores do bloco agente-de-projeto estão fora de ordem")
        if "uploads-web.md" in agents and not (
            root / ".agent/instructions/uploads-web.md"
        ).is_file():
            issues.append("AGENTS.md referencia uploads-web.md inexistente")
        placeholders = sorted(set(PLACEHOLDER.findall(agents)))
        if placeholders:
            issues.append(f"placeholders não preenchidos em AGENTS.md: {placeholders}")
        for pointer in ESSENTIAL_AGENTS_POINTERS:
            if pointer not in agents:
                issues.append(f"AGENTS.md não contém instrução essencial: {pointer}")
        baseline_path = root / ".agent/agents-unmanaged.sha256"
        if baseline_path.is_file():
            baseline = read_text(baseline_path, issues).strip()
            current = unmanaged_agents_hash(agents)
            if baseline != current:
                issues.append("conteúdo externo ao bloco gerenciado de AGENTS.md foi alterado")

    for relative in (
        ".agent/manifest.yaml",
        ".agent/profile.yaml",
        ".agent/skill-sources.lock.yaml",
        ".agent/instructions/gemini.md",
        ".agent/instructions/linguagem-usuario.md",
    ):
        path = root / relative
        if not path.is_file():
            continue
        content = read_text(path, issues)
        placeholders = sorted(set(PLACEHOLDER.findall(content)))
        if placeholders:
            issues.append(f"placeholders não preenchidos em {relative}: {placeholders}")

    profile_path = root / ".agent/profile.yaml"
    if profile_path.is_file():
        profile = read_text(profile_path, issues)
        if "confirmed_by_user: true" not in profile:
            issues.append("profile.yaml ainda não foi confirmado pelo usuário")

    manifest_path = root / ".agent/manifest.yaml"
    if manifest_path.is_file():
        manifest = read_text(manifest_path, issues)
        if top_level_mapping_value(manifest, "bootstrap", "status") != "complete":
            issues.append("bootstrap.status no manifesto ainda não é complete")

    for executable in ("rtk", "mempalace", "node", "npx"):
        if not shutil.which(executable):
            issues.append(f"executável obrigatório não encontrado no PATH: {executable}")

    result = {
        "workspace": str(root),
        "passed": not issues,
        "issues": issues,
        "warnings": warnings,
        "note": "handshakes MCP e provas de persistência devem ser validados separadamente",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
