# Arslan Elif Ece
# A 50
# Assignment 8

from Triangle import*
import math

class IsoscelesTriangle(Triangle):
    def __init__(self, a=None, b=None):
        Triangle().__init__(self, a, b)
        self.__a = self.setSideA(a)
        self.__b = self.setSideB(b)
        self.__c = self.setSideC(b)

    def perimeter(self):
        self.__sides = [self.getSideA(), self.getSideB(), self.getSideC()]
        return sum(self.__sides)

    def area(self):
        return 0.5*pow(self.__sides[0], 2)*sqrt(pow(self.__sides[1], 2) - 0.25)
    
    
        












