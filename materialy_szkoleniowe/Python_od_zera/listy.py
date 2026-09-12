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