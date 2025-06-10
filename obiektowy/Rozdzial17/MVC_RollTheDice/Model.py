# Model - Rzuć kośćmi

import random
from Constants import *

SIDES_PER_DIE = 6
SIDES_PER_DIE_PLUS_ONE = SIDES_PER_DIE + 1

# Klasa Model.
class Model():
    def __init__(self):
        self.nRounds = 0
        self.rollsDict = {}
        self.percentsDict = {}

    def generateRolls(self, nRounds):
        self.nRounds = nRounds
        self.rollsDict = {}
        for total in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):  # Inicjalizacja z wartością 0.
            self.rollsDict[total] = 0

        # Dwukrotny rzut kością, zsumowanie wyników, inkrementacja wartości słownika.
        for roundNumber in range(0, self.nRounds):
            die1 = random.randrange(1, SIDES_PER_DIE_PLUS_ONE)
            die2 = random.randrange(1, SIDES_PER_DIE_PLUS_ONE)
            theSum = die1 + die2
            self.rollsDict[theSum] = self.rollsDict[theSum] + 1

        # Obliczenie wartości procentowej i jej zapisanie w słowniku.
        self.percentsDict = {}
        for rollTotal, count in self.rollsDict.items():
            thisPercent = count / self.nRounds
            self.percentsDict[rollTotal] = thisPercent

    # Widok bieżący wywołuje tę metodę i pobiera wszystkie dane.
    def getRoundsRollsPercents(self):
        return self.nRounds, self.rollsDict, self.percentsDict

    # Ta metoda nie jest teraz używana, pozostaje dostępna dla nowych widoków.
    def getNumberOfRounds(self):
        return self.nRounds

    def getRolls(self):
        return self.rollsDict

    def getPercents(self):
        return self.percentsDict
