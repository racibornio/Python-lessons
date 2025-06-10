# Stack class

class Stack():
    '''Klasa Stack implementuje algorytm „ostatni na wejściu, pierwszy na wyjściu” LIFO.'''
    def __init__(self, startingStackAsList=None):
        if startingStackAsList is None:
            self.dataList = [ ]
        else:
            self.dataList = startingStackAsList[:]  # Utworzenie kopii.

    def push(self, item):
        self.dataList.append(item)

    def pop(self):
        if len(self.dataList) == 0:
            raise IndexError
        element = self.dataList.pop()
        return element

    def peek(self):
        # Pobranie najwyższego elementu stosu bez jego usunięcia ze stosu
        item = self.dataList[-1]
        return item

    def getSize(self):
        nElements = len(self.dataList)
        return nElements

    def show(self):
        # Wyświetlenie stosu w orientacji pionowej.
        print('Stos:')
        for value in reversed(self.dataList):
            print('   ', value)
