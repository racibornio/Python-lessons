# HigherOrLower

import random

# Stałe przedstawiające karty.
SUIT_TUPLE = ('pik', 'kier', 'trefl', 'karo')
RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'walet', 'dama', 'król')

NCARDS = 8

# Przekazanie talii. Wartością zwrotną funkcji jest losowo wybrana karta z talii.
def getCard(deckListIn):
    thisCard = deckListIn.pop() # Pobranie jednej karty z góry talii i jej zwrot.
    return thisCard

# Przekazanie talii. Wartością zwrotną funkcji jest talia, w której karty są ułożone losowo.
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # Utworzenie kopii talii początkowej.
    random.shuffle(deckListOut)
    return deckListOut

# Kod główny programu.
print('Witaj w grze Higher or Lower.')
print('Musisz odgadnąć, czy następna wyświetlona karta będzie miała wartość większą czy mniejszą od aktualnej karty.')
print('Jeżeli zgadniesz, zdobywasz 20 punktów. W przeciwnym razie tracisz 15 punktów.')
print('Na początek masz 50 punktów.')
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:  # Możliwych jest kilka rund gry.
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit = currentCardDict['suit']
    print('Pierwsza widoczna karta to:', currentCardRank + ' of ' + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):   # Jedna gra z tych wielu kart.
        answer = input('Jaka będzie następna karta: większa czy mniejsza niż' +
                       currentCardRank + currentCardSuit + '? (wpisz w lub m: ')
        answer = answer.casefold()  # Wymuszenie użycia małych liter.
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']
        print('Następna karta to', nextCardRank, nextCardSuit)

        if answer == 'w':
            if nextCardValue > currentCardValue:
                print('Masz rację, karta miała większą wartość.')
                score = score + 20
            else:
                print('Niestety karta nie miała większej wartości.')
                score = score - 15

        elif answer == 'm':
            if nextCardValue < currentCardValue:
                score = score + 20
                print('Masz rację, karta miała niższą wartość.')

            else:
                score = score - 15
                print('Niestety karta nie miała niższej wartości.')

        print('Twój wynik:', score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue  # Nie potrzebujemy bieżącej karty.

    goAgain = input('Naciśnij ENTER, aby zagrać ponownie. "k" kończy grę: ')
    if goAgain == 'k':
        break

print('Żegnaj!')










