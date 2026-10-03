import unittest
from genomics_dashboard import sparklines

class TestSparklines(unittest.TestCase):

    def test_draw_sparkline_empty_list(self):
        self.assertEqual(sparklines.draw_sparkline([]), "")

    def test_draw_sparkline_single_value(self):
        self.assertEqual(sparklines.draw_sparkline([5]), " ")

    def test_draw_sparkline_multiple_values(self):
        self.assertEqual(sparklines.draw_sparkline([1, 2, 3, 4, 5]), "   ===")

    def test_draw_sparklines_empty_lists(self):
        self.assertEqual(sparklines.draw_sparklines([], [], []), "")

    def test_draw_sparklines_single_value_lists(self):
        self.assertEqual(sparklines.draw_sparklines([1], [2], [3]), "   \n  *\n ===")

if __name__ == '__main__':
    unittest.main()
