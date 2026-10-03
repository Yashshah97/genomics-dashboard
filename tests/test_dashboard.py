import unittest
from genomics_dashboard import dashboard

class TestDashboard(unittest.TestCase):
    def test_init_curses(self):
        stdscr = None  # Mock curses.stdscr
        dashboard.GenomicsDashboard().init_curses(stdscr)

    def test_add_panel(self):
        dashboard = dashboard.GenomicsDashboard()
        panel = dashboard.Panel('test')
        dashboard.add_panel('test', panel)
        self.assertIn('test', dashboard.panels)

    def test_draw_dashboard(self):
        stdscr = None  # Mock curses.stdscr
        dashboard = dashboard.GenomicsDashboard()
        dashboard.init_curses(stdscr)
        panel = dashboard.Panel('test')
        sparkline = dashboard.Sparkline('test')
        dashboard.add_panel('test', panel)
        dashboard.add_sparkline('test', sparkline)
        dashboard.draw_dashboard()

    def test_Sparkline_add_value(self):
        sparkline = dashboard.Sparkline('test')
        sparkline.add_value(1)

if __name__ == '__main__':
    unittest.main()
