# Klasa HighScoresData.
from Constants import *
from pathlib import Path
import json

class HighScoresData():
    """Dane pliku są przechowywane jako lista list zapisana w formacie JSON.
    Każda lista składa się z imienia gracza i osiągniętego przez niego wyniku:
        [[imię, wynik], [imię, wynik], [imię, wynik] ...]
    W tej klasie wszystkie wyniki są przechowywane na liście self.scoresList.
    Lista jest w kolejności malejącej wyników, od najlepszego do najgorszego.
    """
    def __init__(self):
        self.BLANK_SCORES_LIST = N_HIGH_SCORES * [['-----', 0]]
        self.oFilePath = Path('HighScores.json')

        # Próba otworzenia pliku danych i wczytania informacji.
        try:
            data = self.oFilePath.read_text()
        except FileNotFoundError:  # Brak pliku, zdefiniowanie pustej listy wyników i jej zapisanie.
            self.resetScores()
            return

        # Plik istnieje, dane zostaną wczytane z pliku w formacie JSON.
        self.scoresList = json.loads(data)

    def addHighScore(self, name, newHighScore):
        # Znalezienie odpowiedniego miejsca na dodanie nowego z najlepszych wyników.
        placeFound = False
        for index, nameScoreList in enumerate(self.scoresList):
            thisScore = nameScoreList[1]
            if newHighScore > thisScore:
                # Wstawienie w odpowiednim miejscu i usunięcie ostatniego elementu listy.
                self.scoresList.insert(index, [name, newHighScore])
                self.scoresList.pop(N_HIGH_SCORES)
                placeFound = True
                break
        if not placeFound:
            return  # Wynik nie mieści się na liście najlepszych.

        # Zapisanie uaktualnionej listy najlepszych wyników.
        self.saveScores()

    def saveScores(self):
        scoresAsJson = json.dumps(self.scoresList)
        self.oFilePath.write_text(scoresAsJson)

    def resetScores(self):
        self.scoresList = self.BLANK_SCORES_LIST.copy()
        self.saveScores()

    def getScoresAndNames(self):
        namesList = []
        scoresList = []
        for nameAndScore in self.scoresList:
            thisName = nameAndScore[0]
            thisScore = nameAndScore[1]
            namesList.append(thisName)
            scoresList.append(thisScore)

        return scoresList, namesList

    def getHighestAndLowest(self):
        # Element 0 zawiera najlepszy wynik, a element -1 najgorszy.
        highestEntry = self.scoresList[0]
        lowestEntry = self.scoresList[-1]
        # Pobranie wyniku (drugi element, czyli o indeksie 1) każdej podlisty.
        highestScore = highestEntry[1]
        lowestScore = lowestEntry[1]
        return highestScore, lowestScore

