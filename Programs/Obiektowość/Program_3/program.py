from zasoby_klas import Klasa_pierwsza, Klasa_druga, Klasa_trzecia

obiekt_klasy_1 = Klasa_pierwsza()
obiekt_klasy_2 = Klasa_druga()

print('Atrybut klasy wywołany na rzecz klasy:')
print(Klasa_pierwsza.atrybut_klasy_1)
print()

print('Atrybut instancji wywołany na rzecz instancji:')
print(obiekt_klasy_1.atrybut_klasy_1)
print()

obiekt_klasy_3o = Klasa_trzecia()
print(obiekt_klasy_3o.podwojna_suma)
print(obiekt_klasy_3o.pomnoz_sume(8))
print('Liczbą mnożoną przez podany mnożnik była:', obiekt_klasy_3o.suma)