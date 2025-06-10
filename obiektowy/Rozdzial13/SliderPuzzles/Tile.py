# Klasa Tile.

import pygame
from Constants import *

class Tile():
    """
    Kafelek zawiera liczbę i powiązany obraz.
    """

    font = pygame.font.SysFont(None, 60)

    def __init__(self, window, tileNumber):
        self.window = window
        self.tileNumber = tileNumber

        # Użyj wywołań graficznych w celu utworzenia powierzchni dla
        # poszczególnych kafelków.
        #   W przypadku pustego kafelka, to po prostu kafelek bez niczego.
        #   W przypadku pozostałych, wyświetl okrąg i wyśrodkuj w nim liczbę.
        #
        # Ewentualnie kafelki można wczytywać z katalogu:
        # self.image = pygame.image.load('images/tile' + str(self.tileNumber + 1) + '.png')

        surface = pygame.Surface((SQUARE_WIDTH, SQUARE_HEIGHT))
        if self.tileNumber == STARTING_OPEN_SQUARE_NUMBER: # Wyświetlenie pustego obrazu.
            surface.fill(GRAY)
            pygame.draw.rect(surface, BLACK,
                             pygame.Rect((0, 0, SQUARE_WIDTH, SQUARE_HEIGHT)),
                             2)  # Czarne obramowanie wokół każdego elementu.
        else:  # Numerowane obrazy.
            surface.fill(PURPLE)
            pygame.draw.rect(surface, BLACK,
                             pygame.Rect((0, 0, SQUARE_WIDTH, SQUARE_HEIGHT)),
                             2)  # Czarne obramowanie wokół każdego elementu.
            centerX = SQUARE_WIDTH // 2
            centerY = SQUARE_HEIGHT // 2
            pygame.draw.circle(surface, YELLOW, (centerX, centerY), 35)
            numberAsImage = Tile.font.render(str(self.tileNumber + 1), True, BLACK)
            widthOfNumber = numberAsImage.get_width()
            leftPos = (SQUARE_WIDTH - widthOfNumber) // 2
            heightOfNumber = numberAsImage.get_height()
            topPos = (SQUARE_HEIGHT - heightOfNumber) // 2
            surface.blit(numberAsImage, (leftPos, topPos))

        self.image = surface

    def getTileNumber(self):
        return self.tileNumber

    def draw(self, loc):
        self.window.blit(self.image, loc)
