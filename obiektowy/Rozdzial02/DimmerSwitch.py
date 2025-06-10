# Klasa DimmerSwitch.

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





