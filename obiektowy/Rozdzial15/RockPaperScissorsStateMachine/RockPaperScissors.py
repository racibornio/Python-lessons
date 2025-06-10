# Gra „Kamień, papier, nożyce” utworzona we frameworku pygame.
# Ta gra pokazuje przykład użycia maszyny stanów.

# 1 - Importowanie pakietów.
import pygame
from pygame.locals import *
import pygwidgets
import random
import sys

# 2 Definiowanie stałych.
GRAY = (100, 100, 100)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

ROCK = 'kamień'
PAPER = 'papier'
SCISSORS = 'nożyce'

# Zdefiniowanie stałych dla trzech stanów obsługiwanych przez grę.
STATE_SPLASH = 'Splash'
STATE_PLAYER_CHOICE = 'PlayerChoice'
STATE_SHOW_RESULTS = 'ShowResults'

# 3 - Inicjalizacja środowiska pygame.
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Wczytanie zasobów: obrazy, dźwięki itd.

# Dla ekranu początkowego.
messageField = pygwidgets.DisplayText(window, (15, 25),  'Witaj w grze "Kamień, papier, nożyce"!',
                                    fontSize=50, textColor = WHITE, width = 610, justified = 'center')

rockImage = pygwidgets.Image(window, (25, 120), 'images/Rock.png')
paperImage = pygwidgets.Image(window, (225, 120), 'images/Paper.png')
scissorsImage = pygwidgets.Image(window, (425, 120), 'images/Scissors.png')

startButton = pygwidgets.CustomButton(window, (210, 300),
                                           up='images/startButtonUp.png',
                                           down='images/startButtonDown.png',
                                           over='images/startButtonHighlight.png')

# Dla ekranu rozgrywki.
rockButton = pygwidgets.CustomButton(window, (25, 120),
                                 up = 'images/Rock.png',
                                 over = 'images/RockOver.png',
                                 down = 'images/RockDown.png')

paperButton =  pygwidgets.CustomButton(window, (225, 120),
                                 up = 'images/Paper.png',
                                 over = 'images/PaperOver.png',
                                 down = 'images/PaperDown.png')

scissorButton =  pygwidgets.CustomButton(window, (425, 120),
                                 up = 'images/Scissors.png',
                                 over = 'images/ScissorsOver.png',
                                 down = 'images/ScissorsDown.png')

chooseText = pygwidgets.DisplayText(window, (15, 395), 'Wybierz!',
                                    fontSize=50, textColor = WHITE, width = 610, justified = 'center')

resultsField = pygwidgets.DisplayText(window, (20, 275), '', \
                                    fontSize=50, textColor=WHITE, width=610, justified='center')

# Dla ekranu wyników.
rpsCollectionPlayer = pygwidgets.ImageCollection(window, (50, 62),
                    {ROCK:'images/Rock.png', PAPER:'images/Paper.png', SCISSORS:'images/Scissors.png'}, '')
rpsCollectionComputer = pygwidgets.ImageCollection(window, (350, 62),
                    {ROCK:'images/Rock.png', PAPER:'images/Paper.png', SCISSORS:'images/Scissors.png'}, '')

restartButton = pygwidgets.CustomButton(window, (220, 310),
                                    up='images/restartButtonUp.png',
                                    down='images/restartButtonDown.png',
                                    over='images/restartButtonHighlight.png')

playerScoreCounter = pygwidgets.DisplayText(window, (15, 315), 'Wynik gracza:',
                                    fontSize=50, textColor = WHITE)

computerScoreCounter = pygwidgets.DisplayText(window, (300, 315), 'Wynik komputera:',
                                    fontSize=50, textColor = WHITE)

# Dźwięki.
winnerSound = pygame.mixer.Sound('sounds/ding.wav')
tieSound = pygame.mixer.Sound('sounds/push.wav')
loserSound = pygame.mixer.Sound('sounds/buzz.wav')

# 5 - Inicjalizacja zmiennych.
playerScore = 0
computerScore = 0
state = STATE_SPLASH    # Stan początkowy.

# 6 - Pętla działająca w nieskończoność.
while True:

    # 7 - Sprawdzenie pod kątem zdarzeń i ich obsługa.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if state == STATE_SPLASH:
            if startButton.handleEvent(event):
                state = STATE_PLAYER_CHOICE

        elif state == STATE_PLAYER_CHOICE:  # Pozostawienie wyboru graczowi.
            playerChoice = ''  # Wskazuje na brak wyboru.
            if rockButton.handleEvent(event):
                playerChoice = ROCK
                rpsCollectionPlayer.replace(ROCK)

            elif paperButton.handleEvent(event):
                playerChoice = PAPER
                rpsCollectionPlayer.replace(PAPER)

            elif scissorButton.handleEvent(event):
                playerChoice = SCISSORS
                rpsCollectionPlayer.replace(SCISSORS)

            if playerChoice != '':  # Gracz i komputer dokonali wyboru.
                # Komputer wybiera kroki z dostępnych elementów.
                rps = (ROCK, PAPER, SCISSORS)
                computerChoice = random.choice(rps) # Komputer dokonuje wyboru.
                rpsCollectionComputer.replace(computerChoice)

                # Sprawdzenie stanu gry.
                if playerChoice == computerChoice:  # Remis.
                    resultsField.setValue('Mamy remis!')
                    tieSound.play()

                elif playerChoice == ROCK and computerChoice == SCISSORS:
                    resultsField.setValue('Kamień tępi nożyce. Wygrałeś!')
                    playerScore = playerScore + 1
                    winnerSound.play()

                elif playerChoice == ROCK and computerChoice == PAPER:
                    resultsField.setValue('Kamień został owinięty papierem. Przegrałeś.')
                    computerScore = computerScore + 1
                    loserSound.play()

                elif playerChoice == SCISSORS and computerChoice == PAPER:
                    resultsField.setValue('Nożyce tną papier. Wygrałeś!')
                    playerScore = playerScore + 1
                    winnerSound.play()

                elif playerChoice == SCISSORS and computerChoice == ROCK:
                    resultsField.setValue('Nożyce zostały stępione przez kamień. Przegrałeś.')
                    computerScore = computerScore + 1
                    loserSound.play()

                elif playerChoice == PAPER and computerChoice == ROCK:
                    resultsField.setValue('Papier owija kamień. Wygrałeś!')
                    playerScore = playerScore + 1
                    winnerSound.play()

                elif playerChoice == PAPER and computerChoice == SCISSORS:
                    resultsField.setValue('Paper is cut by Scissors. You lose.')
                    computerScore = computerScore + 1
                    loserSound.play()

                # Wyświetlenie wyniku osiągniętego przez gracza.
                playerScoreCounter.setValue('Twój wynik: '+ str(playerScore))
                # Wyświetlenie wyniku osiągniętego przez komputer.
                computerScoreCounter.setValue('Wynik komputera: '+ str(computerScore))

                state = STATE_SHOW_RESULTS  # Zmiana stanu.

        elif state == STATE_SHOW_RESULTS:
            if restartButton.handleEvent(event):
                state = STATE_PLAYER_CHOICE  # Zmiana stanu.

        else:
            raise ValueError('Nieznany stan::', state)

    # 8 - Wykonywanie wszelkich akcji dla „danej klatki”.
    if state == STATE_PLAYER_CHOICE:
        messageField.setValue('       kamień             papier         nożyce')
    elif state == STATE_SHOW_RESULTS:
        messageField.setValue('Ty                      Komputer')

    # 9 - Usunięcie zawartości okna.
    window.fill(GRAY)

    # 10 - Wyświetlenie wszystkich elementów okna.
    messageField.draw()

    if state == STATE_SPLASH:
        rockImage.draw()
        paperImage.draw()
        scissorsImage.draw()
        startButton.draw()

    # Wyświetlenie elementów gracza.
    elif state == STATE_PLAYER_CHOICE:
        rockButton.draw()
        paperButton.draw()
        scissorButton.draw()
        chooseText.draw()

    # Wyświetlenie wyniku.
    elif state == STATE_SHOW_RESULTS:
        resultsField.draw()
        rpsCollectionPlayer.draw()
        rpsCollectionComputer.draw()
        playerScoreCounter.draw()
        computerScoreCounter.draw()
        restartButton.draw()

    else:
        raise ValueError('Nieznany stan::', state)

    # 11 - Uaktualnienie okna.
    pygame.display.update()

    # 12 - Niewielkie spowolnienie całości.
    clock.tick(FRAMES_PER_SECOND)  # Framework pygame wstrzyma na chwilę działanie.
