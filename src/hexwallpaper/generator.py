import math

def compute_next_coordinate(q, r, hex_size=50):
    """Compute pixel coordinates for a hexagon in axial coordinates (q,r)."""
    x = hex_size * 3/2 * q
    y = hex_size * math.sqrt(3) * (r + q/2)
    return (x, y)
