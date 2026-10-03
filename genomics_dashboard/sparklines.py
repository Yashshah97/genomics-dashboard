"""
Module for displaying sparklines in the Genomics Tui Dashboard.

This module provides a function to generate and display sparklines using ASCII art.
"""

def draw_sparkline(values):
    """
    Draw a sparkline given a list of values.

    Args:
        values (list): A list of numbers representing the data points for the sparkline.

    Returns:
        str: The generated sparkline as an ASCII string.
    """
    if not values:
        return ""

    min_value = min(values)
    max_value = max(values)

    # Calculate the scaling factor to make the line fit within 80 characters
    scale_factor = 80 / (max_value - min_value)

    scaled_values = [(value - min_value) * scale_factor for value in values]

    sparkline = ""
    for i, value in enumerate(scaled_values):
        if i == len(values) // 2:
            sparkline += "*"
        elif value > 10:
            sparkline += "="
        else:
            sparkline += " "

    return sparkline

def draw_sparklines(*values):
    """
    Draw multiple sparklines given a variable number of lists.

    Args:
        *values (list): A variable number of lists representing the data points for each sparkline.

    Returns:
        str: The generated sparklines as an ASCII string.
    """
    return "\n".join(draw_sparkline(values) for values in zip(*values))
