import unittest
from genomics_dashboard import panels

class TestPanels(unittest.TestCase):

    def test_base_panel_init(self):
        panel = panels.BasePanel(10, 20)
        self.assertEqual(panel.width, 10)
        self.assertEqual(panel.height, 20)

    def test_sequence_panel_render(self):
        panel = panels.SequencePanel(10, 20)
        screen = object()  # Mock screen object
        panel.sequence = "ATCG"
        panel.render(screen)

    def test_sparkline_panel_update(self):
        panel = panels.SparklinePanel(10, 20)
        data = {"values": [1, 2, 3]}
        panel.update(data)
        self.assertEqual(panel.data, [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
