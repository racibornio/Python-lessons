#  Przykład wykorzystujący wartości pieniężne.
#
#  Przykład nadpisania metod dziedziczonych po klasach DisplayText i InputText.

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
import sys
import pygwidgets
from DisplayMoney import *
from InputNumber import *

# 2 - Definiowanie stałych.
BLACK = (0, 0, 0)
BLACKISH = (10, 10, 10)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (0, 180, 180)
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.
title = pygwidgets.DisplayText(window, (0, 40),
                'Przykład użycia pól typu InputNumber i DisplayMoney',
                fontSize=36, width=WINDOW_WIDTH, justified='center')

inputCaption = pygwidgets.DisplayText(window, (20, 150),
                'Podaj wartość pieniężną:', fontSize=24,
                width=250, justified='right')
inputField = InputNumber(window, (300, 150), '', width=150, initialFocus=True)
okButton = pygwidgets.TextButton(window, (530, 150), 'OK')

outputCaption1 = pygwidgets.DisplayText(window, (20, 300),
                'Wartość w dolarach i centach:', fontSize=24,
                width=250, justified='right')
moneyField1 = DisplayMoney(window, (300, 300), '', textColor=BLACK,
                backgroundColor=WHITE, width=150)

outputCaption2 = pygwidgets.DisplayText(window, (20, 400),
                'Wartość tylko w dolarach:', fontSize=24,
                width=250, justified='right')
moneyField2 = DisplayMoney(window, (300, 400), '', textColor=BLACK,
                backgroundColor=WHITE, width=150,
                showCents=False)
# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        # Jeżeli został kliknięty przycisk zamknięcia okna, należy wyjść z pygame i zakończyć działanie programu.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Naciśnięcie klawisza Return/Enter lub kliknięcie przycisku OK spowoduje wywołanie akcji.
        if inputField.handleEvent(event) or okButton.handleEvent(event):
            try:
                theValue = inputField.getValue()
            except ValueError:  # Wszelkie pozostałe błędy.
                inputField.setValue('(To nie jest liczba.)')
            else:  # Dane wejściowe są prawidłowe.
                theText = str(theValue)
                moneyField1.setValue(theText)
                moneyField2.setValue(theText)

    # 8  Wykonywanie wszelkich akcji dla „danej klatki”.

    # 9 - Usunięcie zawartości okna.
    window.fill(BACKGROUND_COLOR)

    # 10 - Wyświetlenie wszystkich elementów okna.
    title.draw()
    inputCaption.draw()
    inputField.draw()
    okButton.draw()
    outputCaption1.draw()
    moneyField1.draw()
    outputCaption2.draw()
    moneyField2.draw()

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
