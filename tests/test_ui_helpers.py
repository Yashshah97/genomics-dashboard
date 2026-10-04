"""Smoke tests for ui_helpers."""
import unittest

from genomics_dashboard import ui_helpers


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(ui_helpers, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(ui_helpers) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
