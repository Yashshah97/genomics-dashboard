import unittest
from genomics_dashboard import ui_helpers

class TestUIHelpers(unittest.TestCase):

    def setUp(self):
        self.stdscr = object() # Mock the stdscr object
        self.panel = ui_helpers.create_panel(self.stdscr, 0, 0, 10, 20)

    def test_create_panel(self):
        panel = ui_helpers.create_panel(self.stdscr, 1, 2, 3, 4)
        self.assertIsInstance(panel, curses.window)

    def test_update_panel(self):
        ui_helpers.update_panel(self.panel, "Hello World!")
        self.assertEqual(self.panel.instr(0, 0), b"Hello World!")

    def test_get_panel_height(self):
        self.assertEqual(ui_helpers.get_panel_height(self.panel), 10)

    def test_get_panel_width(self):
        self.assertEqual(ui_helpers.get_panel_width(self.panel), 20)

if __name__ == '__main__':
    unittest.main()
