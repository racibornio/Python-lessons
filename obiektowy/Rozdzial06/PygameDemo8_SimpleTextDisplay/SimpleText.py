# Klasa SimpleText.

import pygame
from pygame.locals import *

class SimpleText():

    def __init__(self, window, loc, value, textColor):
        pygame.font.init()
        self.window = window
        self.loc = loc
        self.font = pygame.font.SysFont(None, 30)
        self.textColor = textColor
        self.text = None  # Wywołanie setText wymusi utworzenie
                          # obrazu zawierającego tekst do wyświetlenia.
        self.setValue(value) # Zdefiniowanie tekstu początkowego do wyświetlenia.

    def setValue(self, newText):
        if self.text == newText:
            return  # Nie ma nic do zmiany.

        self.text = newText  # Zapisanie nowego tekstu.
        self.textSurface = self.font.render(self.text, True, self.textColor)

    def draw(self):
        self.window.blit(self.textSurface, self.loc)
