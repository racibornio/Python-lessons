# Klasa Vector.
import math

class Vector():
    '''Klasa Vector przedstawiająca dwie wartości w postaci wektora,
    pozwalająca na wiele operacji matematycznych.'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, oOther):  # Metoda wywoływana dla operatora +.
        if not isinstance(oOther, Vector):
            raise TypeError('Druga wartość musi być wektorem.')
        return Vector(self.x + oOther.x, self.y + oOther.y)

    def __sub__(self, oOther):  # Metoda wywoływana dla operatora -.
        if not isinstance(oOther, Vector):
            raise TypeError('Druga wartość musi być wektorem.')
        return Vector(self.x - oOther.x, self.y - oOther.y)

    def __mul__(self, oOther):  # Metoda wywoływana dla operatora *.
        # Kod specjalny pozwalający na mnożenie wektora przez wartość skalarną.
        if isinstance(oOther, Vector):  # multiply two vectors
            return Vector((self.x * oOther.x), (self.y * oOther.y))
        elif isinstance(oOther, (int, float)):  # Mnożenie przez wartość skalarną.
            return Vector((self.x * oOther), (self.y * oOther))
        else:
            raise TypeError('Druga wartość musi być wektorem lub wartością skalarną.')

    def __abs__(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def __eq__(self, oOther):  # Metoda wywoływana dla operatora ==.
        if not isinstance(oOther, Vector):
            raise TypeError('Druga wartość musi być wektorem.')
        return (self.x == oOther.x) and (self.y == oOther.y)

    def __ne__(self, oOther):  # Metoda wywoływana dla operatora !=.
        if not isinstance(oOther, Vector):
            raise TypeError('Druga wartość musi być wektorem.')
        return not (self == oOther)  # Wywołanie metody __eq__().

    def __lt__(self, oOther):    # Metoda wywoływana dla operatora <.
        if not isinstance(oOther, Vector):
            raise TypeError('Druga wartość musi być wektorem.')
        if abs(self) < abs(oOther):  # Wywołanie metody __abs__().
            return True
        else:
            return False

    def __gt__(self, oOther):  # Metoda wywoływana dla operatora >.
        if not isinstance(oOther, Vector):
            raise TypeError('Druga wartość musi być wektorem.')
        if abs(self) > abs(oOther):  # Wywołanie metody __abs__().
            return True
        else:
            return False

    def __str__(self):
        return 'Ten wektor ma wartość (' + str(self.x) + ', ' + str(self.y) + ')'
