# Demo pygame 6(a) - używanie klasy Ball, odbijanie jednej piłki.

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
import sys
import random
from Ball import *  # Wczytanie kodu klasy Ball.

# 2 - Definiowanie stałych.
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.
    oBall.update()  # Uaktualnienie obiektu klasy Ball.

   # 9 - Usunięcie zawartości okna przed jego ponownym wyświetleniem.
    window.fill(BLACK)

    # 10 - Wyświetlenie elementów okna.
    oBall.draw()  # Wyświetlenie obiektu klasy Ball.


    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.


