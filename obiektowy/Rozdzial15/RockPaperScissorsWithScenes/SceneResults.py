# Scena Results.
# Graczowi są wyświetlane wyniki bieżącej rundy.

import pygwidgets
import pyghelpers
import pygame
from Constants import *

class SceneResults(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        self.playerScore = 0
        self.computerScore = 0

        self.rpsCollectionPlayer = pygwidgets.ImageCollection(
                                window, (50, 62),
                                {ROCK: 'images/Rock.png',
                                PAPER: 'images/Paper.png',
                                SCISSORS: 'images/Scissors.png'}, '')
        self.rpsCollectionComputer = pygwidgets.ImageCollection(
                                window, (350, 62),
                                {ROCK: 'images/Rock.png',
                                PAPER: 'images/Paper.png',
                                SCISSORS: 'images/Scissors.png'}, '')

        self.youComputerField = pygwidgets.DisplayText(
                                window, (22, 25),
                                'Ty                      Komputer',
                                fontSize=50, textColor=WHITE, width=610, justified='center')

        self.resultsField = pygwidgets.DisplayText(
                                self.window, (20, 275), '',
                                fontSize=50, textColor=WHITE,
                                width=610, justified='center')

        self.restartButton = pygwidgets.CustomButton(
                                self.window, (220, 310),
                                up='images/restartButtonUp.png',
                                down='images/restartButtonDown.png',
                                over='images/restartButtonHighlight.png')

        self.playerScoreCounter = pygwidgets.DisplayText(
                                self.window, (86, 315), 'Wynik:',
                                fontSize=50, textColor=WHITE)

        self.computerScoreCounter = pygwidgets.DisplayText(
                                self.window, (384, 315), 'Wynik:',
                                fontSize=50, textColor=WHITE)
        # Dźwięki.
        self.winnerSound = pygame.mixer.Sound("sounds/ding.wav")
        self.tieSound = pygame.mixer.Sound("sounds/push.wav")
        self.loserSound = pygame.mixer.Sound("sounds/buzz.wav")

    def getSceneKey(self):
        return SCENE_RESULTS

    def enter(self, data):
        # data to słownik (pochodzący ze sceny Play), który ma taką postać:
        #      {'player':playerChoice, 'computer':computerChoice}
        playerChoice = data['player']
        computerChoice = data['computer']

        # Set the player and computer images
        self.rpsCollectionPlayer.replace(playerChoice)
        self.rpsCollectionComputer.replace(computerChoice)

        # Przygotowanie obrazów elementów wybranych przez gracza i komputer.
        if playerChoice == computerChoice:
            self.resultsField.setValue("Mamy remis!")
            self.tieSound.play()

        elif playerChoice == ROCK and computerChoice == SCISSORS:
            self.resultsField.setValue("Kamień tępi nożyce. Wygrałeś!")
            self.playerScore = self.playerScore + 1
            self.winnerSound.play()

        elif playerChoice == ROCK and computerChoice == PAPER:
            self.resultsField.setValue("Kamień został owinięty papierem. Przegrałeś.")
            self.computerScore = self.computerScore + 1
            self.loserSound.play()

        elif playerChoice == SCISSORS and computerChoice == PAPER:
            self.resultsField.setValue("Nożyce tną papier. Wygrałeś!")
            self.playerScore = self.playerScore + 1
            self.winnerSound.play()

        elif playerChoice == SCISSORS and computerChoice == ROCK:
            self.resultsField.setValue("Nożyce zostały stępione przez kamień. Przegrałeś.")
            self.computerScore = self.computerScore + 1
            self.loserSound.play()

        elif playerChoice == PAPER and computerChoice == ROCK:
            self.resultsField.setValue("Papier owija kamień. Wygrałeś!")
            self.playerScore = self.playerScore + 1
            self.winnerSound.play()

        elif playerChoice == PAPER and computerChoice == SCISSORS:
            self.resultsField.setValue("Papier został przecięty przez nożyce. Przegrałeś.")
            self.computerScore = self.computerScore + 1
            self.loserSound.play()

        # Wyświetlenie wyników osiągniętych przez obu graczy.
        self.playerScoreCounter.setValue(
                               'Wynik: ' + str(self.playerScore))
        self.computerScoreCounter.setValue(
                               'Wynik: ' + str(self.computerScore))

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.restartButton.handleEvent(event):
                self.goToScene(SCENE_PLAY)

    # Nie ma potrzeby definiowania metody update(), ponieważ ta
    # dziedziczona po klasie bazowej domyślnie nie wykonuje żadnych zadań.

    def draw(self):
        self.window.fill(OTHER_GRAY)
        self.youComputerField.draw()
        self.resultsField.draw()
        self.rpsCollectionPlayer.draw()
        self.rpsCollectionComputer.draw()
        self.playerScoreCounter.draw()
        self.computerScoreCounter.draw()
        self.restartButton.draw()
