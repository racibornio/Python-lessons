# Gra Większa czy mniejsza - wersja z użyciem frameworka pygame.
# Program główny.

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
import sys
import pygwidgets
from Game import *

# 2 - Definiowanie stałych.
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FRAMES_PER_SECOND = 30

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.
background = pygwidgets.Image(window, (0, 0),
                            'images/background.png')
newGameButton = pygwidgets.TextButton(window, (20, 530),
                            'Nowa gra', width=100, height=45)
higherButton = pygwidgets.TextButton(window, (540, 520),
                            'Większa', width=120, height=55)
lowerButton = pygwidgets.TextButton(window, (340, 520),
                            'Mniejsza', width=120, height=55)
quitButton = pygwidgets.TextButton(window, (880, 530),
                            'Koniec', width=100, height=45)

# 5 - Inicjalizacja zmiennych.
oGame = Game(window)

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        if ((event.type == QUIT) or
            ((event.type == KEYDOWN) and (event.key == K_ESCAPE)) or
            (quitButton.handleEvent(event))):
            pygame.quit()
            sys.exit()

        if newGameButton.handleEvent(event):
            oGame.reset()
            lowerButton.enable()
            higherButton.enable()

        if higherButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(HIGHER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()

        if lowerButton.handleEvent(event):
            gameOver = oGame.hitHigherOrLower(LOWER)
            if gameOver:
                higherButton.disable()
                lowerButton.disable()

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.

    # 9 - Usunięcie zawartości okna przed jego ponownym wyświetleniem.
    background.draw()

    # 10 - Wyświetlenie elementów okna.
    # Nakazanie grze wyświetlenia obiektu typu Game.
    oGame.draw()
    # Wyświetlenie pozostałych komponentów interfejsu użytkownika.
    newGameButton.draw()
    higherButton.draw()
    lowerButton.draw()
    quitButton.draw()

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)
