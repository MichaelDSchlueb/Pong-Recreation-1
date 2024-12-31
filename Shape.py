from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, color, cX, cY):

        self.__color = color
        self.__cX = cX
        self.__cY = cY

    @abstractmethod
    def move():
        pass

    def getColor(self):
        return self.__color

    def setColor(self, newColor):
        self.__color = newColor

    def getCenterX(self):
        return self.__cX

    def getCenterY(self):
        return self.__cY

    def setCenterX(self, newVal):
        self.__cX = newVal

    def setCenterY(self, newVal):
        self.__cY = newVal


