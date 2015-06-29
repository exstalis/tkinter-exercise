#  Arslan Elif Ece
# A 50
# Assignment 8

from Triangle import*


class ScaleneTriangle(Triangle):
    def __init__(self, a=None, b=None, c=None):
        Triangle.__init__(self, a, b, c)
        self.__a = self.setSideA(a)
        self.__b = self.setSideB(b)
        self.__c = self.setSideC(c)
        self.__perimeter = Triangle.perimeter(self)
        self.__sides = list()
        self.__aa = Triangle.angleA(self)
        self.__ab = Triangle.angleB(self)
        self.__ac = Triangle.angleC(self)

    def area(self):
        return Triangle.area(self)

    def perimeter(self):
        return self.__perimeter










