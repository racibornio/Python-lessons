class Auta:

    wlasiciel_klasy = 'Patryk'

    def __init__(self, dodaj):
        print('Metoda __init__(self) zadziałała - utworzono obiekt.')
        self.rok = 2026
        staly_dodaj = 1
        nowy_rok = self.rok + dodaj + staly_dodaj
        print(f'Za {dodaj} lat będzie rok {nowy_rok}')
        pass


auto_no_1  = Auta(10)
print(f'Właścicielem klasy jest {Auta.wlasiciel_klasy} - wywołanie z klasy.')
print(f'Właścicielem klasy jest {auto_no_1.wlasiciel_klasy} - wywołane z obiektu.\n')

print(f'Jest rok {auto_no_1.rok}')