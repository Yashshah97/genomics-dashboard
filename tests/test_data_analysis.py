import unittest
from genomics_dashboard import data_analysis

class TestDataAnalysis(unittest.TestCase):
    def test_count_nucleotides(self):
        sequence = 'ATCG'
        result = data_analysis.count_nucleotides(sequence)
        self.assertEqual(result, {'A': 1, 'C': 1, 'G': 1, 'T': 1})

    def test_calculate_gc_content(self):
        sequence = 'GGGTTT'
        self.assertAlmostEqual(data_analysis.calculate_gc_content(sequence), 100.0)

    def test_calculate_gc_skew(self):
        sequence = 'GGGTTT'
        result = data_analysis.calculate_gc_skew(sequence)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()
