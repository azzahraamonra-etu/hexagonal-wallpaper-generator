from hexgrid import HexGrid
from generator import WallpaperGenerator
from svgwriter import svg_wrap, write_svg

INPUT = "wallpapers/input.png"
OUTPUT = "wallpapers/output.svg"
HEX_SIZE = 20  # configure!

def main():
    # Prepare grid
    from PIL import Image
    img = Image.open(INPUT)
    grid = HexGrid(img.width, img.height, HEX_SIZE)

    # Generate wallpaper
    generator = WallpaperGenerator(INPUT, grid)
    elements = list(generator.generate_hex_svg_elements())

    # Write SVG
    svg_code = svg_wrap(img.width, img.height, elements)
    write_svg(OUTPUT, svg_code)
    print(f"Generated {OUTPUT}")

if __name__ == "__main__":
    main()
