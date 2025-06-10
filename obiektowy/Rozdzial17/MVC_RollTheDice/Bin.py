# Klasa Bin - Rzuć kośćmi

import pygame
import pygwidgets

MAX_BAR_HEIGHT = 300
BAR_BOTTOM = 390
BAR_WIDTH = 30
BAR_COLOR = (128, 128, 128)
COLUMN_LEFT_START = 30
COLUMN_OFFSET = 55

# Klasa Bin.
class Bin():
    def __init__(self, window, binNumber):
        self.window = window
        self.pixelsPerCount = MAX_BAR_HEIGHT

        self.left = COLUMN_LEFT_START + (binNumber * COLUMN_OFFSET)
        self.oBinLabel = pygwidgets.DisplayText(window,
                                (self.left + 3, BAR_BOTTOM + 12), binNumber,
                                fontName='arial', fontSize=24, width=25, justified='center')
        self.oBinCount = pygwidgets.DisplayText(window,
                                (self.left - 5, BAR_BOTTOM + 50), '',
                                fontName='arial', fontSize=18, width=50, justified='center')
        self.oBinPercent = pygwidgets.DisplayText(window,
                                (self.left - 5, BAR_BOTTOM + 80), '',
                                 fontName='arial', fontSize=18, width=50, justified='right')

    def update(self, nRounds, count, percent):
        self.oBinCount.setValue(count)
        percent = '{:.1%}'.format(percent)
        self.oBinPercent.setValue(percent)

        # Wymuszenie użycia wartości zmiennoprzecinkowej, użyj liczby całkowitej podczas wyświetlania prostokąta.
        # Trzeba obliczyć rzeczywistą wysokość i pomnożyć przez dwa, efekt wyglądał lepiej.
        # Wszystkie słupki na pewno będą miały wartość poniżej 50%.
        self.nPixelsPerTrial = float(MAX_BAR_HEIGHT)  / nRounds
        barHeight = int(count * self.nPixelsPerTrial)  * 2
        self.rect = pygame.Rect(self.left, BAR_BOTTOM - barHeight, BAR_WIDTH, barHeight)

    def draw(self):
        pygame.draw.rect(self.window, BAR_COLOR, self.rect, 0)
        self.oBinLabel.draw()
        self.oBinCount.draw()
        self.oBinPercent.draw()
