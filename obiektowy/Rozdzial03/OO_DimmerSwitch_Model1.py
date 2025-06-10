# Klasa DimmerSwitch.

class DimmerSwitch():
    def __init__(self, label):
        self.label = label
        self.isOn = False
        self.brightness = 0

    def turnOn(self):
        self.isOn = True
        # Włączenie światła na podanym poziomie jasności (self.brightness).

    def turnOff(self):
        self.isOn = False
        # Wyłączenie światła.

    def raiseLevel(self):
        if self.brightness < 10:
            self.brightness = self.brightness + 1

    def lowerLevel(self):
        if self.brightness > 0:
            self.brightness = self.brightness - 1

    # Dodatkowa metoda na potrzeby debugowania.
    def show(self):
        print('Label:', self.label)
        print('Czy świstło jest włączone?', self.isOn)
        print('Poziom jasności:', self.brightness)
        print()


# Kod główny.

# Tworzenie pierwszego obiektu DimmerSwitch, włączenie światła i dwukrotne zwiększenie poziomu jego jasności.
oDimmer1 = DimmerSwitch('Dimmer1')
oDimmer1.turnOn()
oDimmer1.raiseLevel()
oDimmer1.raiseLevel()

# Tworzenie pierwszego obiektu DimmerSwitch, włączenie światła i trzykrotne zwiększenie poziomu jego jasności.
oDimmer2 = DimmerSwitch('Dimmer2')
oDimmer2.turnOn()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()
oDimmer2.raiseLevel()

# Tworzenie trzeciego obiektu DimmerSwitch i wykorzystanie ustawień domyślnych.
oDimmer3 = DimmerSwitch('Dimmer3')

# Wyświetlenie informacji o poszczególnych obiektach.
oDimmer1.show()
oDimmer2.show()
oDimmer3.show()
