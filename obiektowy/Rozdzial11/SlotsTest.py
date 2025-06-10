# Przykład standardowy wykorzystujący słownik.
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(x, y)

        # Próba utworzenia dodatkowej zmiennej egzemplarza.
        self.color = 'black'  # To powinno działać świetnie.
        print(self.color)

oPoint = Point(3, 5)


class PointWithSlots():
    # Zdefiniowanie slotów jedynie dla dwóch zmiennych egzemplarza.
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(x, y)

        # Próba utworzenia dodatkowej zmiennej egzemplarza.
        # To powinno zakończyć się niepowodzeniem.
        self.color = 'black'
        print(self.color)

oPointWithSlots = PointWithSlots(3, 5)
