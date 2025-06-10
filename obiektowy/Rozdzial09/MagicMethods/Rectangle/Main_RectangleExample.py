import pygame
import sys
from pygame.locals import *
from Rectangle import *

# Definiowanie stałych.
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_RECTANGLES = 10
FIRST_RECTANGLE = 'first'
SECOND_RECTANGLE = 'second'

# Przygotowanie okna.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
clock = pygame.time.Clock()

rectanglesList = []
for i in range(0, N_RECTANGLES):
    oRectangle = Rectangle(window)
    rectanglesList.append(oRectangle)

whichRectangle = FIRST_RECTANGLE

# Pętla główna.
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            for oRectangle in rectanglesList:
                if oRectangle.clickedInside(event.pos):
                    print('Kliknięto', whichRectangle, 'prostokąt.')

                    if whichRectangle == FIRST_RECTANGLE:
                        oFirstRectangle = oRectangle
                        whichRectangle = SECOND_RECTANGLE

                    elif whichRectangle == SECOND_RECTANGLE:
                        oSecondRectangle = oRectangle
                        # Użytkownik wybrał dwa prostokąty, które teraz zostaną porównane.
                        if oFirstRectangle == oSecondRectangle:
                            print('Prostokąty mają taką samą wielkość.')
                        elif oFirstRectangle < oSecondRectangle:
                            print('Pierwszy prostokąt jest mniejszy od drugiego.')
                        else: # Musi być większy.
                            print('Pierwszy prostokąt jest większy od drugiego.')
                        whichRectangle = FIRST_RECTANGLE

    # Usunięcie zawartości okna i wyświetlenie wszystkich prostokątów.
    window.fill(WHITE)
    for oRectangle in rectanglesList:
        oRectangle.draw()

    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)
