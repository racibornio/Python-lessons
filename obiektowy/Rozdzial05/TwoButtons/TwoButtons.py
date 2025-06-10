# Demo pygame - dwa przyciski.

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
import pygwidgets
import sys

# Definiowanie stałych.
GRAY = (200, 200, 200)
WINDOW_WIDTH = 270
WINDOW_HEIGHT = 100
FRAMES_PER_SECOND = 30

# 2 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.
barkSound = pygame.mixer.Sound('bark.wav')
meowSound = pygame.mixer.Sound('meow.wav')

# 5 - Inicjalizacja zmiennych.
# Tworzenie egzemplarzy przycisku type Simple.
buttonA = pygwidgets.TextButton(window, (20, 30), 'Hau')
buttonB = pygwidgets.TextButton(window, (150, 30), 'Miau')

counter = 0

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        # Jeżeli został kliknięty przycisk zamknięcia okna, należy wyjść z pygame i zakończyć działanie programu.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Przekazanie zdarzenia do przycisku i sprawdzenie, czy został kliknięty.
        if  buttonA.handleEvent(event):
            print('Użytkownik kliknął przycisk Hau.  Liczba pętli wykonanych przez program:', counter)
            barkSound.play()
        elif  buttonB.handleEvent(event):
            print('Użytkownik kliknął przycisk Miau.  Liczba pętli wykonanych przez program:', counter)
            meowSound.play()

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.
    counter = counter + 1

    # 9 - Usunięcie zawartości okna przed jego ponownym wyświetleniem.
    window.fill(GRAY)

    # 10 - Wyświetlenie wszystkich elementów ekranu.
    buttonA.draw()
    buttonB.draw()

    # 11 - Uaktualnienie ekranu.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
