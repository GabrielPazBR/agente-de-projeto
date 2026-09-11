from __future__ import annotations

# Feito por: https://github.com/GabrielPazBR/

import importlib.util
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).parents[1] / "validate_project_setup.py"
SPEC = importlib.util.spec_from_file_location("validate_project_setup", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ValidateProjectSetupTests(unittest.TestCase):
    def run_validator(self, root: Path) -> tuple[int, str]:
        output = io.StringIO()
        with (
            patch.object(sys, "argv", [str(SCRIPT), str(root)]),
            patch.object(MODULE.shutil, "which", return_value="/fake/tool"),
            redirect_stdout(output),
        ):
            code = MODULE.main()
        return code, output.getvalue()

    def test_complete_workspace_passes(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            instructions = root / ".agent/instructions"
            instructions.mkdir(parents=True)
            (root / ".agent/memory").mkdir()
            (root / ".agents/skills/graphify").mkdir(parents=True)
            (root / "graphify-out").mkdir()
            agents_content = (
                    f"{MODULE.START}\n"
                    ".agent/profile.yaml\n"
                    ".agent/manifest.yaml\n"
                    ".agent/instructions/gemini.md\n"
                    ".agent/instructions/linguagem-usuario.md\n"
                    "mempalace instructions mine\n"
                    "Graphify\n"
                    "$graphify . --update\n"
                    "RTK\n"
                    f"{MODULE.END}\n"
            )
            (root / "AGENTS.md").write_text(agents_content, encoding="utf-8")
            (root / ".agent/agents-unmanaged.sha256").write_text(
                MODULE.unmanaged_agents_hash(agents_content) + "\n", encoding="utf-8"
            )
            (root / ".agent/manifest.yaml").write_text(
                'bootstrap:\n  status: "complete"\n', encoding="utf-8"
            )
            (root / ".agent/profile.yaml").write_text(
                "confirmed_by_user: true\n", encoding="utf-8"
            )
            (root / ".agent/skill-sources.lock.yaml").write_text(
                "schema_version: 1\nskills: []\n", encoding="utf-8"
            )
            (instructions / "gemini.md").write_text("# Gemini\n", encoding="utf-8")
            (instructions / "linguagem-usuario.md").write_text(
                "# Linguagem\n", encoding="utf-8"
            )
            (root / ".agents/skills/graphify/SKILL.md").write_text(
                "---\nname: graphify\ndescription: Grafo do código.\n---\n",
                encoding="utf-8",
            )
            (root / "graphify-out/graph.json").write_text(
                "{}\n", encoding="utf-8"
            )

            code, output = self.run_validator(root)

            self.assertEqual(code, 0, output)
            self.assertIn('"passed": true', output)

    def test_incomplete_workspace_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            code, output = self.run_validator(Path(temp))

            self.assertEqual(code, 1, output)
            self.assertIn('"passed": false', output)

    def test_agents_placeholder_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "AGENTS.md").write_text(
                f"{MODULE.START}\n__ACTIVE_CAPABILITIES__\n{MODULE.END}\n",
                encoding="utf-8",
            )

            code, output = self.run_validator(root)

            self.assertEqual(code, 1, output)
            self.assertIn("placeholders não preenchidos em AGENTS.md", output)

    def test_component_complete_does_not_complete_bootstrap(self) -> None:
        content = (
            'bootstrap:\n  status: "in_progress"\n'
            'components:\n  rtk:\n    status: "complete"\n'
        )

        value = MODULE.top_level_mapping_value(content, "bootstrap", "status")

        self.assertEqual(value, "in_progress")

    def test_modified_unmanaged_agents_content_fails(self) -> None:
        original = f"Instrução existente\n{MODULE.START}\nBase\n{MODULE.END}\n"
        modified = f"Conteúdo apagado\n{MODULE.START}\nBase\n{MODULE.END}\n"

        self.assertNotEqual(
            MODULE.unmanaged_agents_hash(original),
            MODULE.unmanaged_agents_hash(modified),
        )


if __name__ == "__main__":
    unittest.main()
