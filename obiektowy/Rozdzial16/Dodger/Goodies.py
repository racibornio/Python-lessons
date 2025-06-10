# Klasy Goodie i GoddieMgr.
import pygame
import pygwidgets
import random
from Constants import *

class Goodie():
    MIN_SIZE = 10
    MAX_SIZE = 40
    MIN_SPEED = 1
    MAX_SPEED = 8
    # Obraz będzie wczytany tylko jednokrotnie.
    GOODIE_IMAGE = pygame.image.load('images/goodie.png')
    RIGHT = 'right'
    LEFT = 'left'

    def __init__(self, window):
        self.window = window
        size = random.randrange(Goodie.MIN_SIZE, Goodie.MAX_SIZE + 1)
        self.y = random.randrange(0, GAME_HEIGHT - size)

        self.direction = random.choice([Goodie.LEFT, Goodie.RIGHT])
        if self.direction == Goodie.LEFT:  # Na początku obiekt znajduje się po prawej stronie okna.
            self.x = WINDOW_WIDTH
            self.speed = - random.randrange(Goodie.MIN_SPEED,
                                                            Goodie.MAX_SPEED + 1)
            self.minLeft = - size
        else:  # Rozpoczęcie po lewej stronie okna.
            self.x = 0 - size
            self.speed = random.randrange(Goodie.MIN_SPEED,
                                                          Goodie.MAX_SPEED + 1)

        self.image = pygwidgets.Image(self.window,
                                                     (self.x, self.y), Goodie.GOODIE_IMAGE)
        percent = int((size * 100) / Goodie.MAX_SIZE)
        self.image.scale(percent, False)

    def update(self):
        self.x = self.x + self.speed
        self.image.setLoc((self.x, self.y))
        if self.direction == Goodie.LEFT:
            if self.x < self.minLeft:
                return True  # Obiekt musi być usunięty.
            else:
                return False  # Obiekt pozostaje w oknie.
        else:
            if self.x > WINDOW_WIDTH:
                return True  # Obiekt musi być usunięty.
            else:
                return False  # Obiekt pozostaje w oknie.

    def draw(self):
        self.image.draw()

    def collide(self, playerRect):
        collidedWithPlayer = self.image.overlaps(playerRect)
        return collidedWithPlayer


class GoodieMgr():
    GOODIE_RATE_LO = 90
    GOODIE_RATE_HI = 111

    def __init__(self, window):
        self.window = window
        self.reset()

    def reset(self):  # Metoda wywoływana podczas rozpoczynania nowej gry.
        self.goodiesList = []
        self.nFramesTilNextGoodie = GoodieMgr.GOODIE_RATE_HI

    def update(self, thePlayerRect):
        # Nakazanie każdemu obiektowi postaci zielonej, by się uaktualnił.
        # Jeżeli obiekt postaci zielonej wyszedł poza krawędź okna, należy go usunąć.
        # Sprawdzenie, ile obiektów postaci zielonej zetknęło się z graczem i ich usunięcie.
        nGoodiesHit = 0
        goodiesListCopy = self.goodiesList.copy()
        for oGoodie in goodiesListCopy:
            deleteMe = oGoodie.update()
            if deleteMe:
                self.goodiesList.remove(oGoodie)  # Usunięcie tego obiektu.

            elif oGoodie.collide(thePlayerRect):
                self.goodiesList.remove(oGoodie)  # Usunięcie tego obiektu.
                nGoodiesHit = nGoodiesHit + 1

        # Jeżeli upłynęła odpowiednia liczba klatek, należy
        # dodać nowy obiekt postaci zielonej (i wyzerować licznik klatek).
        self.nFramesTilNextGoodie = self.nFramesTilNextGoodie - 1
        if self.nFramesTilNextGoodie == 0:
            oGoodie = Goodie(self.window)
            self.goodiesList.append(oGoodie)
            self.nFramesTilNextGoodie = random.randrange(
                                                            GoodieMgr.GOODIE_RATE_LO,
                                                            GoodieMgr.GOODIE_RATE_HI)

        return nGoodiesHit  # Zwrot liczby obiektów postaci zielonej, które zetknęły się z obiektem przedstawiającym gracza.

    def draw(self):
        for oGoodie in self.goodiesList:
            oGoodie.draw()
