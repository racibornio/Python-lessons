# Demo pygame 4(a) - jeden obraz, piłka odbija się od krawędzi okna, używane są współrzędne (x, y).

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
BALL_WIDTH_HEIGHT = 100
N_PIXELS_PER_FRAME = 3

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.
ballImage = pygame.image.load('images/ball.png')

# 5 - Inicjalizacja zmiennych.
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
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
    if (ballX < 0) or (ballX >= MAX_WIDTH):
        xSpeed = -xSpeed  # Odwrócenie kierunku ruchu na osi X.

    if (ballY < 0) or (ballY >= MAX_HEIGHT):
        ySpeed = -ySpeed  # Odwrócenie kierunku ruchu na osi Y.

    # Uaktualnienie położenia piłki z użyciem prędkości w dwóch kierunkach.
    ballX = ballX + xSpeed
    ballY = ballY + ySpeed

    # 9 - Usunięcie zawartości okna przed jego ponownym wyświetleniem.
    window.fill(BLACK)

    # 10 - Wyświetlenie elementów okna.
    window.blit(ballImage, (ballX, ballY))

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
