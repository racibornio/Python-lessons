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
        print('Etykieta:', self.label)
        print('Czy świstło jest włączone?', self.isOn)
        print('Poziom jasności:', self.brightness)
        print()


# Kod główny.

# Tworzenie trzech obiektów typu DimmerSwitch.
oDimmer1 = DimmerSwitch('Dimmer1')
print(type(oDimmer1))
print(oDimmer1)
print()
oDimmer2 = DimmerSwitch('Dimmer2')
print(type(oDimmer2))
print(oDimmer2)
print()
oDimmer3 = DimmerSwitch('Dimmer3')
print(type(oDimmer3))
print(oDimmer3)
print()
