import unittest
from pathlib import Path
import subprocess
import sys


class TestHelloOutput(unittest.TestCase):
    def test_hello_output(self):
        current_file = Path(__file__).resolve()
        repo_root = next(parent for parent in current_file.parents if (parent / "README.md").exists())
        script_path = repo_root / "starter-tasks" / "task-03-hello-script" / "hello.py"
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(result.stdout.strip(), "Hello GitHub Tutorial")
