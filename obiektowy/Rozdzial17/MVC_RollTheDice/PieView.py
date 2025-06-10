# Widok PieView - Rzuć kośćmi

import pygame
import pygame.gfxdraw
import math
from pygwidgets import *
from Constants import *

CENTER_X = 300
CENTER_Y = 300
RADIUS = 200
RADIUS_MINUS_1 = RADIUS - 1
BLACK = (0, 0, 0)

class PieView():
    def __init__(self, window, oModel):
        self.window = window
        self.oModel = oModel
        self.legendFieldsDict = {}
        y = 160
        # Utworzenie pól legendy wykresu.
        for index in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            gray = (index * 20, index * 20, index * 20)
            oLegendField = pygwidgets.DisplayText(window, (550, y),
                                        value=str(index), fontSize=32,
                                        textColor=gray)
            self.legendFieldsDict[index] = oLegendField
            y = y + 25 # Odległość pionowa.

    def update(self, ):
        nRounds, resultsDict, percentsDict = self.oModel.getRoundsRollsPercents()

        self.nRounds = nRounds
        self.resultsDict = resultsDict
        self.percentsDict = percentsDict
        for index in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            # Tę wartość można użyć później.
            #rollCount = resultsDict[index]
            percent = percentsDict[index]
            oLegendField = self.legendFieldsDict[index]

            # Utworzenie wartości procentowej jako ciągu tekstowego z jedną cyfrą po przecinku.
            percent = '{:.1%}'.format(percent)
            oLegendField.setValue(str(index) + ':   ' + percent)

    def drawFilledArc(self, centerX, centerY, radius, degrees1, degrees2, color):
        """Ta metoda generuje listę punktów używanych do utworzenia wypełnionego
        wielokąta, który przedstawia zakrzywienie w okręgu.  Przekazane kąty i odrobinę
        trygonometrii wykorzystamy do ustalenia tych punktów na zakrzywieniu.
        """
        centerTuple = (centerX, centerY)
        nPointsToDraw = int(degrees2 - degrees1)
        if nPointsToDraw == 0:
            return  # Nie ma nic do wyświetlenia.
        # Oba te parametry, degrees, muszę być skonwertowane na radiany, aby obliczyć punkty.
        radians1 = math.radians(degrees1)
        radians2 = math.radians(degrees2)
        radiansDiff = (radians2 - radians1)  / nPointsToDraw

        # Początek i koniec znajduje się w środku okręgu.
        pointsList = [centerTuple]
        # Ustalenie punktów znajdujących się na krawędzi zakrzywienia.
        for pointNumber in range(nPointsToDraw + 1):
            offset = pointNumber * radiansDiff
            x = centerX + (radius * math.cos(radians1 + offset))
            y = centerY + (radius * math.sin(radians1 + offset))
            pointsList.append((x, y))
        pointsList.append(centerTuple)

        pygame.gfxdraw.filled_polygon(self.window, pointsList, color)
        # Jeżeli wokół zakrzywienia chcesz otrzymać czarne obramowanie,
        # usuń znak komentarza na początku następnego wiersza.
        #pygame.gfxdraw.polygon(self.window, pointsList, BLACK)

    # Wyświetlenie "kawałka ciasta" (zakrzywienia) dla każdego wyniku.
    def draw(self):
        startAngle = 0.0
        for index in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            percent = self.percentsDict[index]
            endAngle = startAngle + (percent * 360)
            gray = (index * 20, index * 20, index * 20)
            self.drawFilledArc(CENTER_X, CENTER_Y, RADIUS_MINUS_1,
                                       startAngle, endAngle, gray)
            self.legendFieldsDict[index].draw()

            startAngle = endAngle  # Przygotowanie gruntu dla następnego kawałka.

        pygame.draw.circle(self.window, BLACK, (CENTER_X, CENTER_Y), RADIUS, 2)
