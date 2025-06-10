# Klasy Baddie i BaddieMgr.

import pygame
import pygwidgets
import random
from Constants import *

# Baddie class
class Baddie():
    MIN_SIZE = 10
    MAX_SIZE = 40
    MIN_SPEED = 1
    MAX_SPEED = 8
    # Obraz będzie wczytany tylko jednokrotnie.
    BADDIE_IMAGE = pygame.image.load('images/baddie.png')

    def __init__(self, window):
        self.window = window
        # Utworzenie obiektu obrazu.
        size = random.randrange(Baddie.MIN_SIZE, Baddie.MAX_SIZE + 1)
        self.x = random.randrange(0, WINDOW_WIDTH - size)
        self.y = 0 - size # Na początku obiekt znajduje się ponad oknem.
        self.image = pygwidgets.Image(self.window, (self.x, self.y),
                                      Baddie.BADDIE_IMAGE)

        # Skalowanie obiektu.
        percent = (size * 100) / Baddie.MAX_SIZE
        self.image.scale(percent, False)
        self.speed = random.randrange(Baddie.MIN_SPEED,
                                                      Baddie.MAX_SPEED + 1)

    def update(self):  # Przesunięcie do dołu obiektu postaci czerwonej.
        self.y = self.y + self.speed
        self.image.setLoc((self.x, self.y))
        if self.y > GAME_HEIGHT:
            return True  # Obiekt musi być usunięty.
        else:
            return False  # Obiekt pozostaje w oknie.

    def draw(self):
        self.image.draw()

    def collide(self, playerRect):
        collidedWithPlayer = self.image.overlaps(playerRect)
        return collidedWithPlayer

# Klasa BaddieMgr.
class BaddieMgr():
    ADD_NEW_BADDIE_RATE = 8  # Częstotliwość dodawania nowych obiektów.

    def __init__(self, window):
        self.window = window
        self.reset()

    def reset(self):  # Metoda wywoływana podczas rozpoczynania nowej gry.
        self.baddiesList = []
        self.nFramesTilNextBaddie = BaddieMgr.ADD_NEW_BADDIE_RATE

    def update(self):
        # Nakazanie każdemu obiektowi postaci czerwonej, by się uaktualnił.
        # Sprawdzenie, ile obiektów postaci czerwonej wypadło poza dolną krawędź okna.
        nBaddiesRemoved = 0
        baddiesListCopy = self.baddiesList.copy()
        for oBaddie in baddiesListCopy:
            deleteMe = oBaddie.update()
            if deleteMe:
                self.baddiesList.remove(oBaddie)
                nBaddiesRemoved = nBaddiesRemoved + 1

        # Sprawdzenie, czy to pora na dodanie nowego obiektu.
        self.nFramesTilNextBaddie = self.nFramesTilNextBaddie - 1
        if self.nFramesTilNextBaddie == 0:
            oBaddie = Baddie(self.window)
            self.baddiesList.append(oBaddie)
            self.nFramesTilNextBaddie = BaddieMgr.ADD_NEW_BADDIE_RATE

        # Przekazanie liczby usuniętych obiektów.
        return nBaddiesRemoved

    def draw(self):
        for oBaddie in self.baddiesList:
            oBaddie.draw()

    def hasPlayerHitBaddie(self, playerRect):
        for oBaddie in self.baddiesList:
            if oBaddie.collide(playerRect):
                return True
        return False
