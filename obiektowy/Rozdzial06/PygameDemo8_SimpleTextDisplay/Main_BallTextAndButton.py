# Demo pygame 8 - użycie klas SimpleText, SimpleButton i Ball.

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
import sys
import random
from Ball import *  # Wczytanie kodu klasy Ball.
from SimpleText import *
from SimpleButton import *

# 2 - Definiowanie stałych.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.
oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oFrameCountLabel = SimpleText(window, (60, 20),
                             'Liczba pętli wykonanych przez program: ', WHITE)
oFrameCountDisplay = SimpleText(window, (500, 20), '', WHITE)
oRestartButton = SimpleButton(window, (280, 60),
                      'images/restartUp.png', 'images/restartDown.png')
frameCounter = 0

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if oRestartButton.handleEvent(event):
            frameCounter = 0  # Kliknięto przycisk, więc licznik został wyzerowany.

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.
    oBall.update()  # Uaktualnienie obiektu piłki.
    frameCounter = frameCounter + 1  # Inkrementacja wartości w trakcie każdej klatki.
    oFrameCountDisplay.setValue(str(frameCounter))

   # 9 - Usunięcie zawartości okna przed jego ponownym wyświetleniem.
    window.fill(BLACK)

    # 10 - Wyświetlenie elementów okna.
    oBall.draw()   # Wyświetlenie obiektu piłki.
    oFrameCountLabel.draw()
    oFrameCountDisplay.draw()
    oRestartButton.draw()

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
