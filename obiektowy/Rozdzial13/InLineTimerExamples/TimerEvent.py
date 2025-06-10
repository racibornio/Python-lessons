# Zegar wykorzystujący zdarzenie niestandardowe.

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
import sys
import pygwidgets

# 2 - Definiowanie stałych.
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)
#TIMER_EVENT_ID = pygame.USEREVENT + 1  # Podejście stosowane w pygame 1.x.
TIMER_EVENT_ID = pygame.event.custom_type()  # Nowość w frameworku pygame 2.0.
TIMER_LENGTH = 2.5 # Wartość w sekundach.

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.
headerMessage = pygwidgets.DisplayText(window, (0, 50), 'Kliknij przycisk "Start", aby uruchomić ' +
                                    str(TIMER_LENGTH) + '-sekundowy zegar:',
                                    fontSize=36, justified='center', width=WINDOW_WIDTH)

startButton = pygwidgets.TextButton(window, (200, 100), 'Start')

clickMeButton = pygwidgets.TextButton(window, (320, 100), 'Kliknij mnie')

timerMessage = pygwidgets.DisplayText(window, (0, 160), 'Komunikat wyświetlany podczas działania zegara.',
                                    fontSize=36, justified='center', width=WINDOW_WIDTH)

timerMessage.hide()  # Na początku komunikat pozostaje ukryty.

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        # Jeżeli został kliknięty przycisk zamknięcia okna, należy wyjść z pygame i zakończyć działanie programu.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if startButton.handleEvent(event):
            pygame.time.set_timer(TIMER_EVENT_ID,
                                               int(TIMER_LENGTH * 1000), True)
            startButton.disable()
            timerMessage.show()
            print('Uruchomienie zegara.')

        if event.type == TIMER_EVENT_ID:
            startButton.enable()
            timerMessage.hide()
            print('Zdarzenie zakończyło działanie zegara.')

        if clickMeButton.handleEvent(event):
            print('Kliknięty został inny przycisk.')

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.

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




