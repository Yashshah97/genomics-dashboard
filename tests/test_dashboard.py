"""Smoke tests for dashboard."""
import unittest

from genomics_dashboard import dashboard


class TestModule(unittest.TestCase):
    def test_module_loads(self):
        self.assertTrue(hasattr(dashboard, '__doc__'))

    def test_public_api_exists(self):
        public = [n for n in dir(dashboard) if not n.startswith('_')]
        self.assertTrue(public)


if __name__ == "__main__":
    unittest.main()
