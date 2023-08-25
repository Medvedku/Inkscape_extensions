#!/usr/bin/env python
# coding=utf-8

import random
import inkex

class CreateCircle(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.arg_parser.add_argument(
            "-w",
            "--width",
            action="store",
            type=float,
            dest="width",
            default=100,
            help="Width of the circle",
        )
        self.arg_parser.add_argument(
            "--height",
            action="store",
            type=float,
            dest="height",
            default=100,
            help="Height of the circle",
        )
        self.arg_parser.add_argument(
            "-n",
            "--number",
            action="store",
            type=int,
            dest="number",
            default=1,
            help="Number of circles to create",
        )
        self.arg_parser.add_argument(
            "--boundary_width",
            action="store",
            type=float,
            dest="boundary_width",
            help="Boundary width in mm",
        )
        self.arg_parser.add_argument(
            "--boundary_height",
            action="store",
            type=float,
            dest="boundary_height",
            help="Boundary height in mm",
        )

    def effect(self):
        width = self.options.width
        height = self.options.height
        number_of_circles = self.options.number
        boundary_width_mm = self.options.boundary_width
        boundary_height_mm = self.options.boundary_height

        # Convert boundary dimensions from mm to internal units
        boundary_width = self.svg.unittouu(f"{boundary_width_mm}mm")
        boundary_height = self.svg.unittouu(f"{boundary_height_mm}mm")

        # Create a grid size based on the number of circles
        grid_size = int(number_of_circles ** 0.5)

        # Calculate cell dimensions
        cell_width = boundary_width / grid_size
        cell_height = boundary_height / grid_size

        for i in range(number_of_circles):
            row = i // grid_size
            col = i % grid_size

            # Calculate random x and y within the cell
            x = random.uniform(col * cell_width, (col + 1) * cell_width - width)
            y = random.uniform(row * cell_height, (row + 1) * cell_height - height)

            # Create a circle element
            circle = inkex.Circle(cx=str(x), cy=str(y), r=str(min(width, height) / 2))

            # Add the circle to the root of the document
            self.svg.get_current_layer().add(circle)

if __name__ == "__main__":
    CreateCircle().run()