from math import pi
from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.color import FigureColor

class Circle(GeometricFigure):
    figure_name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor(color)

    def area(self):
        return pi * (self.radius ** 2)

    def __repr__(self):
        return "{} {} цвета радиусом {} с площадью {:.2f}".format(
            self.figure_name,
            self.color.color,
            self.radius,
            self.area()
        )
