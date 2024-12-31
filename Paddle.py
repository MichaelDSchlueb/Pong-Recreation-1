from Shape import Shape
import Constants
from Ball import Ball

class Paddle(Shape):
    def __init__(self, color, cX, cY, width, height):

        super().__init__(color, cX, cY)
        self.__height = height
        self.__width = width
        self.__fifthY = Constants.PADDLE_HEIGHT/Constants.DIVIDER
       

    def move(self, moveKey, width, height):
        centerX = self.getCenterX()
        centerY = self.getCenterY()
        halfHeight = Constants.ONE_QUARTER * Constants.PADDLE_HEIGHT
        if moveKey == 'w' or moveKey == 'i':
            print(centerY)
            if centerY >= Constants.TOP_WALL and centerY <= Constants.BOTTOM_WALL:
                self.setCenterY(centerY - Constants.INCREMENT_VALUE)
            else:
               pass
        if moveKey == 's' or moveKey == 'k':
            print(centerY)
            if centerY >= Constants.TOP_WALL and centerY <= Constants.BOTTOM_WALL:
                self.setCenterY(centerY + Constants.INCREMENT_VALUE)
            else:
                pass
        if moveKey == 'a' or moveKey == 'j':
            print(centerX)
            if centerX >= Constants.LEFT_WALL and centerX <= width:
                self.setCenterX(centerX - Constants.INCREMENT_VALUE)
            else:
               pass
        if moveKey == 'd' or moveKey == 'l':
            print(centerX)
            if centerX >= Constants.LEFT_WALL and centerX <= width:
               self.setCenterX(centerX + Constants.INCREMENT_VALUE)
            else:
                pass

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def setHeight(self, newVal):
        self.__height = newVal

    def collision(self, ball,yhit):
        ball.setXDir(Constants.DIR_CHANGE_RIGHT * ball.getXDir())
        halfHeight = Constants.PADDLE_HEIGHT * Constants.ONE_QUARTER
        if yhit + Constants.PADDLE_HEIGHT >= ball.getCenterY() + halfHeight - Constants.TWO_QUARTERS * self.__fifthY and yhit + Constants.PADDLE_HEIGHT <= self.getCenterY() + halfHeight - Constants.ONE_QUARTER * self.__fifthY:
            ball.setYDir(Constants.UPPER_DIRECTION)
        elif yhit + Constants.PADDLE_HEIGHT >= self.getCenterY() + halfHeight - Constants.ONE_QUARTER * self.__fifthY and yhit + Constants.PADDLE_HEIGHT <= self.getCenterY() + halfHeight - Constants.HALF_OF_ONE_QUARTER * self.__fifthY:
            ball.setYDir(Constants.UP_DIRECTION)
        elif yhit + Constants.PADDLE_HEIGHT >= self.getCenterY() + halfHeight - Constants.HALF_OF_ONE_QUARTER * self.__fifthY and yhit + Constants.PADDLE_HEIGHT <= self.getCenterY() + halfHeight + Constants.HALF_OF_ONE_QUARTER * self.__fifthY:
            ball.setYDir(Constants.STRAIGHT)
        elif yhit + Constants.PADDLE_HEIGHT >= self.getCenterY() + halfHeight + Constants.HALF_OF_ONE_QUARTER * self.__fifthY and yhit + Constants.PADDLE_HEIGHT <= self.getCenterY() + halfHeight + Constants.ONE_QUARTER * self.__fifthY:
            ball.setYDir(Constants.DOWN_DIRECTION)
        elif yhit + Constants.PADDLE_HEIGHT >= self.getCenterY() + halfHeight + Constants.ONE_QUARTER * self.__fifthY and yhit + Constants.PADDLE_HEIGHT <= self.getCenterY() + halfHeight + Constants.TWO_QUARTERS * self.__fifthY:
            ball.setYDir(Constants.DOWNWARDS_DIRECTION)


    def getFifthY(self):
        return self.__fifthY

    def getTopPos(self):
        return self.__topPos

    def setTopPos(self, newVal):
        self.__topPos = newVal

    def getBottomPos(self):
        return self.__bottomPos

    def setBottomPos(self, newVal):
        self.__bottomPos = newVal

     
     


