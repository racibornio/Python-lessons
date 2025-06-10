# Klasa Card.

import pygame
import pygwidgets

class Card():

    BACK_OF_CARD_IMAGE = pygame.image.load('images/BackOfCard.png')

    def __init__(self, window, rank, suit, value):
        self.window = window
        self.rank = rank
        self.suit = suit
        self.cardName = rank + suit
        self.value = value
        fileName = 'images/' + self.cardName + '.png'
        # Zdefiniowanie położenia początkowego; jego zmiana jest możliwa za pomocą metody setLoc().
        self.images = pygwidgets.ImageCollection(window, (0, 0),
                                {'front': fileName,
                                 'back': Card.BACK_OF_CARD_IMAGE}, 'back')

    def conceal(self):
        self.images.replace('back')

    def reveal(self):
        self.images.replace('front')

    def getName(self):
        return self.cardName

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def getRank(self):
        return self.rank

    def setLoc(self, loc): # Wywołanie metody setLoc() z ImageCollection.
        self.images.setLoc(loc)

    def getLoc(self):  # Wywołanie metody location() z ImageCollection
        loc = self.images.getLoc()
        return loc

    def draw(self):
        self.images.draw()

