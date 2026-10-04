"""
Unit tests for core application logic.

This module contains unit tests for the core functionality of the Genomics TUI Dashboard.
"""

import unittest
from io import StringIO
import sys

class TestCore(unittest.TestCase):

    def test_empty_sequence(self):
        """Test that an empty sequence returns None."""
        from genomics_dashboard.core import analyze_sequence
        self.assertIsNone(analyze_sequence(''))

    def test_valid_sequence(self):
        """Test that a valid sequence returns the correct analysis results."""
        from genomics_dashboard.core import analyze_sequence
        result = analyze_sequence('ATCG')
        self.assertIsNotNone(result)
        self.assertEqual(len(result['sparklines']), 4)

    def test_invalid_sequence(self):
        """Test that an invalid sequence raises a ValueError."""
        from genomics_dashboard.core import analyze_sequence
        with self.assertRaises(ValueError):
            analyze_sequence('ABC')

class TestCoreOutput(unittest.TestCase):

    def setUp(self):
        self.out = StringIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_empty_sequence_output(self):
        """Test that an empty sequence returns the correct output."""
        from genomics_dashboard.core import display_results
        display_results({}, self.out)
        self.assertEqual(self.out.getvalue(), '')

    def test_valid_sequence_output(self):
        """Test that a valid sequence returns the correct output."""
        from genomics_dashboard.core import display_results
        result = {'sparklines': [1, 2, 3, 4]}
        display_results(result, self.out)
        self.assertEqual(self.out.getvalue(), 'Sparkline 1: \u2588\u2588\u2588\u2588\n'
                                            'Sparkline 2: \u2588\u2588\u2588\u2588\n'
                                            'Sparkline 3: \u2588\u2588\u2588\u2588\n'
                                            'Sparkline 4: \u2588\u2588\u2588\u2588\n')

if __name__ == '__main__':
    unittest.main()
