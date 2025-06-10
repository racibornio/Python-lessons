# Program wykorzystujący obiekt typu SimpleSpriteSheetAnimation.

# 1 - Importowanie bibliotek.
import pygame
from pygame.locals import *
import sys
import pygwidgets
from SimpleSpriteSheetAnimation import *

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

# 5 - Inicjalizacja zmiennych.
oWaterAnimation = SimpleSpriteSheetAnimation(window, (22, 140), 'images/water_003.png', 50, 192, 192, .05)
oPlayButton = pygwidgets.TextButton(window, (60, 320), "Uruchom")

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if oPlayButton.handleEvent(event):
            oWaterAnimation.play()

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.
    oWaterAnimation.update()

    # 9 - Usunięcie zawartości okna.
    window.fill(BGCOLOR)

    # 10 - Wyświetlenie wszystkich elementów okna.
    oWaterAnimation.draw()
    oPlayButton.draw()

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
