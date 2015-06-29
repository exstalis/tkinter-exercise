# Arslan Elif Ece
# A 50
# Assignment 8
from math import *

class Triangle():
    def __init__(self, a=None, b=None, c=None, sides=[]):
        sides = [a, b, c]
        self.__a = a
        self.__b = b
        self.__c = c
        self.__sides = list(sides)
        self.__perimeter = 0.0
        self.__area = 0.0
        self.__angles = list()



    def setSideA(self, a):
        self.__a = a


    def setSideB(self, b):
        self.__b = b


    def setSideC(self, c):
        self.__c = c

    def sides(self, sides):
        self.__sides = sides.copy()
        return self.__sides
    
 
    def getSideA(self):
        return self.__a

    def getSideB(self):
        return self.__b


    def getSideC(self):
        return self.__c

    def perimeter(self):
        for side in self.__sides:
            cmp_sides = sum(self.__sides) - side
            if cmp_sides > side:
                self.__perimeter += side
            else:
                return "cant shape triangle! {}".format(self.__sides)
        return self.__perimeter

    def area(self):
        u = self.__perimeter/2
        self.__area = sqrt(u*(u-self.__a)*(u-self.__b)*(u-self.__c))
        return self.__area

    def angleA(self):
        return degrees(acos((pow(self.__b, 2)+pow(self.__c, 2)-pow(self.__a, 2))/(2*self.__b*self.__c)))

    def angleB(self):
        return degrees(acos((pow(self.__c, 2)+pow(self.__a, 2)-pow(self.__b, 2))/(2*self.__c*self.__a)))

    def angleC(self):
        return degrees(acos((pow(self.__a, 2)+pow(self.__b, 2)-pow(self.__c, 2))/(2*self.__b*self.__a)))

    def getAngles(self):
        self.__angles.append(self.angleA())
        self.__angles.append(self.angleB())
        self.__angles.append(self.angleC())
        return self.__angles
