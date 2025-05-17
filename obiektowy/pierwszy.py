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


startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank':rank, 'suit':suit, 'value':thisValue + 1}
        startingDeckList.append(cardDict)
        print('Value:', thisValue)
        print('Obiekt zwrócony:', startingDeckList)
        print()