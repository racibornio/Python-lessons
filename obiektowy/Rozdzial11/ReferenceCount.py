# Przykład użycia licznika odwołań.

class Square():
    def __init__(self, width, color):
        self.width = width
        self.color = color

# Utworzenie obiektu.
oSquare1 = Square(5, 'red')
print(oSquare1)
# Wartość licznika odwołań do obiektu typu Square wynosi 1.

# Teraz jeszcze inna zmienna prowadzi do tego samego obiektu.
oSquare2 = oSquare1
print(oSquare2)
# Wartość licznika odwołań do obiektu typu Square wynosi 2.
