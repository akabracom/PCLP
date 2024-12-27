from lab_python_oop.geometric_figure import GeometricFigure
from lab_python_oop.color import FigureColor

class Rectangle(GeometricFigure):
    figure_name = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "{} {} цвета шириной {} и высотой {} с площадью {:.2f}".format(
            self.figure_name,
            self.color.color,
            self.width,
            self.height,
            self.area()
        )
