import math
import sys

class BiquadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def roots(self):
        d = self.discriminant()
        if d >= 0:
            return (-self.b + math.sqrt(d)) / (2 * self.a), (-self.b - math.sqrt(d)) / (2 * self.a)
        else:
            return None


def main():
    if len(sys.argv) == 4:
        a, b, c = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
    else:
        while True:
            try:
                a = float(input("Введите коэффициент A: "))
                b = float(input("Введите коэффициент B: "))
                c = float(input("Введите коэффициент C: "))
                break
            except ValueError:
                print("Некорректный ввод. Введите действительное число.")

    equation = BiquadraticEquation(a, b, c)
    roots = equation.roots()
    if roots is not None:
        print("Корни уравнения:", roots)
    else:
        print("Уравнение не имеет вещественных корней.")


if __name__ == "__main__":
    main()

