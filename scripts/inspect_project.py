#!/usr/bin/env python3
"""Inspeciona um workspace sem modificar arquivos."""

# Feito por: https://github.com/GabrielPazBR/

from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


VERSION_COMMANDS = {
    "git": ["git", "--version"],
    "python": [sys.executable, "--version"],
    "uv": ["uv", "--version"],
    "node": ["node", "--version"],
    "npm": ["npm", "--version"],
    "npx": ["npx", "--version"],
    "rtk": ["rtk", "--version"],
    "mempalace": ["mempalace", "--help"],
    "gemini": ["gemini", "--version"],
    "agy": ["agy", "--version"],
    "docker": ["docker", "--version"],
}

PROJECT_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    ".agent/manifest.yaml",
    ".agent/profile.yaml",
    ".codex/config.toml",
    ".mcp.json",
    "mcp.json",
    "package.json",
    "pyproject.toml",
    "Cargo.toml",
    "pnpm-workspace.yaml",
]

LOCKFILES = [
    "uv.lock",
    "poetry.lock",
    "package-lock.json",
    "pnpm-lock.yaml",
    "yarn.lock",
    "bun.lock",
    "bun.lockb",
    "Cargo.lock",
]


def run(command: list[str], cwd: Path | None = None) -> dict[str, Any]:
    resolved = shutil.which(command[0])
    invocation = command
    if os.name == "nt" and resolved and Path(resolved).suffix.lower() in {".cmd", ".bat"}:
        invocation = [
            os.environ.get("COMSPEC", "cmd.exe"),
            "/d",
            "/c",
            resolved,
            *command[1:],
        ]
    try:
        completed = subprocess.run(
            invocation,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=8,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"ok": False, "error": str(exc)}

    output = (completed.stdout or completed.stderr).strip()
    return {
        "ok": completed.returncode == 0,
        "exit_code": completed.returncode,
        "output": output[:1000],
    }


def executable_state(name: str, command: list[str]) -> dict[str, Any]:
    executable = command[0]
    path = shutil.which(executable)
    if executable == sys.executable:
        path = sys.executable
    if not path:
        return {"found": False}
    result = run(command)
    return {"found": True, "path": path, "probe": result}


def git_state(root: Path) -> dict[str, Any]:
    if not shutil.which("git"):
        return {"available": False}
    repository = run(["git", "rev-parse", "--show-toplevel"], root)
    state: dict[str, Any] = {"available": True, "repository": repository}
    if repository.get("ok"):
        state["status"] = run(["git", "status", "--short"], root)
        state["remotes"] = run(["git", "remote"], root)
    return state


def skill_names(root: Path) -> list[str]:
    names: set[str] = set()
    for relative in (Path(".agents/skills"), Path(".agent/skills")):
        directory = root / relative
        if not directory.is_dir():
            continue
        for child in directory.iterdir():
            if child.is_dir() and (child / "SKILL.md").is_file():
                names.add(child.name)
    return sorted(names)


def catalog_skills(
    path: Path, scope: str, include_entries: bool, limit: int = 300
) -> dict[str, Any]:
    if not path.is_dir():
        return {"scope": scope, "path": str(path), "exists": False, "count": 0}
    skill_files = sorted(path.rglob("SKILL.md"))
    entries = [
        {"name": skill_file.parent.name, "path": str(skill_file.parent)}
        for skill_file in skill_files[:limit]
    ]
    result: dict[str, Any] = {
        "scope": scope,
        "path": str(path),
        "exists": True,
        "count": len(skill_files),
        "sample_names": [entry["name"] for entry in entries[:20]],
    }
    if include_entries:
        result["skills"] = entries
        result["truncated"] = len(skill_files) > limit
    return result


def client_scope(include_catalog_entries: bool) -> dict[str, Any]:
    home = Path.home()
    codex_home = Path(os.environ.get("CODEX_HOME", home / ".codex")).expanduser()
    config_candidates = [
        codex_home / "config.toml",
        codex_home / "mcp.json",
        home / ".claude/settings.json",
        home / ".claude/mcp.json",
        home / ".cursor/mcp.json",
        home / ".gemini/settings.json",
    ]
    catalogs = [
        catalog_skills(codex_home / "skills", "codex-user", include_catalog_entries),
        catalog_skills(
            codex_home / "plugins/cache", "codex-plugin-cache", include_catalog_entries
        ),
        catalog_skills(home / ".agents/skills", "agents-user", include_catalog_entries),
        catalog_skills(home / ".claude/skills", "claude-user", include_catalog_entries),
        catalog_skills(home / ".cursor/skills", "cursor-user", include_catalog_entries),
    ]
    return {
        "codex_home": str(codex_home),
        "config_files": {
            str(path): path.is_file() for path in config_candidates
        },
        "skill_catalogs": catalogs,
    }


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("workspace", type=Path)
    parser.add_argument(
        "--full-catalogs",
        action="store_true",
        help="inclui caminhos de todas as skills encontradas nos catálogos",
    )
    args = parser.parse_args()

    root = args.workspace.expanduser().resolve()
    home = Path.home().resolve()
    if not root.is_dir():
        parser.error(f"workspace inexistente: {root}")
    if root == Path(root.anchor) or root == home:
        parser.error("use a pasta específica do projeto, não uma raiz ampla")

    report = {
        "workspace": str(root),
        "environment": {
            "os": platform.system(),
            "release": platform.release(),
            "architecture": platform.machine(),
            "shell": os.environ.get("SHELL") or os.environ.get("COMSPEC") or "",
        },
        "files": {name: (root / name).exists() for name in PROJECT_FILES},
        "lockfiles": [name for name in LOCKFILES if (root / name).exists()],
        "directories": {
            ".agent": (root / ".agent").is_dir(),
            ".agents": (root / ".agents").is_dir(),
            ".git": (root / ".git").exists(),
            "memory": (root / ".agent/memory").is_dir(),
        },
        "executables": {
            name: executable_state(name, command)
            for name, command in VERSION_COMMANDS.items()
        },
        "git": git_state(root),
        "skills": skill_names(root),
        "client_scope": client_scope(args.full_catalogs),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
