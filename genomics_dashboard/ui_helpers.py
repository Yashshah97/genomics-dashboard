"""
Utility functions for curses UI manipulation.

This module provides helper functions for working with the curses library,
specifically for creating and updating panels and text in a TUI dashboard.
"""

import curses

def create_panel(stdscr, y, x, height, width):
    """
    Create a new panel at the specified position on the screen.

    :param stdscr: The main window of the curses application
    :param y: The row where the panel will be drawn (top-left corner)
    :param x: The column where the panel will be drawn (top-left corner)
    :param height: The height of the panel in rows
    :param width: The width of the panel in columns
    """
    return curses.newwin(height, width, y, x)

def update_panel(panel, text):
    """
    Update the contents of a panel with new text.

    :param panel: The panel to be updated
    :param text: The new text to display in the panel
    """
    panel.clear()
    panel.addstr(0, 0, text)
    panel.refresh()

def get_panel_height(panel):
    """
    Get the height of a panel in rows.

    :param panel: The panel whose height is requested
    :return: The height of the panel in rows
    """
    return panel.getmaxyx()[0]

def get_panel_width(panel):
    """
    Get the width of a panel in columns.

    :param panel: The panel whose width is requested
    :return: The width of the panel in columns
    """
    return panel.getmaxyx()[1]
