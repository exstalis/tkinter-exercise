# Arslan Elif Ece
# A 50
# Assignment 8

import math
from tkinter import *
import tkinter
from EquilateralTriangle import *
from IsoscelesTriangle import *
from ScaleneTriangle import *

class CalculateTriangles:
    def __init__(self):
        self.__main_window = tkinter.Tk()
        self.__top = Frame(self.__main_window)
        self.__mid = Frame(self.__main_window)
        self.__bottom = Frame(self.__main_window)
        self.__last = Frame(self.__main_window)

        self.__prompt1 = Label(self.__top, text = "Equilateral : Side A")

        self.__sideOfEq = DoubleVar()
        self.__sideEntryofEq = Entry(self.__top,textvariable = self.__sideOfEq,
                                     width=5)
        


        self.__buttonTop = Button(self.__top, text="Get", \
                                  command=self.__equilTriangleMethod)

        self.__area1Var = DoubleVar()
        self.__perimeter1Var = DoubleVar()
        self.__angleA1Var = DoubleVar()
        self.__angleB1Var = DoubleVar()
        self.__angleC1Var = DoubleVar()

        self.__label00 = Label(self.__top, text ="Area:")
        self.__area1Entry = Entry(self.__top, textvariable = self.__area1Var, width=3)

        self.__label01 = Label(self.__top, text ="Perimeter:")
        self.__perimeter1Entry = Entry(self.__top, textvariable = self.__perimeter1Var, \
                                       width=3)

        self.__label02 = Label(self.__top, text ="Angle A:")
        self.__angleA1Entry = Entry(self.__top, textvariable = self.__angleA1Var, width=3)

        self.__label03 = Label(self.__top, text ="Angle B:")
        self.__angleB1Entry = Entry(self.__top, textvariable = self.__angleB1Var, width=3)

        self.__label04 = Label(self.__top, text ="Angle C:")
        self.__angleC1Entry = Entry(self.__top, textvariable = self.__angleC1Var, width=3)

        self.__prompt1.pack(side = "left")
        self.__sideEntryofEq.pack(side = "left")
        self.__buttonTop.pack(side = "left")
        self.__label00.pack(side = "left")
        self.__area1Entry.pack(side = "left")
        self.__label01.pack(side = "left")
        self.__perimeter1Entry.pack(side = "left")
        self.__label02.pack(side = "left")
        self.__angleA1Entry.pack(side = "left")
        self.__label03.pack(side = "left")
        self.__angleB1Entry.pack(side = "left")
        self.__label04.pack(side = "left")
        self.__angleC1Entry.pack(side = "left")















        self.__prompt2 = Label(self.__mid, text = "Isosceles : Side A")
        self.__side21Var = DoubleVar()
        self.__side21Entry = Entry(self.__mid, \
                                   textvariable =  self.__side21Var, width=3)
        self.__prompt21 = Label(self.__mid, text = "Side B")
        self.__side22Var = DoubleVar()
        self.__side22Entry = Entry(self.__mid, \
                                   textvariable =  self.__side22Var, width=3)

        self.__buttonMid= Button(self.__mid, text="Get",\
                                        command = self.__isoscelesTriangleMethod)

        self.__area2Var = DoubleVar()
        self.__perimeter2Var = DoubleVar()
        self.__angleA2Var = DoubleVar()
        self.__angleB2Var = DoubleVar()
        self.__angleC2Var = DoubleVar()

        self.__label10 = Label(self.__mid, text ="Area:")
        self.__area2Entry = Entry(self.__mid, \
                                  textvariable = self.__area2Var, width=3)

        self.__label11 = Label(self.__mid, text ="Perimeter:")
        self.__perimeter2Entry = Entry(self.__mid, \
                                       textvariable = self.__perimeter2Var, \
                                       width=3)

        self.__label12 = Label(self.__mid, text ="Angle A:")
        self.__angleA2Entry = Entry(self.__mid, \
                                    textvariable = self.__angleA2Var, width=3)

        self.__label13 = Label(self.__mid, text ="Angle B:")
        self.__angleB2Entry = Entry(self.__mid, \
                                    textvariable = self.__angleB2Var, width=3)

        self.__label14 = Label(self.__mid, text ="Angle C:")
        self.__angleC2Entry = Entry(self.__mid,\
                                    textvariable = self.__angleC2Var, width=3)

        self.__prompt2.pack(side = "left")
        self.__side21Entry.pack(side = "left")
        self.__prompt21.pack(side = "left")
        self.__side22Entry.pack(side = "left")
        self.__buttonMid.pack(side = "left")
        self.__label10.pack(side = "left")
        self.__area2Entry.pack(side = "left")
        self.__label11.pack(side = "left")
        self.__perimeter2Entry.pack(side = "left")
        self.__label12.pack(side = "left")
        self.__angleA2Entry.pack(side = "left")
        self.__label13.pack(side = "left")
        self.__angleB2Entry.pack(side = "left")
        self.__label14.pack(side = "left")
        self.__angleC2Entry.pack(side = "left")












        self.__prompt3 = Label(self.__bottom, text = "Isosceles : Side A")
        self.__side31Var = DoubleVar()
        self.__side31Entry = Entry(self.__bottom, \
                                   textvariable = self.__side31Var, width=3)

        self.__prompt31 = Label(self.__bottom, text = "Side B")
        self.__side32Var = DoubleVar()
        self.__side32Entry = Entry(self.__bottom, \
                                   textvariable = self.__side32Var, width=3)

        self.__prompt32 = Label(self.__bottom, text = "Side C")
        self.__side33Var = DoubleVar()
        self.__side33Entry = Entry(self.__bottom, \
                                   textvariable = self.__side33Var, width=3)

        self.__buttonBottom= Button(self.__bottom, text="Get",\
                                       command = self.__scaleneTriangleMethod)

        self.__area3Var = DoubleVar()
        self.__perimeter3Var = DoubleVar()
        self.__angleA3Var = DoubleVar()
        self.__angleB3Var = DoubleVar()
        self.__angleC3Var = DoubleVar()

        self.__label20 = Label(self.__bottom, text ="Area:")
        self.__area3Entry = Entry(self.__bottom, \
                                  textvariable = self.__area3Var, width=3)

        self.__label21 = Label(self.__bottom, text ="Perimeter:")
        self.__perimeter3Entry = Entry(self.__bottom, \
                                       textvariable = self.__perimeter3Var, \
                                       width=3)

        self.__label22 = Label(self.__bottom, text ="Angle A:")
        self.__angleA3Entry = Entry(self.__bottom, \
                                    textvariable = self.__angleA3Var, width=3)

        self.__label23 = Label(self.__bottom, text ="Angle B:")
        self.__angleB3Entry = Entry(self.__bottom, \
                                    textvariable = self.__angleB3Var, width=3)

        self.__label24 = Label(self.__bottom, text ="Angle C:")
        self.__angleC3Entry = Entry(self.__bottom,\
                                     textvariable = self.__angleC3Var, width=3)

        self.__prompt3.pack(side = "left")
        self.__side31Entry.pack(side = "left")
        self.__prompt31.pack(side = "left")
        self.__side32Entry.pack(side = "left")
        self.__prompt32.pack(side = "left")
        self.__side33Entry.pack(side = "left")
        self.__buttonBottom.pack(side = "left")
        self.__label20.pack(side = "left")
        self.__area3Entry.pack(side = "left")
        self.__label21.pack(side = "left")
        self.__perimeter3Entry.pack(side = "left")
        self.__label22.pack(side = "left")
        self.__angleA3Entry.pack(side = "left")
        self.__label23.pack(side = "left")
        self.__angleB3Entry.pack(side = "left")
        self.__label24.pack(side = "left")
        self.__angleC3Entry.pack(side = "left")


        self.__buttonGet = Button(self.__last, text="Get All", \
                                  command=self.__getAll)

        self.__buttonGet.pack(side = "left")
        self.__buttonClear = Button(self.__last, text="Clear All", \
                                  command=self.__clearAll)

        self.__buttonClear.pack(side = "left")

        
        self.__top.pack()
        self.__mid.pack()
        self.__bottom.pack()
        self.__last.pack()
        tkinter.mainloop()

    def __equilTriangleMethod(self):
        self.__equilTriangle = EquilateralTriangle(self.__sideOfEq.get())
        self.__angleA1Var.set(self.__equilTriangle.getAngle())
        self.__angleB1Var.set(self.__equilTriangle.getAngle())
        self.__angleC1Var.set(self.__equilTriangle.getAngle())
        self.__area1Var.set(self.__equilTriangle.area())
        self.__perimeter1Var.set(self.__equilTriangle.perimeter())

    def __isoscelesTriangleMethod(self):
        self.__isoscelesTriangle = IsoscelesTriangle(self.__side21Var.get(),
                                                     self.__side22Var.get())
        self.__angleA2Var.set(self.__isoscelesTriangle.angleA())
        self.__angleB2Var.set(self.__isoscelesTriangle.angleB())
        self.__angleC2Var.set(self.__isoscelesTriangle.angleC())
        
        self.__perimeter2Var.set(self.__isoscelesTriangle.perimeter())
        self.__area2Var.set(self.__isoscelesTriangle.area())
        
    def __scaleneTriangleMethod(self):
        self.__scaleneTriangle = ScaleneTriangle(self.__side31Var.get(),
                                                     self.__side32Var.get(),
                                                    self.__side33Var.get())
        self.__angleA3Var.set(self.__scaleneTriangle.angleA())
        self.__angleB3Var.set(self.__scaleneTriangle.angleB())
        self.__angleC3Var.set(self.__scaleneTriangle.angleC())
        self.__perimeter3Var.set(self.__scaleneTriangle.perimeter())
        self.__area3Var.set(self.__scaleneTriangle.area())
        
    def __getAll(self):
        self.__equilTriangleMethod()
        self.__scaleneTriangleMethod()
        self.__isoscelesTriangleMethod()

    def __clearAll(self):
        self.__sideEntryofEq.delete(0,last=END)
        self.__angleA1Entry.delete(0,last=END)
        self.__angleA2Entry.delete(0,last=END)
        self.__angleA3Entry.delete(0,last=END)
        self.__angleB1Entry.delete(0,last=END)
        self.__angleB2Entry.delete(0,last=END)
        self.__angleB3Entry.delete(0,last=END)
        self.__angleC1Entry.delete(0,last=END)
        self.__angleC2Entry.delete(0,last=END)
        self.__angleC3Entry.delete(0,last=END)
        self.__area1Entry.delete(0,last=END)
        self.__area2Entry.delete(0,last=END)
        self.__area3Entry.delete(0,last=END)
        self.__perimeter3Entry.delete(0,last=END)
        self.__perimeter2Entry.delete(0,last=END)
        self.__perimeter1Entry.delete(0,last=END)
        self.__side21Entry.delete(0,last=END)
        self.__side22Entry.delete(0,last=END)
        self.__side31Entry.delete(0,last=END)
        self.__side32Entry.delete(0,last=END)
        self.__side33Entry.delete(0,last=END)


