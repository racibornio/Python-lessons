class Program_list_i_klas:
    def __init__(self, nazwa):
        self.nazwa = nazwa


lista_nazw_obiektow = []
lista_obiektow = []
nazwa_obiektu_1 = input("Podaj nazwę 1-go obiektu:")
obiekt_1 = Program_list_i_klas(nazwa_obiektu_1)
lista_nazw_obiektow.append(nazwa_obiektu_1)
lista_obiektow.append(obiekt_1)

nazwa_obiektu_2 = input("Podaj nazwę 2-go obiektu:")
obiekt_2 = Program_list_i_klas(nazwa_obiektu_2)
lista_nazw_obiektow.append(nazwa_obiektu_2)
lista_obiektow.append(obiekt_2)

print(f'Powstała lista: {lista_nazw_obiektow}.')

print([obiekt.nazwa for obiekt in lista_obiektow])