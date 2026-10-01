# Utworzenie pustej listy
lista_edukacyjna = []
print(f'Pusta lista edukacyjna: {lista_edukacyjna}\n')

# Dodanie elementów do listy
lista_edukacyjna.append('a')
lista_edukacyjna.append('b')
print(f'Lista edukacyjna: {lista_edukacyjna}\n')

# Dodanie kolejnego elementu do listy - append() na końcu listy
lista_edukacyjna.append('c')
print(f'Lista edukacyjna po dodaniu kolejnego elementu: {lista_edukacyjna}\n')

# Dodanie elementu do listy - insert() w określonym miejscu
# .insert(index, element)
lista_edukacyjna.insert(0, '_')
print(f'Lista edukacyjna po dodaniu elementu w określonym miejscu: {lista_edukacyjna}\n')

lista_edukacyjna.insert(2, 'ą')
print(f'Lista edukacyjna po dodaniu elementu w określonym miejscu: {lista_edukacyjna}\n')


# Lista liczb całkowitych
lista_nr_1 = [1, 2, 3, 4, 5]
print(f'Lista nr 1: {lista_nr_1}\n')
print(f'Pierwszy element listy: {lista_nr_1[0]}\n')
print(f'Ostatni element listy: {lista_nr_1[-1]}\n')

# Lista liter
lista_nr_2 = ['a', 'b', 'c', 'd', 'e']
print(f'Lista nr 2: {lista_nr_2}\n')
print(f'Pierwszy element listy: {lista_nr_2[0]}\n')
print(f'Ostatni element listy: {lista_nr_2[-1]}\n')

# Wypełnianie listy pustej i poddanie jej modyfikacji - nadpisywaniu
lista_do_zmiany = []
lista_do_zmiany.append(1)
lista_do_zmiany.append(2)
print(f'Lista do zmiany: {lista_do_zmiany}\n')
lista_do_zmiany[0] = 'a'
lista_do_zmiany[1] = 'b'
print(f'Lista do zmiany po zmianach: {lista_do_zmiany}\n')
lista_do_zmiany.insert(0, '_')
print(f'Lista do zmiany po wstawieniu elementu: {lista_do_zmiany}\n')


# Usuwanie po wskazanym indeksie - wypada z pamięci
lista_do_usuwania = [1, 2, 3, 4, 5]
print(f'Lista do usuwania: {lista_do_usuwania}\n')
del lista_do_usuwania[0]
print(f'Lista po "del lista_do_usuwania[0]": {lista_do_usuwania}\n')
del lista_do_usuwania[1]
print(f'Lista po "del lista_do_usuwania[1]": {lista_do_usuwania}\n')
del lista_do_usuwania[-1]
print(f'Lista po "del lista_do_usuwania[-1]": {lista_do_usuwania}\n')

# Usuwanie ostatniego lub wskazanego elementu - można przechwycić do pamięci jako zmienną
lista_do_usuwania = [1, 2, 3, 4, 5]
print(f'Lista do usuwania: {lista_do_usuwania}\n')
lista_do_usuwania.pop()
print(f'Lista po "lista_do_usuwania.pop()": {lista_do_usuwania}\n')
lista_do_usuwania.pop(-1)
print(f'Lista po "lista_do_usuwania.pop(-1)": {lista_do_usuwania}\n')
lista_do_usuwania.pop(1)
print(f'Lista po "lista_do_usuwania.pop(1)": {lista_do_usuwania}\n')
usuniety_element = lista_do_usuwania.pop()
print(f'Usunięty element: {usuniety_element}\n')
print(f'Lista: {lista_do_usuwania}\n')

# Usuwanie po wartości - pierwszym wystąpieniu - wypada z pmięci
lista_do_usuwania = [1, 2, 3, 4, 5]
print(f'Lista do usuwania: {lista_do_usuwania}\n')
lista_do_usuwania.remove(3)
print(f'Lista po "lista_do_usuwania.remove(3)": {lista_do_usuwania}\n')


# Lista nieposortowana - do posortowania trwale
lista_do_posortowania = [5, 2, 1, 4, 3]
print(f'Lista do posortowania: {lista_do_posortowania}\n')
lista_do_posortowania.sort()
print(f'Lista posortowana trwale po "lista_do_posortowania.sort()": {lista_do_posortowania}\n')

# Lista nieposortowana - do posortowania tymczasowo
lista_do_posortowania = [5, 2, 1, 4, 3]
sorted(lista_do_posortowania)
print(f'Lista posortowana tymczasowo - czy na pewno?: {lista_do_posortowania}\n')
print(f'Lista posortowana tymczasowo - tym razem skutecznie; musi być przekazana jako argument: "sorted(lista_do_posortowania)": {sorted(lista_do_posortowania)}\n')
print(f'I od razu odczyt - lista nie została posortowana trwale: {lista_do_posortowania}\n')

# PROGRAM

print('ZACZYNAMY PROGRAM\n')
lista_programu = []
while True:
    element = input("Wpisz coś lub wpisz 'koniec' aby zakończyć: ")
    if element == 'koniec':
        break
    lista_programu.append(element)
    print(f'Lista programu: {lista_programu}')
    print(f'Posortowana lista programu: {sorted(lista_programu)}\n')

print(f'Lista programu: {lista_programu}\n')

# Odwrotne sortowanie listy
lista_do_odwrotnego_sortowania = [5, 2, 1, 4, 3]
print(f'Lista do odwrotnego sortowania: {lista_do_odwrotnego_sortowania}')
print(f'Poniższy efekt uzyskano kodem: "sorted(lista_do_odwrotnego_sortowania, reverse=True)"')
print(f'Lista do odwrotnego sortowania: {sorted(lista_do_odwrotnego_sortowania, reverse=True)}')
print(f'Następnie lista jest ponownie nieposortowana:')
print(f'Lista do odwrotnego sortowania: {lista_do_odwrotnego_sortowania}\n')

# Odwrócenie listy - bez sortowania rosnąco po drodze!
print(f'Listę można też odwrócić/zawrócić bez jej uprzedniego sortowania: "lista_do_odwrotnego_sortowania.reverse()"')
lista_do_odwrotnego_sortowania.reverse()
print(f'Lista po odwróceniu: {lista_do_odwrotnego_sortowania}')
print(f'Lista po odwróceniu: {lista_do_odwrotnego_sortowania}')

# Iteracja po liście - wyświetlenie elementów listy w pętli for
print(f'Iteracja po liście - wyświetlenie elementów listy w pętli for:')
for element in lista_do_odwrotnego_sortowania:
    print(f'Element listy: {element}')

# Utworzenie nowej listy
print(f'### Utworzenie nowej listy ###')

elementy = []
for value in range(6, 11):
    elementy.append(value)
    print(f'Dodano {value}.')

print(f'Nowa lista: {elementy}')

liczby_parzyste = list(range(0, 11, 2))
liczby_nieparzyste = list(range(1, 11, 2))
print(f'Lista liczb parzystych: {liczby_parzyste}')
print(f'Lista liczb nieparzystych: {liczby_nieparzyste}\n')

lista_kwadratow = []
for item in range(1, 11):
    lista_kwadratow.append(item ** 2)
    print(f'Kwadrat liczty {item} to {item ** 2}.')

print(f'Lista kwadratów: {lista_kwadratow}')
print(f'Najmniejszy element listy kwadratów: {min(lista_kwadratow)}')
print(f'Największy element listy kwadratów: {max(lista_kwadratow)}')
print(f'Suma elementów listy kwadratów: {sum(lista_kwadratow)}\n')

# Lista składana
print(f'### Lista składana ###')
lista_skladana = [item*item for item in range(1, 11)]
print(f'Lista składana: {lista_skladana}\n')

lista_probna = []
for item in range(10):
    if item % 2 == 0:
        lista_probna.append(item*item)
    else:
        0

print(f'Lista próbna: {lista_probna}.')


nowa_lista = []
[nowa_lista.append(item*item) if item % 2 == 0 else 0 for item in range(10)]
print(f'Nowa lista: {nowa_lista}.')

taka_lista = [item*item if item % 2 == 0 else 0 for item in range(10)]
print(f'Lista z wyrażenia złożonego: {taka_lista}.\n')

lista_do_wyboru = ['P', 'W', 'Ś', 'C', 'P', 'S', 'N']
print(f'Lista: {lista_do_wyboru}')
print(f'Wybrane: {lista_do_wyboru[0:2]}')
print(f'Wybrane: {lista_do_wyboru[2:4]}')
print(f'Wybrane: {lista_do_wyboru[:3]}')
print(f'Wybrane: {lista_do_wyboru[4:]}\n')

print(f'Indeks dnia "wtorek": {lista_do_wyboru.index(('W'))}\n')
print(f'Ile razy dzień na "P"? -> {lista_do_wyboru.count(('P'))}\n')

print(f'Dni roboce to: {[lista_do_wyboru[i] for i in range(5)]}')
print(f'Dni wolne to {[lista_do_wyboru[i] for i in range(5, 7, 1)]}\n')
print(f'Co 2-gi dzień: {lista_do_wyboru[::2]}')
print(f'Tydzień od końca: {lista_do_wyboru[::-1]}\n')
print(f'dir: {dir(lista_do_wyboru)}')
print(f'help: {help(lista_do_wyboru)}\n')

# Kopiowanie listy
lista_1 = [1, 2, 3]
lista_2 = lista_1

lista_2.append(4)
print(f'lista_1 jest taka sama jak lista_2, choć to do lista_2 dodany został element: {lista_1}\n')

print(f'Poprawnym sposobem kopiowania list nie jest przyrównywanie do siebie zmiennych, tylko dawanie całego wycinka: lista_3 = lista_4[:].')
lista_3 = [0, 9, 8]
lista_4 = lista_3[:]
lista_4.append(-1)
print(f'lista_3: {lista_3}')
print(f'lista_4: {lista_4} - lista_3 nie została zmieniona.\n')