# Kod główny utworzonego w stylu MVC programu Rzuć kośćmi - Irv Kalb

# 1 - Importowanie pakietów.
# import pygame
import pygwidgets
import sys
from Constants import *
from Controller import *

# 2 - Definiowanie stałych.
FRAMES_PER_SECOND = 30

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('Rzuć kośćmi')
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.
# Utworzenie obiektu kontrolera.
oController = Controller(window)

# 6 - Pętla działająca w nieskończoność.
while True:
    # 7 -  Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Przekazanie wszystkich zdarzeń do kontrolera.
        oController.handleEvent(event)

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.

    # 9 - Usunięcie zawartości okna (pozostawienie tego zadania kontrolerowi).
    # 10 - Wyświetlenie elementów okna.
    oController.draw()

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND) # Framework pygame wstrzyma na chwilę działanie.
