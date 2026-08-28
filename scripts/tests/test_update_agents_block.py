from __future__ import annotations

# Feito por: https://github.com/GabrielPazBR/

import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "update_agents_block.py"
SPEC = importlib.util.spec_from_file_location("update_agents_block", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


BLOCK = f"{MODULE.START}\n## Base\nConteúdo\n{MODULE.END}\n"


class UpdateAgentsBlockTests(unittest.TestCase):
    def test_merge_preserves_existing_content(self) -> None:
        existing = "# Projeto\n\nInstrução existente.\n"

        merged = MODULE.merge(existing, BLOCK)

        self.assertIn("Instrução existente.", merged)
        self.assertEqual(MODULE.unmanaged_hash(existing), MODULE.unmanaged_hash(merged))

    def test_merge_updates_only_managed_block(self) -> None:
        existing = (
            "# Projeto\n\n"
            f"{MODULE.START}\nAntigo\n{MODULE.END}\n\n"
            "Rodapé\n"
        )

        merged = MODULE.merge(existing, BLOCK)

        self.assertNotIn("Antigo", merged)
        self.assertIn("Rodapé", merged)
        self.assertEqual(MODULE.unmanaged_hash(existing), MODULE.unmanaged_hash(merged))

    def test_placeholders_are_rejected(self) -> None:
        block = f"{MODULE.START}\n__VALUE__\n{MODULE.END}\n"

        with self.assertRaisesRegex(ValueError, "placeholders"):
            MODULE.merge("", block)

    def test_main_writes_baseline_and_agents(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            block_path = root / "block.md"
            block_path.write_text(BLOCK, encoding="utf-8")
            original = "# Existente\n"
            (root / "AGENTS.md").write_text(original, encoding="utf-8")

            import sys
            from unittest.mock import patch

            with patch.object(sys, "argv", [str(SCRIPT), str(root), str(block_path)]):
                code = MODULE.main()

            self.assertEqual(code, 0)
            self.assertIn("# Existente", (root / "AGENTS.md").read_text(encoding="utf-8"))
            baseline = (root / ".agent/agents-unmanaged.sha256").read_text(
                encoding="utf-8"
            ).strip()
            self.assertEqual(baseline, MODULE.unmanaged_hash(original))


if __name__ == "__main__":
    unittest.main()
