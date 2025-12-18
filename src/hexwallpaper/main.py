import argparse
import os
from PIL import Image
from hexgrid import HexGrid
from generator import WallpaperGenerator
from svgwriter import svg_wrap, write_svg

def main():
    # 1. Setup CLI arguments
    parser = argparse.ArgumentParser(description="Convert an image to a hexagonal SVG wallpaper.")
    parser.add_argument("input_path", help="Path to the input image file")
    parser.add_argument("--size", type=int, default=20, help="Size of each hexagon (default: 20)")
    parser.add_argument("--output", default="output.svg", help="Path for the output SVG file")
    
    args = parser.parse_args()

    # 2. Validation
    if not os.path.exists(args.input_path):
        print(f"Error: The file '{args.input_path}' was not found.")
        return

    print(f"Processing {args.input_path} with hex size {args.size}...")

    # 3. Load Image & Prepare Grid
    img = Image.open(args.input_path)
    grid = HexGrid(img.width, img.height, args.size)

    # 4. Generate Content
    generator = WallpaperGenerator(args.input_path, grid)
    elements = list(generator.generate_hex_svg_elements())

    # 5. Write Output
    svg_code = svg_wrap(img.width, img.height, elements)
    write_svg(args.output, svg_code)
    print(f"Success! Generated {args.output}")

if __name__ == "__main__":
    main()