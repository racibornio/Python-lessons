# Demo pygame - tekst i przyciski

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
import sys
import random
import pygwidgets

# 2 - Definiowanie stałych.
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3
BALL_WIDTH_HEIGHT = 100

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# 5 - Inicjalizacja zmiennych.
oBall = pygwidgets.Image(window, (0, 0), 'images/ball.png')
ballLeft = 0
ballTop = 0

MAX_WIDTH = WINDOW_WIDTH - BALL_WIDTH_HEIGHT
MAX_HEIGHT = WINDOW_HEIGHT - BALL_WIDTH_HEIGHT
ballX = random.randrange(MAX_WIDTH)
ballY = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME

oBackground = pygwidgets.Image(window, (0, 0), 'images/background.jpg')

oRestartButton = pygwidgets.CustomButton(window, (500, 430),
                                        up='images/restartUp.png',
                                        down='images/restartDown.png',
                                        over='images/restartOver.png',
                                        disabled= 'images/restartDisabled.png')

oHitMeButton = pygwidgets.TextButton(window, (500, 370), 'Przycisk tekstowy')

oMessageTextA = pygwidgets.DisplayText(window, (20, 50), 'Dowolny tekst',
                                    fontSize=36, textColor=WHITE)

oMessageTextB = pygwidgets.DisplayText(window, (20, 150),
                                       'Inny dowolny tekst\nKolejny dowolny tekst\nI jeszcze więcej dowolnego tekstu',
                                       fontSize=36, textColor=WHITE, justified='center')

oUserInputA = pygwidgets.InputText(window, (20, 350), '',
                                  fontSize=24, textColor=BLACK, backgroundColor=WHITE)

oUserInputB= pygwidgets.InputText(window, (20, 430), '', width = 400,
                                  fontSize=24, textColor=WHITE, backgroundColor=BLACK)

counter = 0

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if  oRestartButton.handleEvent(event):
                counter = 0

        if  oHitMeButton.handleEvent(event):
                print('Nie naciskaj mnie')

        if oUserInputA.handleEvent(event):
            userText = oUserInputA.getText()
            print('W pierwszym polu tekstowym użytkownik wpisał:', userText)

        if oUserInputB.handleEvent(event):
            userText = oUserInputB.getText()
            print('W drugim polu tekstowym użytkownik wpisał:', userText)


    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.
    counter = counter + 1
    oMessageTextA.setValue('Oto dowolny tekst.  Licznik pętli:' + str(counter))

    ballLeft, ballRight = oBall.getLoc()

    if (ballLeft < 0) or (ballLeft + BALL_WIDTH_HEIGHT >= WINDOW_WIDTH):
        xSpeed = -xSpeed  # Odwrócenie kierunku ruchu na osi X.

    if (ballTop < 0) or (ballTop + BALL_WIDTH_HEIGHT >= WINDOW_HEIGHT):
        ySpeed = -ySpeed  # Odwrócenie kierunku ruchu na osi Y.

    # Uaktualnienie prostokąta ograniczającego piłkę, z użyciem prędkości w dwóch kierunkach.
    ballLeft = ballLeft + xSpeed
    ballTop = ballTop + ySpeed
    oBall.setLoc( (ballLeft, ballTop ))


    # 9 - Usunięcie zawartości okna przed jego ponownym wyświetleniem.
    oBackground.draw()  # Wyświetlenie obrazu tła.

    # 10 - Wyświetlenie elementów okna.
    oBall.draw()

    oRestartButton.draw()
    oHitMeButton.draw()

    oMessageTextA.draw()
    oMessageTextB.draw()

    oUserInputA.draw()
    oUserInputB.draw()

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.




