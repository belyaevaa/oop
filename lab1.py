import sympy as sym
from sympy import *
from abc import ABC, abstractmethod
#считаем правую, левую, центральную производную
#sympy позволяет считать предел
#abc - библиотека базовых абстрактных классов

#Абстрактный класс который не вызывается, а только инициализирует данные
class Abstract(ABC):
    #инициализация данных:
    def __init__(self, function, delta_x, point):
        #инкапсуляция: мы не можем использовать эти переменные вне родительским и дочерним классом
        self._function = function
        self._delta_x = delta_x
        self._point = point
        self._f = lambdify(x, self._function)

    #переопределение print
    def __str__(self):
        return f"f(x) = {self._function}"

    def getFunction(self):
        return self._function

    #полиморфизм: просто объявляем методы
    @abstractmethod
    def right_p(self):
        pass

    @abstractmethod
    def left_p(self):
        pass

    @abstractmethod
    def center_p(self):
        pass

    @abstractmethod
    def diff(self):
        pass
#дочерний класс, наследует от abstcract
#dir - производная справа/слева/по центру
class Calc(Abstract):
    #инициализируем данные из абстрактного класса
    def __init__(self, function, delta_x, point):
        super().__init__(function, delta_x, point)

    def right_p(self):
        # формула правой производной через предел
        return round(sym.limit((self._f(x + self._delta_x) - self._f(x)) / self._delta_x, x, self._point, dir='+'), 5)

    def left_p(self):
        return round(sym.limit((self._f(x + self._delta_x) - self._f(x)) / self._delta_x, x, self._point, dir='-'), 5)

    def center_p(self):
        return round(sym.limit((self._f(x + self._delta_x) - self._f(x)) / self._delta_x, x, self._point, dir='+-'), 5)

    def diff(self):
        return sym.diff(self._function, "x")


if __name__ == '__main__':
    x = symbols('x')
    delta_x = 0.000000001
    function = 1/x + (3*x)**2 + 45
    point = 2
    a = Calc(function, delta_x, point)
    print(a)
    print(f"f'(x) = {a.diff()}")
    print(f"Производная справа {a.right_p()}")
    print(f"Производная слева {a.left_p()}")
    print(f"Производная центральная {a.center_p()}")
