import random, time, copy

WIDTH = 9
HEIGHT = 9

#utworzenie listy list przedstawiającej komórki
nextCells = []
for x in range(WIDTH):
    column = [] #utworzenie nowej kolumny
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') #dodanie komórki żywej
        else:
            column.append(' ') #dodanie komórki martwej
    nextCells.append(column) #nextCells to lista list kolumn


while True: # pętla główna programu
    print('\n\n\n\n\n') #oddzielenie poszczególnych kroków znakami nowego wiersza
    currentCells = copy.deepcopy(nextCells)

    #wyświetlenie currentCells na ekranie
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') #wyświetlenie znaku # lub spacji
        print() #wyświetalnie znaku nowego wiersza na końcu danego wiersza komórek

    #oblicznie komórek w następnym kroku na podstawie komórek bieżącego kroku
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #pobranie współrzędnych komórek sąsiadujących z daną komórką
            #'%WIDTH' gwarantuje, że wartość leftCoord zawsze będzie w przedziale od 0 do WIDTH - 1
            leftCoord = (x - 1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

        #liczba sąsiadujących żywych komórek
        numNeighbors = 0
        if currentCells[leftCoord][aboveCoord] == '#':
            numNeighbors += 1 #sąsiadująca komórka w lewym górnym rogu jest żywa
        if currentCells[x][aboveCoord] == '#':
            numNeighbors += 1 #sąsiadująca komórka na górze jest żywa
        if currentCells[rightCoord][aboveCoord] == '#':
            numNeighbors += 1 #sąsiadująca komórka w prawym górnym rogu jest żywa
        if currentCells[leftCoord][y] == '#':
            numNeighbors += 1 #sąsiadująca komórka po lewej stronie jest żywa
        if currentCells[rightCoord][y] == '#':
            numNeighbors += 1 #sąsiadująca komórka po prawej stronie jest żywa
        if currentCells[leftCoord][belowCoord] == '#':
            numNeighbors += 1 #sąsiadująca komórka w lewym dolnym rogu jest żywa
        if currentCells[x][belowCoord] == '#':
            numNeighbors += 1 #sąsiadująca komórka na dole jest żywa
        if currentCells[rightCoord][belowCoord] == '#':
            numNeighbors += 1 #sąsiadujące komórka w prawym dolnym rogu jest żywa

        #określenie stanu komórki na podstawie reguł gry
        if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
            #dwie lub trzy żywe komórki sąsiadujące oznaczają, że komórka pozostaje żywa
            nextCells[x][y] = '#'
        elif currentCells[x][y] == ' ' and numNeighbors == 3:
            #trzy żywe komórki sąsiadujące oznaczają, że komórka ożywa
            nextCells[x][y] = '#'
        else:
            #reszta komórek pozostaje martwa lub obumiera
            nextCells[x][y] = ' '
    time.sleep(1) #dodanie sekundowej przerwy, aby zminimalizować miganie ekranu