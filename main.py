from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import matplotlib.pyplot as plt


def main():
    N = 10

    rect = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")

    print(rect)
    print(circle)
    print(square)

    # Пример использования внешнего пакета matplotlib
    plt.bar(["Прямоугольник", "Круг", "Квадрат"], [rect.area(), circle.area(), square.area()])
    plt.title("Площади фигур")
    plt.show()

if __name__ == "__main__":
    main()
