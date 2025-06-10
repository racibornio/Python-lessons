# Demo pygame 7 - test użycia klasy SimpleButton.

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
from SimpleButton import *
import sys

# Definiowanie stałych.
GRAY = (200, 200, 200)
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

# 2 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.
# Utworzenie egzemplarza typu SimpleButton.
oButton = SimpleButton(window, (150, 30),
                        'images/buttonUp.png',
                        'images/buttonDown.png')

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Przekazanie zdarzenia do przycisku w celu sprawdzenia, czy został kliknięty.
        if oButton.handleEvent(event):
            print('Użytkownik kliknął przycisk.')

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.

    # 9 - Usunięcie zawartości okna.
    window.fill(GRAY)

    # 10 - Wyświetlenie wszystkich elementów okna.
    oButton.draw() # Wyświetlenie przycisku.

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
