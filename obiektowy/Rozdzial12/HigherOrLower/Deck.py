# Klasa Deck.

import random
from Card import *

class Deck():
    SUIT_TUPLE = ('karo', 'trefl', 'kier', 'pik')
    # Ten słownik mapuje figury poszczególnych kart na ich wartości w standardowej talii kart.
    STANDARD_DICT = {'as':1, 'dwójka':2, 'trójka':3, 'czwórka':4, 'piątka':5,
                     'szóstka':6, 'siódemka':7, 'ósemka': 8, 'dziewiątka':9,
                     'dziesiątka':10, 'walet':11, 'dama':12, 'król':13}

    def __init__(self, window, rankValueDict=STANDARD_DICT):
        # rankValueDict ma wartość domyślną STANDARD_DICT. Można również
        # użyć innego słownika, np. specjalnie przeznaczonego dla gry Blackjack.
        self.startingDeckList = []
        self.playingDeckList = []
        for suit in Deck.SUIT_TUPLE:
            for rank, value in rankValueDict.items():
                oCard = Card(window, rank, suit, value)
                self.startingDeckList.append(oCard)

        self.shuffle()

    def shuffle(self):
        # Skopiowanie talii początkowej i zapisanie jej na liście talii bieżącej gry.
        self.playingDeckList = self.startingDeckList.copy()
        for oCard in self.playingDeckList:
            oCard.conceal()
        random.shuffle(self.playingDeckList)

    def getCard(self):
        if len(self.playingDeckList) == 0:
            raise IndexError('Brak kolejnych kart.')
        # Pobranie jednej karty z talii i jej zwrócenie.
        oCard = self.playingDeckList.pop()
        return oCard

    def returnCardToDeck(self, oCard):
        # Odłożenie karty z powrotem do talii.
        self.playingDeckList.insert(0, oCard)


if __name__ == '__main__':
    # Kod główny pozwalający na przetestowanie klasy Deck.

    import pygame

    # Stałe.
    WINDOW_WIDTH = 100
    WINDOW_HEIGHT = 100

    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    oDeck = Deck(window)
    for i in range(1, 53):
        oCard = oDeck.getCard()
        print('Name: ', oCard.getName(), '  Value:', oCard.getValue())


##    Kod opcjonalny definiujący talię do gry w blackjack'a.
##    print('BlackJack Deck:')
##    blackJackDict = {'as':1, 'dwójka':2, 'trójka':3, 'czwórka':4, 'piątka':5,
##               'szóstka':6, 'siódemka':7, 'ósemka': 8, 'dziewiątka':9,
##               'dziesiątka':10, 'walet':10, 'dama':10, 'król':10}
##    oBlackjackDeck = Deck(window, rankValueDict=blackJackDict)
##
##    for i in range(1, 53):
##        oCard = oBlackjackDeck.getCard()
##        print('Nazwa: ', oCard.getName(), '  Wartość:', oCard.getValue())

