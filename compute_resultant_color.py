#!/usr/bin/env python

import inkex
from inkex.colors import Color
from colorsys import rgb_to_hls, hls_to_rgb

def blend_with_black(color, alpha):
    return [c * alpha + (1 - alpha) * 0 for c in color]

class ComputeResultantColor(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.arg_parser.add_argument(
            "-o",
            "--opacity",
            action="store",
            type=int,
            dest="opacity",
            default=100,
            help="Opacity level to blend with black (%)",
        )

    def effect(self):
        opacity = self.options.opacity / 100.0  # Convert to float
        for element in self.svg.selection.filter(inkex.PathElement).values():
            current_color = element.style.get('fill')
            if current_color:
                color = Color(current_color).to_rgb()
                color = [c / 255.0 for c in color]  # Normalize to [0, 1]
                new_color = blend_with_black(color, opacity)
                new_color_hex = "#{:02x}{:02x}{:02x}".format(
                    int(new_color[0] * 255),
                    int(new_color[1] * 255),
                    int(new_color[2] * 255)
                )
                element.style['fill'] = new_color_hex

if __name__ == "__main__":
    ComputeResultantColor().run()
