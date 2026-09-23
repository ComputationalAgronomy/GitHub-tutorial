import unittest
from pathlib import Path
import subprocess
import sys


class TestHelloOutput(unittest.TestCase):
    def test_hello_output(self):
        starter_tasks_dir = Path(__file__).resolve().parents[1]
        script_path = starter_tasks_dir / "task-03-hello-script" / "hello.py"
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout.strip(), "Hello GitHub Tutorial")
