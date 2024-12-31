import pygame
from Ball import Ball
from Paddle import Paddle
from Constants import *

class Pong:

    def __init__(self):
        self.__ball = Ball(BALL_COLOR, HEIGHT/DIVIDE_TWO, WIDTH/DIVIDE_TWO, RADIUS)
        self.__paddleLeft = Paddle(PADDLE_COLOR, PADDLE_LEFT_X, PADDLE_LEFT_Y, PADDLE_WIDTH, PADDLE_HEIGHT) 
        self.__paddleRight = Paddle(PADDLE_COLOR, PADDLE_RIGHT_X, PADDLE_LEFT_Y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.__score = pygame.math.Vector2(START_X,START_Y)
    

    def reset(self):
        self.__paddleLeft.setCenterX(PADDLE_LEFT_X)
        self.__paddleLeft.setCenterY(PADDLE_LEFT_Y)
        self.__paddleRight.setCenterX(PADDLE_RIGHT_X)
        self.__paddleRight.setCenterY(PADDLE_LEFT_Y)
        self.__ball.setCenterX(HEIGHT/DIVIDE_TWO)
        self.__ball.setCenterY(WIDTH/DIVIDE_TWO)
        self.__ball.setYDir(START_Y)
        self.__ball.setXDir(START_X)
        self.__score = pygame.Vector2(START_X,START_Y)

    def setP1Score(self):
        self.__score[P_ONE_SCORE] += INCREMENT_SCORE

    def setP2Score(self):
        self.__score[P_TWO_SCORE] += INCREMENT_SCORE

    def getP1Score(self):
        return self.__score[P_ONE_SCORE]

    def getP2Score(self):
        return self.__score[P_TWO_SCORE]

    def run(self):
        pygame.init()

        font = pygame.font.Font('freesansbold.ttf', SCORE_SIZE)
    
        screen = pygame.display.set_mode((HEIGHT, WIDTH), pygame.RESIZABLE)

        clock = pygame.time.Clock()

        running = True

        while running:
            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if keys[pygame.K_r]:
                        self.reset()
                    if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_a] or keys[pygame.K_d]:
                        if keys[pygame.K_w]:
                            moveKey = chr(pygame.K_w)
                        if keys[pygame.K_s]:
                            moveKey = chr(pygame.K_s)
                        if keys[pygame.K_a]:
                            moveKey = chr(pygame.K_a)
                        if keys[pygame.K_d]:
                            moveKey = chr(pygame.K_d)
                        self.__paddleLeft.move(moveKey, screenWidth, screenHeight)
                    if keys[pygame.K_i] or keys[pygame.K_k] or keys[pygame.K_j] or keys[pygame.K_l]:
                        if keys[pygame.K_i]:
                           moveKey = chr(pygame.K_i)
                        if keys[pygame.K_k]:
                            moveKey = chr(pygame.K_k)
                        if keys[pygame.K_j]:
                            moveKey = chr(pygame.K_j)
                        if keys[pygame.K_l]:
                            moveKey = chr(pygame.K_l)
                        self.__paddleRight.move(moveKey, screenWidth, screenHeight)
                    if keys[pygame.K_SPACE]:
                        self.__ball.setXDir(DIR_CHANGE_RIGHT)

            screen.fill(BACKGROUND_COLOR)

            screenWidth = pygame.display.Info().current_w

            screenHeight = pygame.display.Info().current_h

            self.__paddleLeft.move(keys, screenWidth, screenHeight)

            self.__paddleRight.move(keys, screenWidth, screenHeight)

            self.__ball.move(screenWidth, screenHeight, self.__paddleLeft, self.__paddleRight, self.__score)

            pygame.draw.circle(screen, self.__ball.getColor(), (self.__ball.getCenterX(), self.__ball.getCenterY()), self.__ball.getRadius())

            pygame.draw.rect(screen, self.__paddleLeft.getColor(), pygame.Rect(self.__paddleLeft.getCenterX(), self.__paddleLeft.getCenterY(), PADDLE_WIDTH, PADDLE_HEIGHT))

            pygame.draw.rect(screen, self.__paddleRight.getColor(), pygame.Rect(self.__paddleRight.getCenterX(), self.__paddleRight.getCenterY(), PADDLE_WIDTH, PADDLE_HEIGHT))


            scoreKeeper = font.render(str(self.__score), ANTIALIAS, TEXT_COLOR, BACKGROUND_COLOR)

            textLocation = (SCORE_X, SCORE_Y)

            screen.blit(scoreKeeper, textLocation)

            winFont = pygame.font.Font('freesansbold.ttf', VICTORY_SIZE)
            messageLocation = (WIN_MESSAGE_LOCATION_X, WIN_MESSAGE_LOCATION_Y)

            if self.__score[P_ONE_SCORE] == WINNING_SCORE:
               winMessage = winFont.render(PLAYER_ONE_WIN, ANTIALIAS, TEXT_COLOR, BACKGROUND_COLOR)
               screen.blit(winMessage, messageLocation)
               self.__ball.setXDir(START_X)
               self.__ball.setYDir(START_Y)
               if keys[pygame.K_SPACE]:
                   self.reset()
               
            elif self.__score[P_TWO_SCORE] == WINNING_SCORE:
              winMessage = winFont.render(PLAYER_TWO_WIN, ANTIALIAS, TEXT_COLOR, BACKGROUND_COLOR)
              screen.blit(winMessage, messageLocation)
              self.__ball.setXDir(START_X)
              self.__ball.setYDir(START_Y)
              if keys[pygame.K_SPACE]:
                  self.reset()
              

            pygame.display.flip()

            clock.tick(CLOCK_TIME)

        pygame.quit()
