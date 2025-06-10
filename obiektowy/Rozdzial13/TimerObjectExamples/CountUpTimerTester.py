# Przykład użycia zegara.

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
import sys
import pygwidgets
import pyghelpers

# 2 - Definiowanie stałych.
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 240
FRAMES_PER_SECOND = 30
WHITE = (255, 255, 255)

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.
oHeaderMessage = pygwidgets.DisplayText(window, (0, 50), 'Kliknij przycisk "Start", aby uruchomić:',
                                       fontSize=36, justified='center', width=WINDOW_WIDTH)

oStartButton = pygwidgets.TextButton(window, (180, 100), 'Start')

oStopButton = pygwidgets.TextButton(window, (320, 100), 'Stop')

oTimerMessage = pygwidgets.DisplayText(window, (66, 160), 'getTimeInSeconds      getTimeInHHMMSS',
                                      fontSize=36, width=WINDOW_WIDTH)

oTimerDisplaySeconds = pygwidgets.DisplayText(window, (220, 190), '',
                                      fontSize=36, justified='right')
oTimerDisplayHHMMSS = pygwidgets.DisplayText(window, (356, 190), '',
                                      fontSize=36, justified='right')

oTimerMessage.hide()  # Na początku komunikat pozostaje ukryty.
oTimer = pyghelpers.CountUpTimer()  # Utworzenie obiektu typu Timer.


# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        # Jeżeli został kliknięty przycisk zamknięcia okna, należy wyjść z pygame i zakończyć działanie programu.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oStartButton.handleEvent(event):
            oTimer.start()  # Uruchomienie zegara.
            oStartButton.disable()
            oTimerMessage.show()
            print('Uruchomienie zegara.')

        if oStopButton.handleEvent(event):
            print('Kliknięty został przycisk Stop.')
            oTimerMessage.hide()
            oTimer.stop()
            oStartButton.enable()

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.
    timeInSeconds = oTimer.getTimeInSeconds()
    timeInHHMMSS = oTimer.getTimeInHHMMSS(2)
    oTimerDisplaySeconds.setValue(str(timeInSeconds))
    oTimerDisplayHHMMSS.setValue(timeInHHMMSS)

    # 9 - Usunięcie zawartości okna.
    window.fill(WHITE)

    # 10 - Wyświetlenie wszystkich elementów okna.
    oHeaderMessage.draw()
    oStartButton.draw()
    oStopButton.draw()
    oTimerMessage.draw()
    oTimerDisplaySeconds.draw()
    oTimerDisplayHHMMSS.draw()

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
