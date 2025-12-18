import marimo as mo
from hexwallpaper.hexgrid import HexGrid
from hexwallpaper.generator import WallpaperGenerator
from hexwallpaper.svgwriter import svg_wrap, write_svg
from PIL import Image
import os

app = mo.App()

@app.cell
def _():
    mo.md("# Hex Wallpaper Generator (Marimo)")
    return

@app.cell
def hex_size_slider():
    hex_size = mo.ui.slider(5, 80, 20, label="Hexagon Size")
    hex_size
    return hex_size

@app.cell
def file_selector():
    file = mo.ui.file(label="Upload Input PNG")
    file
    return file

@app.cell
def generate_button(file_selector, hex_size_slider):
    btn = mo.ui.button(label="Generate SVG")
    btn
    return btn

@app.cell
def run_generate(generate_button, file_selector, hex_size_slider):
    if not generate_button.value:
        mo.stop()

    if file_selector.value is None:
        mo.md("**Please upload an input file.**")
        mo.stop()

    filename = file_selector.value.name
    file_selector.value.save(filename)

    img = Image.open(filename)
    grid = HexGrid(img.width, img.height, hex_size_slider.value)
    gen = WallpaperGenerator(filename, grid)
    elements = list(gen.generate_hex_svg_elements())

    svg_code = svg_wrap(img.width, img.height, elements)
    out_path = f"output_{hex_size_slider.value}.svg"
    write_svg(out_path, svg_code)

    mo.md(f"## SVG generated → `{out_path}`")
    mo.md("You can now download the SVG.")
    return out_path

app.run()
