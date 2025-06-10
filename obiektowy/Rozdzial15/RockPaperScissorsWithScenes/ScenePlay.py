# Scena Play.
# Gracz wybiera jeden element spośród trzech: kamień, papier, nożyce.

import pygwidgets
import pyghelpers
import pygame
from Constants import *
import random

class ScenePlay(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        self.RPSTuple = (ROCK, PAPER, SCISSORS)

        self.titleField = pygwidgets.DisplayText(self.window, (15, 40), '    kamień               papier          nożyce',
                                              fontSize=50, textColor=WHITE, width=610, justified='center')

        self.messageField = pygwidgets.DisplayText(self.window, (30, 395), 'Wybierz!',
                                              fontSize=50, textColor=WHITE, width=610, justified='center')

        self.rockButton = pygwidgets.CustomButton(self.window, (25, 120),
                                             up="images/Rock.png",
                                             over="images/RockOver.png",
                                             down="images/RockDown.png")

        self.paperButton = pygwidgets.CustomButton(self.window, (225, 120),
                                              up="images/Paper.png",
                                              over="images/PaperOver.png",
                                              down="images/PaperDown.png")

        self.scissorButton = pygwidgets.CustomButton(self.window, (425, 120),
                                                up="images/Scissors.png",
                                                over="images/ScissorsOver.png",
                                                down="images/ScissorsDown.png")

    def getSceneKey(self):
        return SCENE_PLAY

    def handleInputs(self, eventsList, keyPressedList):
        playerChoice = None

        for event in eventsList:
            if self.rockButton.handleEvent(event):
                playerChoice = ROCK

            if self.paperButton.handleEvent(event):
                playerChoice = PAPER

            if self.scissorButton.handleEvent(event):
                playerChoice = SCISSORS

            if playerChoice is not None:  # Gracz dokonał wyboru.
                computerChoice = random.choice(self.RPSTuple)  # Komputer dokonuje wyboru.
                dataDict = {'player': playerChoice, 'computer': computerChoice}
                self.goToScene(SCENE_RESULTS, dataDict)  # Przejście na scenę Results.

    # Nie ma potrzeby definiowania metody update(), ta dziedziczona po klasie bazowej domyślnie nie wykonuje żadnych zadań.

    def draw(self):
        self.window.fill(GRAY)
        self.titleField.draw()
        self.rockButton.draw()
        self.paperButton.draw()
        self.scissorButton.draw()
        self.messageField.draw()

