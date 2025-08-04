class Klasa_pierwsza:


    atrybut_klasy_1 = "Atrybut klasy 1"

    def __init__(self):
        print("__init__ z 'klasa_pierwsza' załadowany")
        self.atrybut_instancji_1 = "Atrybut instancji 1"


class Klasa_druga:
    def __init__(self):
        print("__init__ z 'klasa_druga' załadowany")
        kolejnosc = 2


class Klasa_trzecia:
    a = 5
    b = 5
    suma = a + b

    def __init__(self):
        suma = self.a + self.b
        self.podwojna_suma = suma * 2


    def pomnoz_sume(self, mnoznik):
        suma = self.a + self.b
        # self.suma = self.a + self.b
        iloczyn = suma * mnoznik
        return iloczyn
    

class klasa_czwarta:
    atrybut_klasy_a = 90
    atrybut_klasy_b = 100

    def __init__(self):
        print("__init__ z 'klasa_czwarta' załadowany")