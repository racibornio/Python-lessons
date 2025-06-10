import pygame
from pygame.locals import *
import random

# Klasa Ball.
class Ball():

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window  # Zapamiętanie okna, aby później można było je wyświetlić.
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.image = pygame.image.load('images/ball.png')
        # Prostokąt o parametrach [x, y, width, height].
        ballRect = self.image.get_rect()
        self.width = ballRect.width
        self.height = ballRect.height
        self.maxWidth = windowWidth - self.width
        self.maxHeight = windowHeight - self.height

        # Losowy wybór położenia początkowego.
        self.x = random.randrange(0, self.maxWidth)
        self.y = random.randrange(0, self.maxHeight)

        # Losowy wybór prędkości z przedziału od -4 do 4, z wyjątkiem 0,
        # w obu kierunkach, x i y.
        speedsList = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.xSpeed = random.choice(speedsList)
        self.ySpeed = random.choice(speedsList)

    def update(self):
        # Sprawdzenie pod kątem uderzenia w ścianę. W takim wypadku trzeba zmienić kierunek ruchu.
        if (self.x < 0) or (self.x >= self.maxWidth):
            self.xSpeed = -self.xSpeed

        if (self.y < 0) or (self.y >= self.maxHeight):
            self.ySpeed = -self.ySpeed

        # Uaktualnienie współrzędnych x i y obiektu Ball, z użyciem prędkości w dwóch kierunkach.
        self.x = self.x + self.xSpeed
        self.y = self.y + self.ySpeed

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
