import subprocess
import sys
import unittest
from pathlib import Path


class TestHelloWithName(unittest.TestCase):
    def test_name_input(self):
        script_path = Path(__file__).resolve().parent / "hello_with_name.py"
        result = subprocess.run(
            [sys.executable, str(script_path)],
            input="Taylor\n",
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Hello, Taylor!", result.stdout)

    def test_empty_input(self):
        script_path = Path(__file__).resolve().parent / "hello_with_name.py"
        result = subprocess.run(
            [sys.executable, str(script_path)],
            input="\n",
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertIn("Hello, friend!", result.stdout)
