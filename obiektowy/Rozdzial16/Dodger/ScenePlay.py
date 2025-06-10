#  Scena Play - scena główna gry.
from pygame.locals import *
import pygwidgets
import pyghelpers
from Player import *
from Baddies import *
from Goodies import *

def showCustomYesNoDialog(theWindow, theText):
    oDialogBackground = pygwidgets.Image(theWindow, (40, 250),
                                            'images/dialog.png')
    oPromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 290),
                                            theText, width=WINDOW_WIDTH,
                                            justified='center', fontSize=36)

    oYesButton = pygwidgets.CustomButton(theWindow, (320, 370),
                                            'images/gotoHighScoresNormal.png',
                                            over='images/gotoHighScoresOver.png',
                                            down='images/gotoHighScoresDown.png',
                                            disabled='images/gotoHighScoresDisabled.png')

    oNoButton = pygwidgets.CustomButton(theWindow, (62, 370),
                                            'images/noThanksNormal.png',
                                            over='images/noThanksOver.png',
                                            down='images/noThanksDown.png',
                                            disabled='images/noThanksDisabled.png')

    choiceAsBoolean = pyghelpers.customYesNoDialog(theWindow,
                                            oDialogBackground, oPromptDisplayText,
                                            oYesButton, oNoButton)
    return choiceAsBoolean

BOTTOM_RECT = (0, GAME_HEIGHT + 1, WINDOW_WIDTH,
                                WINDOW_HEIGHT - GAME_HEIGHT)
STATE_WAITING = 'waiting'
STATE_PLAYING = 'playing'
STATE_GAME_OVER = 'game over'

class ScenePlay(pyghelpers.Scene):

    def __init__(self, window):
        self.window = window

        self.controlsBackground = pygwidgets.Image(self.window,
                                        (0, GAME_HEIGHT),
                                        'images/controlsBackground.jpg')

        self.quitButton = pygwidgets.CustomButton(self.window,
                                        (30, GAME_HEIGHT + 90),
                                        up='images/quitNormal.png',
                                        down='images/quitDown.png',
                                        over='images/quitOver.png',
                                        disabled='images/quitDisabled.png')

        self.highScoresButton = pygwidgets.CustomButton(self.window,
                                        (190, GAME_HEIGHT + 90),
                                        up='images/gotoHighScoresNormal.png',
                                        down='images/gotoHighScoresDown.png',
                                        over='images/gotoHighScoresOver.png',
                                        disabled='images/gotoHighScoresDisabled.png')

        self.newGameButton = pygwidgets.CustomButton(self.window,
                                        (450, GAME_HEIGHT + 90),
                                        up='images/startNewNormal.png',
                                        down='images/startNewDown.png',
                                        over='images/startNewOver.png',
                                        disabled='images/startNewDisabled.png',
                                        enterToActivate=True)

        self.soundCheckBox = pygwidgets.TextCheckBox(self.window,
                                        (430, GAME_HEIGHT + 17),
                                        'Background music',
                                        True, textColor=WHITE)

        self.gameOverImage = pygwidgets.Image(self.window, (140, 180),
                                        'images/gameOver.png')

        self.titleText = pygwidgets.DisplayText(self.window,
                                        (70, GAME_HEIGHT + 17),
                                        'Wynik:                                 Najlepszy:',
                                        fontSize=24, textColor=WHITE)

        self.scoreText = pygwidgets.DisplayText(self.window,
                                        (80, GAME_HEIGHT + 47), '0',
                                        fontSize=36, textColor=WHITE,
                                        justified='right')

        self.highScoreText = pygwidgets.DisplayText(self.window,
                                        (270, GAME_HEIGHT + 47), '',
                                        fontSize=36, textColor=WHITE,
                                        justified='right')

        pygame.mixer.music.load('sounds/background.mid')
        self.dingSound = pygame.mixer.Sound('sounds/ding.wav')
        self.gameOverSound = pygame.mixer.Sound('sounds/gameover.wav')

        # Tworzenie obiektów.
        self.oPlayer = Player(self.window)
        self.oBaddieMgr = BaddieMgr(self.window)
        self.oGoodieMgr = GoodieMgr(self.window)

        self.highestHighScore = 0
        self.lowestHighScore = 0
        self.backgroundMusic = True
        self.score = 0
        self.playingState = STATE_WAITING

    def getSceneKey(self):
        return SCENE_PLAY

    def enter(self, data):
        self.getHiAndLowScores()

    def getHiAndLowScores(self):
        # Pobranie ze sceny wyników słownika wyników,
        # który ma taką postać:
        #  {'highest': highestScore, 'lowest': lowestScore}
        infoDict = self.request(SCENE_HIGH_SCORES, HIGH_SCORES_DATA)
        self.highestHighScore = infoDict['highest']
        self.highScoreText.setValue(self.highestHighScore)
        self.lowestHighScore = infoDict['lowest']

    def reset(self):   # Rozpoczęcie nowej gry.
        self.score = 0
        self.scoreText.setValue(self.score)
        self.getHiAndLowScores()

        # Nakazanie menedżerom wyzerowania się.
        self.oBaddieMgr.reset()
        self.oGoodieMgr.reset()

        if self.backgroundMusic:
            pygame.mixer.music.play(-1, 0.0)
        self.newGameButton.disable()
        self.highScoresButton.disable()
        self.soundCheckBox.disable()
        self.quitButton.disable()
        pygame.mouse.set_visible(False)

    def handleInputs(self, eventsList, keyPressedList):
        if self.playingState == STATE_PLAYING:
            return  # Ignorowanie zdarzeń przycisków podczas gry.

        for event in eventsList:
            if self.newGameButton.handleEvent(event):
                self.reset()
                self.playingState = STATE_PLAYING

            if self.highScoresButton.handleEvent(event):
                self.goToScene(SCENE_HIGH_SCORES)

            if self.soundCheckBox.handleEvent(event):
                self.backgroundMusic = self.soundCheckBox.getValue()

            if self.quitButton.handleEvent(event):
                self.quit()

    def update(self):
        if self.playingState != STATE_PLAYING:
            return  # Aktualizacja jedynie podczas gry.

        # Przeniesienie obiektu gracza do położenia wskazywanego przez kursor
        # myszy oraz pobranie prostokąta ograniczającego obiekt gracza.
        mouseX, mouseY = pygame.mouse.get_pos()
        playerRect = self.oPlayer.update(mouseX, mouseY)

        # Nakazanie egzemplarzowi typu GoodieMgr przesunięcia wszystkich obiektów postaci zielonych.
        # Zwrot liczby obiektów postaci zielonych, które zetknęły się z obiektem gracza.
        nGoodiesHit = self.oGoodieMgr.update(playerRect)
        if nGoodiesHit > 0:
            self.dingSound.play()
            self.score = self.score + (nGoodiesHit * POINTS_FOR_GOODIE)

        # Nakazanie egzemplarzowi typu BaddieMgr przesunięcia wszystkich obiektów postaci czerwonych.
        # Zwrot liczby obiektów postaci czerwonych, które spadły poza dolną krawędź okna.
        nBaddiesEvaded  = self.oBaddieMgr.update()
        self.score = self.score + (nBaddiesEvaded * POINTS_FOR_BADDIE_EVADED)

        self.scoreText.setValue(self.score)

        # Sprawdzenie, czy gracz zetknął się z jakimkolwiek obiektem postaci czerwonej lub zielonej.
        if self.oBaddieMgr.hasPlayerHitBaddie(playerRect):
            pygame.mouse.set_visible(True)
            pygame.mixer.music.stop()

            self.gameOverSound.play()
            self.playingState = STATE_GAME_OVER
            self.draw()  # Wymuszenie wyświetlenia komunikatu informującego o końcu gry.

            if self.score > self.lowestHighScore:
                scoreString = 'Twój wynik: ' + str(self.score) + '\n'
                if self.score > self.highestHighScore:
                    dialogText = (scoreString +
                                       'jest jednym z 10 najlepszych, GRATULACJE!')
                else:
                    dialogText = (scoreString +
                                      'trafia na listę najlepszych wyników.')

                result = showCustomYesNoDialog(self.window, dialogText)
                if result: # Nawigacja.
                    self.goToScene(SCENE_HIGH_SCORES, self.score)

            self.newGameButton.enable()
            self.highScoresButton.enable()
            self.soundCheckBox.enable()
            self.quitButton.enable()

    def draw(self):
        self.window.fill(BLACK)

        # Nakazanie menedżerom wyświetlenia obiektów postaci czerwonych i zielonych.
        self.oBaddieMgr.draw()
        self.oGoodieMgr.draw()

        # Nakazanie wyświetlenia obiektu przedstawiającego gracza.
        self.oPlayer.draw()

        # Wyświetlenie informacji na dole okna gry.
        self.controlsBackground.draw()
        self.titleText.draw()
        self.scoreText.draw()
        self.highScoreText.draw()
        self.soundCheckBox.draw()
        self.quitButton.draw()
        self.highScoresButton.draw()
        self.newGameButton.draw()

        if self.playingState == STATE_GAME_OVER:
            self.gameOverImage.draw()

    def leave(self):
        pygame.mixer.music.stop()
