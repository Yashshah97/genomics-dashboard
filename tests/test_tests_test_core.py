import unittest
from genomics_dashboard import tests_test_core

class TestTestCore(unittest.TestCase):

    def test_import_analyze_sequence(self):
        from genomics_dashboard.core import analyze_sequence
        self.assertIsNotNone(analyze_sequence)

    def test_import_display_results(self):
        from genomics_dashboard.core import display_results
        self.assertIsNotNone(display_results)

if __name__ == '__main__':
    unittest.main()
