import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SERVER_PATH = Path(__file__).resolve().parents[1] / "server" / "ue_rag_mcp.py"
SPEC = importlib.util.spec_from_file_location("ue_rag_mcp", SERVER_PATH)
SERVER = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = SERVER
SPEC.loader.exec_module(SERVER)


class UeRagMcpTests(unittest.TestCase):
    def setUp(self):
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        (self.root / "Source").mkdir()
        (self.root / "Config").mkdir()
        (self.root / "Docs").mkdir()
        (self.root / "Binaries").mkdir()
        (self.root / "Source" / "CombatComponent.cpp").write_text(
            "class UCombatComponent {}\nvoid UCombatComponent::ApplyCooldown() {}\n",
            encoding="utf-8",
        )
        (self.root / "Config" / "DefaultGameplay.ini").write_text(
            "[/Script/Game.CooldownSettings]\nCooldownTag=Ability.Cooldown\n",
            encoding="utf-8",
        )
        (self.root / "Docs" / "combat.md").write_text("# Cooldown Flow\nCombatComponent owns cooldown state.\n", encoding="utf-8")
        (self.root / "Binaries" / "ignored.cpp").write_text("CooldownShouldNotAppear", encoding="utf-8")
        metadata_directory = self.root / ".ue-rag"
        metadata_directory.mkdir()
        (metadata_directory / "assets.json").write_text(
            json.dumps([{"object_path": "/Game/UI/WBP_Cooldown", "asset_name": "WBP_Cooldown", "class": "WidgetBlueprint"}]),
            encoding="utf-8",
        )

    def tearDown(self):
        self.temporary_directory.cleanup()

    def test_index_search_open_and_status(self):
        indexed = SERVER.rebuild_index(str(self.root))
        self.assertEqual(indexed["scanned_files"], 3)
        self.assertGreaterEqual(indexed["indexed_chunks"], 4)
        rebuilt = SERVER.rebuild_index(str(self.root))
        self.assertEqual(rebuilt["indexed_chunks"], indexed["indexed_chunks"])
        results = SERVER.search_index(str(self.root), "Cooldown", limit=8)
        self.assertGreaterEqual(results["result_count"], 3)
        self.assertNotIn("Binaries/ignored.cpp", [result["path"] for result in results["results"]])
        opened = SERVER.open_result(str(self.root), results["results"][0]["result_id"])
        self.assertIn("content", opened)
        status = SERVER.index_status(str(self.root))
        self.assertTrue(status["ready"])
        self.assertIn("source", status["chunks_by_kind"])
        self.assertIn("asset", status["chunks_by_kind"])


if __name__ == "__main__":
    unittest.main()
