# Demo pygame 6(b) - używanie klasy Ball, odbijanie wielu piłek.

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
N_BALLS = 3

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.
ballList = []
for oBall in range(0, N_BALLS):
    # W trakcie każdej iteracji pętli następuje utworzenie obiektu typu Ball.
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)  # Dołączenie nowego obiektu typu Ball do listy egzemplarzy Ball.

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.
    for oBall in ballList:
        oBall.update()  # Uaktualnienie poszczególnych obiektów Ball.

   # 9 - Usunięcie zawartości okna przed jego ponownym wyświetleniem.
    window.fill(BLACK)

    # 10 - Wyświetlenie elementów okna.
    for oBall in ballList:
        oBall.draw()   # Wyświetlenie poszczególnych obiektów Ball.

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.


