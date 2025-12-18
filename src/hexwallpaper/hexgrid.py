import math

class HexGrid:
    def __init__(self, img_width, img_height, hex_size):
        self.img_width = img_width
        self.img_height = img_height
        self.hex_size = hex_size
        self.width_step = hex_size * 3**0.5
        self.height_step = hex_size * 1.5

    def iter_centers(self):
        """Yield center coordinates of hexagons covering the image."""
        y = 0
        row = 0

        while y < self.img_height:
            x_offset = (self.width_step / 2) if row % 2 else 0
            x = x_offset

            while x < self.img_width:
                yield (x, y)
                x += self.width_step

            y += self.height_step
            row += 1

    def polygon(self, cx, cy):
        """Return 6-vertex polygon for the hexagon centered at (cx,cy)."""
        points = []
        for i in range(6):
            angle = math.pi / 180 * (60 * i + 30)
            px = cx + self.hex_size * math.cos(angle)
            py = cy + self.hex_size * math.sin(angle)
            points.append((px, py))
        return points
