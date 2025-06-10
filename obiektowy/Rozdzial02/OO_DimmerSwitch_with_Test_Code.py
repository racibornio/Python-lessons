# Klasa DimmerSwitch razem z kodem testowym.

class DimmerSwitch():
    def __init__(self):
        self.switchIsOn = False
        self.brightness = 0

    def turnOn(self):
        self.switchIsOn = True

    def turnOff(self):
        self.switchIsOn = False

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    # Dodatkowa metoda na potrzeby debugowania.
    def show(self):
        print('Czy światło jest włączone?', self.switchIsOn)
        print('Poziom jasności:', self.brightness)

# Kod główny.
oDimmer = DimmerSwitch()

# Włączenie światła i pięciokrotne podniesienie poziomu jego jasności.
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()

# Dwukrotne obniżenie poziomu jasności światła i jego wyłączenie.
oDimmer.lowerLevel()
oDimmer.lowerLevel()
oDimmer.turnOff()
oDimmer.show()

# Włączenie światła i trzykrotne podniesienie poziomu jego jasności.
oDimmer.turnOn()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.raiseLevel()
oDimmer.show()
