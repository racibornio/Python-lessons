# Klasa Sample.
class Sample():

    nObjects = 0  # To jest zmienna klasy zdefiniowana w klasie Sample.
    def __init__(self, name):
        self.name = name
        Sample.nObjects = Sample.nObjects + 1

    def howManyObjects(self):
        print('Liczba obiektów klasy Sample:', Sample.nObjects)

    def __del__(self):
        Sample.nObjects = Sample.nObjects - 1

# Utworzenie 4 obiektów.
oSample1 = Sample('A')
oSample2 = Sample('B')
oSample3 = Sample('C')
oSample4 = Sample('D')

# Usunięcie 1 obiektu.
del oSample3

# Sprawdzenie liczby obiektów.
oSample1.howManyObjects()
