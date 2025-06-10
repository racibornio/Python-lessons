# Demo pygame 3(a) - jeden obraz, którym można poruszać za pomocą klawiatury.

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
MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
TARGET_X = 400
TARGET_Y = 320
TARGET_WIDTH_HEIGHT = 120
N_PIXELS_TO_MOVE = 3

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.
ballImage = pygame.image.load('images/ball.png')
targetImage = pygame.image.load('images/target.jpg')

# 5 - Inicjalizacja zmiennych.
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
targetRect = pygame.Rect(TARGET_X, TARGET_Y, TARGET_WIDTH_HEIGHT, TARGET_WIDTH_HEIGHT)

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        # Jeżeli został kliknięty przycisk zamknięcia okna, należy wyjść z pygame i zakończyć działanie programu.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Sprawdzenie, czy użytkownik nacisnął klawisz.
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ballX = ballX - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_RIGHT:
                ballX = ballX + N_PIXELS_TO_MOVE
            elif event.key == pygame.K_UP:
                ballY = ballY - N_PIXELS_TO_MOVE
            elif event.key == pygame.K_DOWN:
                ballY = ballY + N_PIXELS_TO_MOVE

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.
    # Sprawdzenie, czy piłka ma kolizję z prostokątem docelowym.
    ballRect = pygame.Rect(ballX, ballY,
                                       BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)
    if ballRect.colliderect(targetRect):
        print('Piłka znajduje się w prostokącie docelowym.')

    # 9 - Usunięcie zawartości okna.
    window.fill(BLACK)

    # 10 - Wyświetlenie wszystkich elementów okna.
    window.blit(targetImage, (TARGET_X, TARGET_Y))  # Wyświetlenie prostokąta docelowego.
    window.blit(ballImage, (ballX, ballY))  # Wyświetlenie piłki.

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
