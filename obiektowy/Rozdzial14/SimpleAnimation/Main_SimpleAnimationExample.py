# Przykład użycia animacji.
# W tym programie został użyty obiekt typu SimpleAnimation.

# 1 - Importowanie bibliotek.
import pygame
from pygame.locals import *
import sys
import pygwidgets
from SimpleAnimation import *

# 2 Definiowanie stałych.
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 30
BGCOLOR = (0, 128, 128)

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.
dinosaurAnimTuple = ('images/Dinobike/f1.gif',
                      'images/Dinobike/f2.gif',
                      'images/Dinobike/f3.gif',
                      'images/Dinobike/f4.gif',
                      'images/Dinobike/f5.gif',
                      'images/Dinobike/f6.gif',
                      'images/Dinobike/f7.gif',
                      'images/Dinobike/f8.gif',
                      'images/Dinobike/f9.gif',
                      'images/Dinobike/f10.gif')

# 5 - Inicjalizacja zmiennych.
oDinosaurAnimation = SimpleAnimation(window, (22, 140),
                                     dinosaurAnimTuple, .1)
oPlayButton = pygwidgets.TextButton(window, (20, 240), "Uruchom")

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


        if oPlayButton.handleEvent(event):
            oDinosaurAnimation.play()

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.
    oDinosaurAnimation.update()

    # 9 - Usunięcie zawartości okna.
    window.fill(BGCOLOR)

    # 10 - Wyświetlenie wszystkich elementów okna.
    oDinosaurAnimation.draw()
    oPlayButton.draw()

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
