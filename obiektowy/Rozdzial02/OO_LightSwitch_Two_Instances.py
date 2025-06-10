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
oLightSwitch1 = LightSwitch()  # Utworzenie obiektu klasy LightSwitch.
oLightSwitch2 = LightSwitch()  # Utworzenie innego obiektu klasy LightSwitch.

#  Kod testowy.
oLightSwitch1.show()
oLightSwitch2.show()
oLightSwitch1.turnOn() # Pierwszy przełącznik jest w pozycji „włączony”.
# Na początku drugi przełącznik powinien być w pozycji „wyłączony”,
# a dzięki temu wywołaniu to staje się oczywiste.
oLightSwitch2.turnOff()
oLightSwitch1.show()
oLightSwitch2.show()

