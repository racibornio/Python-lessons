# Program główny przeznaczony do tworzenia potworów.

import random

class Monster():
    def __init__(self, nRows, nCols, maxSpeed):
        self.nRows = nRows  # Wymiary siatki.
        self.nCols = nCols  # Wymiary siatki.
        self.myRow = random.randrange(self.nRows) # Wybór dowolnego wiersza.
        self.myCol = random.randrange(self.nCols) # Wybór dowolnej kolumny.
        self.mySpeedX = random.randrange(-maxSpeed, maxSpeed) + 1 # Prędkość według osi X.
        self.mySpeedY = random.randrange(-maxSpeed, maxSpeed + 1) # Prędkość według osi Y.
        # Ustawienie pozostałych zmiennych egzemplarza takich jak health, power itd.

    def move(self):
        self.myRow = (self.myRow + self.mySpeedY) %  self.nRows
        self.myCol = (self.myCol + self.mySpeedX) % self.nCols


N_MONSTERS = 20
N_ROWS = 100   # To może być dowolna wartość.
N_COLS = 200   # To może być dowolna wartość.
MAX_SPEED = 4


monsterList = []  # Na początku lista jest pusta.
for i in range(N_MONSTERS):
    oMonster = Monster(N_ROWS, N_COLS, MAX_SPEED)  # Utworzenie egzemplarza typu Monster.
    monsterList.append(oMonster)  # Dodanie obiektu Monster do listy.

# Później, podczas gry...

for oMonster in monsterList:
    oMonster.move()
