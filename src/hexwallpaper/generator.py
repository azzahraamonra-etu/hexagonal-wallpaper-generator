from PIL import Image
import numpy as np

class WallpaperGenerator:
    def __init__(self, input_path, hex_grid):
        self.input_path = input_path
        self.hex_grid = hex_grid
        # Load image and ensure it's RGB
        self.image = Image.open(input_path).convert("RGB")
    
    def sample_color(self, cx, cy):
        """
        Return average RGB color for the area around cx, cy.
        """
        r = self.hex_grid.hex_size
        # Define a small sampling box around the center
        left = int(max(0, cx - r/2))
        top = int(max(0, cy - r/2))
        right = int(min(self.image.width, cx + r/2))
        bottom = int(min(self.image.height, cy + r/2))

        region = self.image.crop((left, top, right, bottom))
        data = np.array(region)
        
        if data.size == 0:
            return (0, 0, 0)
            
        average_color = np.mean(data, axis=(0, 1))
        return tuple(average_color.astype(int))

    def generate_hex_svg_elements(self):
        """
        This is the method main.py was looking for!
        It loops through the grid and builds the SVG shapes.
        """
        for cx, cy in self.hex_grid.iter_centers():
            # Get the 6 points of the hexagon
            vertices = self.hex_grid.polygon(cx, cy)
            points_str = " ".join([f"{x:.2f},{y:.2f}" for x, y in vertices])
            
            # Get the color for this specific hexagon
            rgb = self.sample_color(cx, cy)
            hex_color = "#{:02x}{:02x}{:02x}".format(*rgb)
            
            # Yield the XML string for this hexagon
            yield f'<polygon points="{points_str}" fill="{hex_color}" stroke="{hex_color}" stroke-width="1"/>'