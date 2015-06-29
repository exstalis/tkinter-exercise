#  Arslan Elif Ece
# A 50
# Assignment 8


from Triangle import*
from math import *
class EquilateralTriangle(Triangle):
    def __init__(self, side=None):
        Triangle().__init__(a=None, b=None, c=None)
        self.__angle = 60
        self.__side = side
        self.__area = 0.0
        self.setSideA(self.__side)
        self.setSideB(self.__side)
        self.setSideC(self.__side)
        self.__perimeter = 3*self.__side
    
   
    def getSide(self):
        return self.__side
    
 
    def setAngle(self, angles=60):
        self.__angle = 60
    
  
    def getAngle(self):
        return self.__angle

    def perimeter(self):
        return self.__perimeter

    def area(self):
        self.__area = 0.25*sqrt(3)*self.__side**2
        return self.__area





