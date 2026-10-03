"""
Collection of panel classes for displaying data.

Each panel class represents a widget in the dashboard. They are responsible for rendering
their own content and updating their state.
"""

import curses

class BasePanel:
    """Base class for all panels."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def render(self, screen):
        """Render the panel content on the given screen."""
        pass
    
    def update(self, data):
        """Update the panel state with new data."""
        pass

class SequencePanel(BasePanel):
    """Panel for displaying a DNA/RNA sequence."""
    
    def __init__(self, width, height):
        super().__init__(width, height)
        self.sequence = ""
    
    def render(self, screen):
        y, x = 0, 0
        for char in self.sequence:
            screen.addch(y, x, char)
            x += 1
            if x >= self.width:
                x = 0
                y += 1
    
    def update(self, data):
        self.sequence = data["sequence"]

class SparklinePanel(BasePanel):
    """Panel for displaying a sparkline."""
    
    def __init__(self, width, height):
        super().__init__(width, height)
        self.data = []
    
    def render(self, screen):
        y, x = 0, 0
        for value in self.data:
            screen.addch(y, x, "*")
            x += 1
            if x >= self.width:
                x = 0
                y += 1
    
    def update(self, data):
        self.data = data["values"]
