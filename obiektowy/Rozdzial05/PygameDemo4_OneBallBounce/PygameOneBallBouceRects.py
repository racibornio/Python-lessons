# Demo pygame 4(b) - jeden obraz, piłka odbija się od krawędzi okna, używany jest prostokąt ograniczający obiektu.

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
import sys
import random

# 2 - Definiowanie stałych.
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.
ballImage = pygame.image.load('images/ball.png')

# 5 - Inicjalizacja zmiennych.
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        # Jeżeli został kliknięty przycisk zamknięcia okna, należy wyjść z pygame i zakończyć działanie programu.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed  # Odwrócenie kierunku ruchu na osi X.

    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed  # Odwrócenie kierunku ruchu na osi Y.

    # Uaktualnienie prostokąta ograniczającego piłkę, z użyciem prędkości w dwóch kierunkach.
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed

    # 9 - Usunięcie zawartości okna przed jego ponownym wyświetleniem.
    window.fill(BLACK)

    # 10 - Wyświetlenie elementów okna.
    window.blit(ballImage, ballRect)

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
