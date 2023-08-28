#!/usr/bin/env python

import inkex
from colorsys import rgb_to_hls, hls_to_rgb

class ChangeLightness(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.arg_parser.add_argument(
            "-l",
            "--lightness",
            action="store",
            type=float,
            dest="lightness",
            default=0,
            help="Lightness level change for fill color",
        )

    def effect(self):
        lightness_change = self.options.lightness / 100.0

        for element in self.svg.selection.values():
            style = element.style
            fill_color = style.get('fill')
            if fill_color and fill_color.startswith('#'):
                r, g, b = int(fill_color[1:3], 16), int(fill_color[3:5], 16), int(fill_color[5:7], 16)
                h, l, s = rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
                l += lightness_change
                l = max(0, min(l, 1)) # Clamp to [0, 1]
                r, g, b = hls_to_rgb(h, l, s)
                new_color = f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"
                style['fill'] = new_color
                element.style = style

if __name__ == "__main__":
    ChangeLightness().run()
