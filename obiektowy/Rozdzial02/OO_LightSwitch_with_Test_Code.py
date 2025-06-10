# OO_LightSwitch.

class LightSwitch():
    def __init__(self):
        self.switchIsOn = False

    def turnOn(self):
        # Przełącznik w pozycji włączony.
         self.switchIsOn = True

    def turnOff(self):
        # Przełącznik w pozycji wyłączony.
         self.switchIsOn = False

    def show(self):  # Metoda dodana na potrzeby testów.
        print(self.switchIsOn)

# Kod główny.
oLightSwitch = LightSwitch()  # Utworzenie obiektu klasy LightSwitch.

# Wywołania metod.
oLightSwitch.show() # Wywołanie metody show() klasy oLightSwitch.
oLightSwitch.turnOn() # Wywołanie metody turnOn() klasy oLightSwitch.
oLightSwitch.show()
oLightSwitch.turnOff() # Wywołanie metody turnOff() klasy oLightSwitch.
oLightSwitch.show()
oLightSwitch.turnOn() # Wywołanie metody turnOn() klasy oLightSwitch.
oLightSwitch.show()
