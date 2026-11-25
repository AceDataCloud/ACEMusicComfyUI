import importlib.util
from pathlib import Path
import sys
from unittest import TestCase
from unittest.mock import patch


class HostTests(TestCase):
    def test_graph_load_and_same_task_refresh(self):
        source = Path(__file__).resolve().parents[1] / "__init__.py"
        spec = importlib.util.spec_from_file_location("ace_music_nodes", source)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        spec.loader.exec_module(module)
        self.assertEqual(len(module.NODE_CLASS_MAPPINGS), 9)
        query = module.NODE_CLASS_MAPPINGS["AceMusicRetrieve"]
        self.assertIn("task_id", query.INPUT_TYPES()["required"])
        with patch(
            "ace_music_nodes.nodes.invoke",
            return_value={"id": "saved", "state": "pending"},
        ) as invoke:
            output = query().run(task_id="saved")
            self.assertEqual(output["result"][0], "saved")
            self.assertEqual(
                invoke.call_args.args[1:], ("retrieve", {"task_id": "saved"})
            )
