# Scena najlepszych wyników.
import pygwidgets
import pyghelpers
from HighScoresData import *

def showCustomAnswerDialog(theWindow, theText):
    oDialogBackground = pygwidgets.Image(theWindow, (35, 450),
                                                'images/dialog.png')
    oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 480),
                                                theText, width=WINDOW_WIDTH,
                                                justified='center', fontSize=36)
    oUserInputText = pygwidgets.InputText(theWindow, (200, 550), '',
                                                fontSize=36, initialFocus=True)
    oNoButton = pygwidgets.CustomButton(theWindow, (65, 595),
                                                'images/noThanksNormal.png',
                                                over='images/noThanksOver.png',
                                                down='images/noThanksDown.png',
                                                disabled='images/noThanksDisabled.png')
    oYesButton = pygwidgets.CustomButton(theWindow, (330, 595),
                                                'images/addNormal.png',
                                                over='images/addOver.png',
                                                down='images/addDown.png',
                                                disabled='images/addDisabled.png')
    userAnswer = pyghelpers.customAnswerDialog(theWindow,
                                                oDialogBackground,
                                                oPromptDisplayText, oUserInputText,
                                                oYesButton, oNoButton)
    return userAnswer

def showCustomResetDialog(theWindow, theText):
    oDialogBackground = pygwidgets.Image(theWindow,
                                               (35, 450), 'images/dialog.png')
    oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 480),
                                                theText, width=WINDOW_WIDTH,
                                                justified='center', fontSize=36)
    oNoButton = pygwidgets.CustomButton(theWindow, (65, 595),
                                                'images/cancelNormal.png',
                                                over='images/cancelOver.png',
                                                down='images/cancelDown.png',
                                                disabled='images/cancelDisabled.png')
    oYesButton = pygwidgets.CustomButton(theWindow, (330, 595),
                                                'images/okNormal.png',
                                                over='images/okOver.png',
                                                down='images/okDown.png',
                                                disabled='images/okDisabled.png')
    choiceAsBoolean = pyghelpers.customYesNoDialog(theWindow,
                                                oDialogBackground, oPromptDisplayText,
                                                oYesButton, oNoButton)
    return choiceAsBoolean


class SceneHighScores(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        self.oHighScoresData = HighScoresData()

        self.backgroundImage = pygwidgets.Image(self.window,
                                                (0, 0),
                                                'images/highScoresBackground.jpg')

        self.namesField = pygwidgets.DisplayText(self.window, (260, 84), '',
                                                   fontSize=48, textColor=BLACK,
                                                   width=300, justified='left')
        self.scoresField = pygwidgets.DisplayText(self.window,
                                                  (25, 84), '', fontSize=48,
                                                  textColor=BLACK,
                                                  width=175, justified='right')

        self.quitButton = pygwidgets.CustomButton(self.window,
                                                  (30, 650),
                                                  up='images/quitNormal.png',
                                                  down='images/quitDown.png',
                                                  over='images/quitOver.png',
                                                  disabled='images/quitDisabled.png')

        self.backButton = pygwidgets.CustomButton(self.window,
                                                 (240, 650),
                                                 up='images/backNormal.png',
                                                 down='images/backDown.png',
                                                 over='images/backOver.png',
                                                 disabled='images/backDisabled.png')

        self.resetScoresButton = pygwidgets.CustomButton(self.window,
                                                 (450, 650),
                                                 up='images/resetNormal.png',
                                                 down='images/resetDown.png',
                                                 over='images/resetOver.png',
                                                 disabled='images/resetDisabled.png')

        self.showHighScores()

    def getSceneKey(self):
        return SCENE_HIGH_SCORES

    def enter(self, newHighScoreValue=None):
        # Metoda może być wywołana na dwa różne sposoby:
        # 1. Jeżeli wynik nie mieści się w pierwszej dziesiątce, wartością newHighScoreValue będzie None.
        # 2. Wartością newHighScoreValue jest score bieżącej gry - ten wynik mieści się w pierwszej dziesiątce.
        if newHighScoreValue is None:
            return  # Nie ma nic do zrobienia.

        self.draw() # Wyświetlenie obiektu przed wyświetleniem okna dialogowego.
        # Mamy nowy najlepszy wynik przekazany ze sceny Play.
        dialogQuestion = ('Aby zachować wynik ' +
                                 str(newHighScoreValue) + ',\n' +
                                 'podaj swoje imię:')
        playerName = showCustomAnswerDialog(self.window,
                                                                    dialogQuestion)
        if playerName is None:
            return  # Gracz kliknął przycisk Anuluj.

        # Dodanie gracza i jego wyniku na listę najlepszych wyników.
        if playerName == '':
            playerName = 'Anonim'
        self.oHighScoresData.addHighScore(playerName,
                                                            newHighScoreValue)

        # Wyświetlenie uaktualnionej listy najlepszych wyników.
        self.showHighScores()

    def showHighScores(self):
        # Pobranie imion i wyników, a następnie wyświetlenie ich w polach.
        scoresList, namesList = self.oHighScoresData.getScoresAndNames()
        self.namesField.setValue(namesList)
        self.scoresField.setValue(scoresList)

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.quitButton.handleEvent(event):
                self.quit()

            elif self.backButton.handleEvent(event):
                self.goToScene(SCENE_PLAY)

            elif self.resetScoresButton.handleEvent(event):
                confirmed = showCustomResetDialog(self.window,
                                        'Czy na pewno chcesz \nWYZEROWAĆ listę wyników?')
                if confirmed:
                    self.oHighScoresData.resetScores()
                    self.showHighScores()

    def draw(self):
        self.backgroundImage.draw()
        self.scoresField.draw()
        self.namesField.draw()
        self.quitButton.draw()
        self.resetScoresButton.draw()
        self.backButton.draw()

    def respond(self, requestID):
        if requestID == HIGH_SCORES_DATA:
            # Pochodzące ze sceny Play żądanie najlepszego i najgorszego wyniku.
            # Utworzenie słownika i jego przekazanie scenie Play.
            highestScore, lowestScore = self.oHighScoresData.getHighestAndLowest()
            return {'highest':highestScore, 'lowest':lowestScore}
