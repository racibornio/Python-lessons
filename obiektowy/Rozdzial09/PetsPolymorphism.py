# Polimorfizm u zwierząt.
# Trzy klasy, każda z inną metodą "daj głos" - speak().

class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, 'mówi: hau, hau, hau!')

class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, 'mówi: miiiaaaau')

class Bird():
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, 'mówi: ćwir, ćwir')

oDog1 = Dog('Rover')
oDog2 = Dog('Fido')
oCat1 = Cat('Fluffy')
oCat2 = Cat('Spike')
oBird = Bird('Big Bird')

petsList = [oDog1, oDog2, oCat1, oCat2, oBird]

# Wysłanie tej samej wiadomości (wywołanie tej samej metody) do wszystkich zwierząt.
for oPet in petsList:
    oPet.speak()
