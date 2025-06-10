# Demo pygame 2 - jeden obraz, kliknięcie myszą i przesunięcie obrazu.

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

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.
ballImage = pygame.image.load('images/ball.png')

# 5 - Inicjalizacja zmiennych.
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        # Jeżeli został kliknięty przycisk zamknięcia okna, należy wyjść z pygame i zakończyć działanie programu.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Sprawdzenie, czy użytkownik kliknął myszą.
        if event.type == pygame.MOUSEBUTTONUP:
            #  mouseX, mouseY = event.pos   #  Można tak zrobić, jeśli zachodzi potrzeba.

            # Sprawdzenie, czy kliknięto prostokąt ograniczający piłkę.
            # Jeżeli tak, należy losowo wybrać nowe współrzędne.
            if ballRect.collidepoint(event.pos):
                ballX = random.randrange(MAX_WIDTH)
                ballY = random.randrange(MAX_HEIGHT)
                ballRect = pygame.Rect(ballX, ballY, BALL_WIDTH_HEIGHT, BALL_WIDTH_HEIGHT)

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.

    # 9 - Usunięcie zawartości okna.
    window.fill(BLACK)

    # 10 - Wyświetlenie wszystkich elementów okna.
    # Wyświetlenie piłki w miejscu o losowo wybranych współrzędnych.
    window.blit(ballImage, (ballX, ballY))

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
