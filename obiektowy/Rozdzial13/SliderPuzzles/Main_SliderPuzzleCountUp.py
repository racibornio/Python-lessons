# Gra Slider Puzzle z zegarem odmierzającym czas.

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
import pygwidgets
import pyghelpers
import sys
from Game import *

# 2 - Definiowanie stałych.
WINDOW_WIDTH = 470
WINDOW_HEIGHT = 560
FRAMES_PER_SECOND = 30

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.
restartButton = pygwidgets.CustomButton(window, (320, 455),
                                        up='images/restartButtonUp.jpg',
                                        down='images/restartButtonDown.jpg',
                                        over='images/restartButtonOver.jpg')

# 5 - Inicjalizacja zmiennych.
clock = pygame.time.Clock()

timerDisplay = pygwidgets.DisplayText(window, (50, 465), '',
                                    fontSize=36, textColor=WHITE)

messageDisplay = pygwidgets.DisplayText(window, (50, 510), 'Kliknij kwadrat, aby go przesunąć.',
                                    fontSize=36, textColor=WHITE)

oGame = Game(window)  # Utworzenie głównego obiektu gry.

oCountUpTimer = pyghelpers.CountUpTimer()
oCountUpTimer.start()

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        # Sprawdzenie, czy zdarzenie dotyczy przycisku X.
        if event.type == pygame.QUIT:
            # Po wystąpieniu tego zdarzenia należy zakończyć program.
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN:
            messageDisplay.setText('')
            oGame.gotClick(event.pos)
            over = oGame.checkForWin()
            if over:
                messageDisplay.setText('Świetna robota!!!')
                oCountUpTimer.stop()

        if restartButton.handleEvent(event):
            oGame.startNewGame()
            oCountUpTimer.start()

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.
    timeToShow = oCountUpTimer.getTimeInHHMMSS()  # prawdzenie w obiekcie zegara, ile czasu upłynęło.
    timerDisplay.setValue('Czas: ' + timeToShow)  # Umieszczenie tej wartości w polu tekstowym.

    # 9 - Usunięcie zawartości okna przed jego ponownym wyświetleniem.
    window.fill(BLACK)

    # 10 - Wyświetlenie elementów okna.
    oGame.draw()  # Nakazanie grze wyświetlenia obiektu typu Game.
    restartButton.draw()

    timerDisplay.draw()  # Wyświetlenie pola tekstowego.
    messageDisplay.draw()  # Wyświetlenie komunikatu.

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
