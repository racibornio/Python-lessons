# Klasa Game.

from Square import *
import random

class Game():
    START_LEFT = 35
    START_TOP = 30

    def __init__(self, window):
        self.window = window
        '''
        Plansza gry składa się z 4 wierszy i 4 kolumn - 16 kwadratów,
        z 15 obrazami (liczby od 1 do 15) oraz jednym pustym kwadratem.
        Ponieważ listy i krotki Pythona są liczone od zera, kwadraty są
        wewnętrznie ponumerowane (indeksowane) od 0 do 15, np.:
             0  1  2  3
             4  5  6  7
             8  9 10 11
            12 13 14 15
        (Kwadrat to obszar w oknie, składa się z kafelka, który może się poruszać.)

        Poniżej znajduje się słownik squareNumber:krotka.  Każda krotka zawiera wszystkie
        ruchy (sąsiedzi pionowe i poziome), pozwalające zamieniać kafle miejscami z danym kwadratem.
        Na przykład kwadrat 0 może przejść na jedynie kwadraty 1 i 4.
        '''

        LEGAL_MOVES_DICT = {
            0:(1, 4),
            1:(0, 2, 5),
            2:(1, 3, 6),
            3:(2, 7),
            4:(0, 5, 8),
            5:(1, 4, 6, 9),
            6:(2, 5, 7, 10),
            7:(3, 6, 11),
            8:(4, 9, 12),
            9:(5, 8, 10, 13),
            10:(6, 9, 11, 14),
            11:(7, 10, 15),
            12:(8, 13),
            13:(9, 12, 14),
            14:(10, 13, 15),
            15:(11, 14)}

        yPos = Game.START_TOP
        self.squaresList = []

        # Utworzenie listy obiektów typu Square.
        for row in range(0, 4):
            xPos = Game.START_LEFT
            for col in range(0, 4):
                squareNumber = (row * 4) + col
                legalMovesTuple = LEGAL_MOVES_DICT[squareNumber]
                oSquare = Square(self.window, xPos, yPos, squareNumber, legalMovesTuple)
                self.squaresList.append(oSquare)
                xPos = xPos + SQUARE_WIDTH
            yPos = yPos + SQUARE_HEIGHT

        self.soundTick = pygame.mixer.Sound('sounds/tick.wav')
        self.soundApplause = pygame.mixer.Sound('sounds/applause.wav')
        self.soundNope = pygame.mixer.Sound('sounds/nope.wav')

        self.playing = False
        self.startNewGame()

    def startNewGame(self):
        # Wszystkie kwadraty zostaną wyzerowane.
        for oSquare in self.squaresList:
            oSquare.reset()

        self.oOpenSquare = self.squaresList[STARTING_OPEN_SQUARE_NUMBER]

        for i in range(0, 200):  # Wykonanie 200 dowolnych ruchów w celu losowego ułożenia kwadratów.
            legalMovesForThisTile = self.oOpenSquare.getLegalMoves()
            nextMoveNumber = random.choice(legalMovesForThisTile)
            oSquare = self.squaresList[nextMoveNumber]

            # Zamiana miejscami losowo wybranego kwadratu i pustego.
            self.switch(oSquare, playMoveSound=False)

        self.playing = True

    def gotClick(self, clickLoc):
        if not self.playing:
            return  # Koniec gry, oczekiwanie na kliknięcie przycisku Restart.

        for oSquare in self.squaresList:
            if oSquare.clickedInside(clickLoc):
                squareNumber = oSquare.getSquareNumber()
                # print('Kliknięto myszą kwadrat numer:', squareNumber)
                legalMovesForOpenSquareTuple = self.oOpenSquare.getLegalMoves()
                legalMove = squareNumber in legalMovesForOpenSquareTuple

                if legalMove:
                    self.switch(oSquare, playMoveSound=True)
                else:  # Niedozwolony ruch (nie obok pustego kwadratu).
                    self.soundNope.play()
                return

    # Zamiana miejscami danego kwadratu i pustego.
    def switch(self, oSquareToSwitch, playMoveSound=False):
        oSquareToSwitch.switch(self.oOpenSquare)
        # Ponowne przypisanie pustego kwadratu.
        self.oOpenSquare = oSquareToSwitch

        if playMoveSound:
            self.soundTick.play()

    def checkForWin(self):
        if not self.playing:
            return False

        for oSquare in self.squaresList:
            if not oSquare.isTileInProperPlace():
                return False

        # Wszystko na odpowiednim miejscu, koniec gry.
        self.playing = False
        self.soundApplause.play()
        return True

    def getGamePlaying(self):
        return self.playing

    def stopPlaying(self):
        self.playing = False

    def draw(self):
        for oSquare in self.squaresList:
            oSquare.draw()
