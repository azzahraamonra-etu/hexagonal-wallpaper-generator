def svg_wrap(width, height, elements):
    content = "\n".join(elements)
    return f"""<svg xmlns="http://www.w3.org/2000/svg"
         width="{width}" height="{height}"
         viewBox="0 0 {width} {height}">
{content}
</svg>
"""

def write_svg(path, svg_code):
    with open(path, "w") as f:
        f.write(svg_code)
