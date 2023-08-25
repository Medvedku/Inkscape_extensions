#!/usr/bin/env python

import inkex

class AssignColors(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.arg_parser.add_argument(
            "-t",
            "--threshold",
            action="store",
            type=float,
            dest="threshold",
            default=200,
            help="X-coordinate for color 2",
        )
        self.arg_parser.add_argument(
            "-c1",
            "--color1",
            action="store",
            type=str,
            dest="color1",
            default="#0000FF",
            help="Starting Color (hex)",
        )
        self.arg_parser.add_argument(
            "-c2",
            "--color2",
            action="store",
            type=str,
            dest="color2",
            default="#FF0000",
            help="Ending Color (hex)",
        )

    def effect(self):
        red_x_coordinate = self.options.threshold
        color1 = [int(self.options.color1[i:i + 2], 16) for i in range(1, 6, 2)]
        color2 = [int(self.options.color2[i:i + 2], 16) for i in range(1, 6, 2)]

        for element in self.svg.selection.filter(inkex.PathElement).values():
            bbox = element.bounding_box()
            centroid_x = (bbox.left + bbox.right) / 2

            t = centroid_x / red_x_coordinate # Normalize the x-coordinate
            t = max(0, min(t, 1)) # Clamp to [0, 1]

            # Interpolate color between color1 and color2
            new_color_rgb = [int(c1 * (1 - t) + c2 * t) for c1, c2 in zip(color1, color2)]
            new_color_hex = "#{:02x}{:02x}{:02x}".format(*new_color_rgb)
            element.style['fill'] = new_color_hex

if __name__ == "__main__":
    AssignColors().run()
