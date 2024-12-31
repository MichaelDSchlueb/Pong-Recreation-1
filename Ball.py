from Shape import Shape
import Constants

class Ball(Shape):
    def __init__(self, color, cX, cY, radius):

        super().__init__(color, cX, cY)
        self.__radius = radius
        self.__xDir = Constants.START_X
        self.__yDir = Constants.START_Y

    def move(self, width, height, leftPaddle, rightPaddle, score):
        halfPaddleHeight = Constants.ONE_QUARTER * Constants.PADDLE_HEIGHT
        if self.getCenterY() + Constants.PADDLE_HEIGHT <= leftPaddle.getCenterY() + halfPaddleHeight + Constants.TWO_QUARTERS * leftPaddle.getFifthY() and self.getCenterY() + Constants.PADDLE_HEIGHT >= leftPaddle.getCenterY() + halfPaddleHeight - Constants.TWO_QUARTERS * leftPaddle.getFifthY():
          if self.getCenterX() - self.__radius <= leftPaddle.getCenterX() + Constants.PADDLE_WIDTH: 
              leftPaddle.collision(self, self.getCenterY())
        if self.getCenterY() + Constants.PADDLE_HEIGHT <= rightPaddle.getCenterY() + halfPaddleHeight + Constants.TWO_QUARTERS * rightPaddle.getFifthY() and self.getCenterY() + Constants.PADDLE_HEIGHT >= rightPaddle.getCenterY() + halfPaddleHeight - Constants.TWO_QUARTERS * leftPaddle.getFifthY():
          if self.getCenterX() + self.__radius >= rightPaddle.getCenterX():
              rightPaddle.collision(self, self.getCenterY())

        

        self.setCenterX(self.getCenterX() + self.__xDir * Constants.SPEED)

        if self.getCenterY() >= height:
            self.__yDir =  Constants.DIR_CHANGE_RIGHT
        elif self.getCenterY() <= Constants.TOP_WALL:
            self.__yDir = Constants.DIR_CHANGE_LEFT

        self.setCenterY(self.getCenterY() + self.__yDir * Constants.SPEED)

        if self.getCenterX() <= Constants.LEFT_WALL:
            score[Constants.P_ONE_SCORE] += Constants.INCREMENT_SCORE
            self.setCenterX(Constants.HEIGHT/Constants.DIVIDE_TWO)
            self.setCenterY(Constants.WIDTH/Constants.DIVIDE_TWO)

        elif self.getCenterX() >= width:
            score[Constants.P_TWO_SCORE] += Constants.INCREMENT_SCORE
            self.setCenterX(Constants.HEIGHT/Constants.DIVIDE_TWO)
            self.setCenterY(Constants.WIDTH/Constants.DIVIDE_TWO)
            
            

    def getXDir(self):
        return self.__xDir

    def getYDir(self):
        return self.__yDir

    def setYDir(self, newVal):
        self.__yDir = newVal

    def setXDir(self, newVal):
        self.__xDir = newVal

    def getRadius(self):
        return self.__radius


        
