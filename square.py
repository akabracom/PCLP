from lab_python_oop.rectangle import Rectangle

class Square(Rectangle):
    figure_name = "Квадрат"

    def __init__(self, side, color):
        super().__init__(side, side, color)

    def __repr__(self):
        return "{} {} цвета со стороной {} с площадью {:.2f}".format(
            self.figure_name,
            self.color.color,
            self.width,
            self.area()
        )
