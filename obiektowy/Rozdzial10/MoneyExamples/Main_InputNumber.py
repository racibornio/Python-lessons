# Przykład wykorzystujący pole tekstowe dla wartości walutowych.
#
# Przykład nadpisania metod dziedziczonych po klasie InputText.
#

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
import sys
import pygwidgets
from InputNumber import *

# 2 - Definiowanie stałych.
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  # set the speed (frames per second)

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.
title = pygwidgets.DisplayText(window, (0, 40), 'Przykład użycia pól typu InputNumber i InputText',
                            fontSize=36, width=WINDOW_WIDTH, justified='center')

inputTextCaption = pygwidgets.DisplayText(window, (20, 150), 'Podaj dowolną wartość:',
                            fontSize=24, width=190, justified='right')
oInputText = pygwidgets.InputText(window, (230, 150), '', width=150)
okButtonText = pygwidgets.TextButton(window, (430, 150), 'OK')

inputNumberCaption = pygwidgets.DisplayText(window, (20, 250), 'Podaj wartość liczbową:',
                            fontSize=24, width=190, justified='right')
oInputNumber = InputNumber(window, (230, 250), '', width=150)
okButtonNumber = pygwidgets.TextButton(window, (430, 250), 'OK')


# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        # Jeżeli został kliknięty przycisk zamknięcia okna, należy wyjść z pygame i zakończyć działanie programu.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Naciśnięcie klawisza Return/Enter lub kliknięcie przycisku OK spowoduje wywołanie akcji.
        if oInputText.handleEvent(event) or okButtonText.handleEvent(event):
            theText = oInputText.getValue()
            print('Pole tekstowe zawiera następującą wartość:', theText)

        if oInputNumber.handleEvent(event) or okButtonNumber.handleEvent(event):
            try:  # Czy wystąpiły jakiekolwiek błędy.
                theText = oInputNumber.getValue()
            except ValueError:
                oInputNumber.setValue('(To nie jest liczba.)')
            else:  # Dane wejściowe są prawidłowe.
                print('Pole tekstowe zawiera następującą wartość:', theText)

    # 8  Wykonywanie wszelkich akcji dla „danej klatki”.

    # 9 - Usunięcie zawartości okna przed jego ponownym wyświetleniem.
    window.fill(BACKGROUND_COLOR)

    # 10 - Wyświetlenie wszystkich elementów ekranu.
    title.draw()
    inputTextCaption.draw()
    oInputText.draw()
    okButtonText.draw()
    inputNumberCaption.draw()
    oInputNumber.draw()
    okButtonNumber.draw()

    # 11 - Uaktualnienie ekranu.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
