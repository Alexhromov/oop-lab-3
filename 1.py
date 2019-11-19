# 1. Змініть клас Rational із Індивідуального завдання Лабораторної роботи No1 для
# виконання наступних задач:
# • додавання двох раціональних чисел. Результат слід зберігати у скороченому
# вигляді;
# • віднімання двох раціональних чисел. Результат слід зберігати у скороченому
# вигляді;

# • множення двох раціональних чисел. Результат слід зберігати у скороченому
# вигляді;
# • ділення двох раціональних чисел. Результат слід зберігати у скороченому
# вигляді;
# • порівняння двох раціональних чисел.


class Rational:
    """
        Виконання арифметичних операцій з раціональними числами
    """

    def __init__(self, numerator=1, denominator=2):
        from math import gcd
        t = gcd(numerator, denominator)
        if t != 1:
            self.numerator = int(numerator / t)
            self.denominator = int(denominator / t)

        else:
            self.numerator = numerator
            self.denominator = denominator

    def write_rat(self):
        """
            Виведення числа в форматі  a / b
        """
        return str(self.numerator) + '/' + str(self.denominator)

    def write_flot(self):
        """
            Виведення числа в форматі з плаваючою точкой
        """
        return self.numerator / self.denominator

    def __repr__(self):

        return f"{self.numerator} / {self.denominator}"

    def __add__(self, other):

        return Rational(self.numerator * other.denominator + other.numerator*self.denominator, self.denominator*other.denominator)

    def __sub__(self, other):

        return Rational(self.numerator * other.denominator - other.numerator*self.denominator, self.denominator*other.denominator)

    def __mul__(self, other):

        return Rational(self.numerator * other.numerator, self.denominator*other.denominator)

    def __truediv__(self, other):

        return Rational(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):

        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):

        return self.numerator / self.denominator < other.numerator / other.denominator

    def __gt__(self, other):

        return self.numerator / self.denominator > other.numerator / other.denominator


if __name__ == "__main__":
    a = Rational(3, 5)
    b = Rational(4, 3)
    print(a.write_rat())
    print(a.write_flot())
    print(b.write_rat())
    print(b.write_flot())

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a > b)
    print(a < b)
    print(a == b)
