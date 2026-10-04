"""Smoke tests for panels."""
import unittest

from genomics_dashboard import panels


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(panels, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(panels) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
