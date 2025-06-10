# Demo pygame 5 - rysowanie prostych figur.

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
import sys

# 2 - Definiowanie stałych.
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
GRAY = (230, 230, 230)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
TEAL = (0, 255, 255)
PURPLE = (255, 0, 255)

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        # Jeżeli został kliknięty przycisk zamknięcia okna, należy wyjść z pygame i zakończyć działanie programu.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.

    # 9 - Usunięcie zawartości okna.
    window.fill(GRAY)

    # 10 - Wyświetlenie wszystkich elementów okna.
    # Rysowanie prostokąta.
    pygame.draw.line(window, BLUE, (20, 20), (60, 20), 4)  # W górę.
    pygame.draw.line(window, BLUE, (20, 20), (20, 60), 4)  # W lewo.
    pygame.draw.line(window, BLUE, (20, 60), (60, 60), 4)  # W prawo.
    pygame.draw.line(window, BLUE, (60, 20), (60, 60), 4)  # W dół.
    # Rysowanie znaku X w kwadracie.
    pygame.draw.line(window, BLUE, (20, 20), (60, 60), 1)
    pygame.draw.line(window, BLUE, (20, 60), (60, 20), 1)

    # Rysowanie okręgów wypełnionego i pustego.
    pygame.draw.circle(window, GREEN, (250, 50), 30, 0) # Okręg wypełniony.
    pygame.draw.circle(window, GREEN, (400, 50), 30, 2) # Krawędź o grubości 2 pikseli.

    # Rysowanie prostokątów wypełnionego i pustego.
    pygame.draw.rect(window, RED, (250, 150, 100, 50), 0) # Prostokąt wypełniony.
    pygame.draw.rect(window, RED, (400, 150, 100, 50), 1) # Krawędź o grubości 1 piksela.

    # Rysowanie elips wypełnionej i pustej.
    pygame.draw.ellipse(window, YELLOW, (250, 250, 80, 40), 0) # Elipsa wypełniona.
    pygame.draw.ellipse(window, YELLOW, (400, 250, 80, 40), 2) # Krawędź o grubości 2 pikseli.

    # Rysowanie sześciokąta.
    pygame.draw.polygon(window, TEAL, ((240, 350), (350, 350),
                                                            (410, 410), (350, 470),
                                                            (240, 470), (170, 410)))

    # Rysowanie łuku.
    pygame.draw.arc(window, BLUE, (20, 400, 100, 100), 0, 2, 5)

    # Rysowanie linii wygładzonych: pojedynczej, a następnie listy punktów.
    pygame.draw.aaline(window, RED, (500, 400),  (540, 470), 1)
    pygame.draw.aalines(window, BLUE, True,
                                  ((580, 400), (587, 450),
                                   (595, 460), (600, 444)), 1)

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.

