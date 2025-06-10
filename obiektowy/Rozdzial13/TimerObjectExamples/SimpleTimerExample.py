# Program wykorzystujący prosty zegar.

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
import sys
import pygwidgets
import pyghelpers

# 2 - Definiowanie stałych.
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 240
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)
TIMER_LENGTH = 2.5  # Wartość w sekundach.

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.
headerMessage = pygwidgets.DisplayText(window, (0, 50), 'Kliknij przycisk "Start", aby uruchomić ' +
                                       str(TIMER_LENGTH) + '-sekundowy zegar:',
                                       fontSize=36, justified='center', width=WINDOW_WIDTH)

startButton = pygwidgets.TextButton(window, (280, 100), 'Start')

clickMeButton = pygwidgets.TextButton(window, (400, 100), 'Kliknij mnie')

timerMessage = pygwidgets.DisplayText(window, (0, 160), 'Komunikat wyświetlany podczas działania zegara.',
                                      fontSize=36, justified='center', width=WINDOW_WIDTH)

timerMessage.hide()  # Na początku komunikat pozostaje ukryty.
oTimer = pyghelpers.Timer(TIMER_LENGTH)  # Utworzenie obiektu typu Timer.


# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if startButton.handleEvent(event):
            oTimer.start()  # Uruchomienie zegara.
            startButton.disable()
            timerMessage.show()
            print('Uruchomienie zegara.')

        if clickMeButton.handleEvent(event):
            print('Kliknięty został inny przycisk.')

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.
    if oTimer.update():  # Wartość True oznacza, że zegar zakończył działanie.
        startButton.enable()
        timerMessage.hide()
        print('Zegar zakończył działanie.')

    # 9 - Usunięcie zawartości okna przed jego ponownym wyświetleniem.
    window.fill(WHITE)

    # 10 - Wyświetlenie wszystkich elementów ekranu.
    headerMessage.draw()
    startButton.draw()
    clickMeButton.draw()
    timerMessage.draw()

    # 11 - Uaktualnienie ekranu.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
