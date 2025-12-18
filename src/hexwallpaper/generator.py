from PIL import Image
import numpy as np

class WallpaperGenerator:
    def __init__(self, input_path, hex_grid):
        self.input_path = input_path
        self.hex_grid = hex_grid
        # TODO: Load image here
    
    def sample_color(self, cx, cy):
        """
        Return average RGB color for the area around cx, cy.
        """
        pass