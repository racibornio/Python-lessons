#mutable, ordered, iterable, cannot be a key in dictionary unless with 'frozenset'
#values can repeat
#nazwa_listy.append(wartość) -> wstawia wartość na sam koniec
#nazwa_listy = nazwa_listy + [element] -> robi to samo co linia powyżej z append()
#nazwa_listy.insert(nr_indeksu, wartość) -> wstawia wartość na podany indeks przesuwając resztę w prawo
#nazwa_listy.pop() -> usuwa ostatni indeks, ale pozwala to przypisać do zmiennej
#nazwa_listy.pop(nr_indeksu) -> usuwa wskazany indeks, ale pozwala to przypisać do zmiennej
#del nazwa_listy[nr_indeksu] -> po prostu usuwa wskazany indeks
#nazwa_listy.remove(wartość) -> usuwa pierwsze wystąpienie podanej wartości
#nazwa_listy.sort() -> sortuje listę Asc (dla intów najpierw zrzutuj)
#nazwa_listy.sort(reverse=True) -> sortuje listę Desc (dla intów najpierw zrzutuj)
#zmienna = sorted(nazwa_listy) -> tymczasowo sortuje listę Asc
#zmienna = sorted(nazwa_listy, reverse=True) -> tymczasowo sortuje listę Desc
#nazwa_listy.reverse() -> przerzuca zastaną kolejność elementów - ustawia listę od końca
#ROZSZERZANIE LISTY


from operator import index

list_of_intigers = [0, 1, 2, 3, 4, 5]
list_of_strings = ["a", "b", "c", "z", "g"]
list_of_bools = [True, True, False, True]
empty_list = []
print('Empty list', empty_list)

print(list_of_intigers)
print(list_of_intigers[0])
print(list_of_intigers[-1]) #print last item

list_of_intigers.append(6) #add an element at the end
print('6th position added', list_of_intigers)

list_of_intigers.insert(1, 0.5) #adds an element on an indicated index with an indicated value
print('new 1st position added', list_of_intigers)

del list_of_intigers[1] #deletes an indicated index
print('New 1st position deleted', list_of_intigers)

popped_value = list_of_intigers.pop() #deletes an indicated index but allows to work with an item yet
print('Last position popped', list_of_intigers)
print('Popped value', popped_value)

list_of_intigers.pop(3) #deletes an indicated index
print('3rd position popped', list_of_intigers)

value_to_remove = 4
list_of_intigers.remove(value_to_remove) #removes by the value - removes only the first occurence
print(value_to_remove, 'removed by value:', list_of_intigers)

removed_value = "c"
list_of_strings.remove(removed_value) #also allows to work with an item yet - removes only the first occurence
print(removed_value, "has been removed.")

print(list_of_strings)

list_of_lists = [ [1, 3, 5, 7, 9],
                  [2, 4, 6, 8, 0],
                  ['a', 'e', 'i', 'o', 'u'],
                  ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż'] ]

print(list_of_lists[0][0],list_of_lists[1][0],list_of_lists[2][0],list_of_lists[3][0])

#przejdź przez nad-listę i wyświetl całe pod-listy
for i in range(len(list_of_lists)):
    print('Lista:', list_of_lists[i])

#wejdź do każdej pod-listy i wypisz jej elementy
for i in range(len(list_of_lists)):
    for j in list_of_lists[i]:
        print('Element', j)

#tabliczka mnożenia
for i in range(1, 11):
    for j in range(1, 11):
        print(i, '*', j, '=', i*j)

#test mutowalności listy
mute_list = [0]
print('Initial mute_list', mute_list)
before_mutation = id(mute_list)
mute_list[0] = 1
print('mute_list after mutation', mute_list)
after_mutation = id(mute_list)
if before_mutation == after_mutation:
    print('The address has not changed - the list is a mutable structure')
else:
    print('The address has changed - the list is not a mutable structure')

#sort list Asc
list_of_strings.sort()
print('List sorted A-Z', list_of_strings)

#sort list Desc
list_of_strings.sort(reverse=True)
print('List sorted Z-A', list_of_strings)
print('List after modifications', list_of_strings)

#list sorted temporarily
temporarily_sorted = sorted(list_of_strings)
print('List temporarily sorted', temporarily_sorted)
print('List after temporary sorting', list_of_strings)
print('Sorted temporarily', sorted(list_of_strings)) #temporarily
print('Current state', list_of_strings) #previous version restored
list_of_strings.sort()
print('Restored', list_of_strings)
print('Temporarily reversed', sorted(list_of_strings, reverse=True))

#reverse() method just reverses the list - doesn't sort it!
list_of_strings.reverse()
print('Reversed with function reverse()', list_of_strings)

#jako argument z True w metodzie sort sortuje Desc
#jako metoda po prostu wyświetla w odwróconej kolejności trwale
#kolejne użycie reverse() znowu odwróci kolejność

# wypełnij pustą listę 10-ma wartościami int 1-10
list_for_data = []
for i in range(1, 11):
    list_for_data.append(i)

print('List length:', len(list_for_data))
# odczyt listy - dwa argumenty przy wywołaniu intepretowania jako index i wartość odpowiednio
for i, v in enumerate(list_for_data):
    print(i, ':', v)

for i in range(len(list_for_data)):
    list_for_data.pop()

print('List length:', len(list_for_data))

# #wariant 1 - wypełnij listę podanymi wartościami
# lista_do_wypelnienia = []
# licznik = 10
# for i in range(1, 11):
#     lista_do_wypelnienia.append(input(f'Wpisz dane jeszcze {licznik} razy'))
#     licznik -= 1
#     print('Lista teraz:', lista_do_wypelnienia)
#
# print('Cała lista to', lista_do_wypelnienia)
#
#
# #wariant 2 - wypełnij listę podanymi wartościami - szybsza
# lista_inaczej = []
# for i, e in enumerate(range(10, 0, -1)):
#     lista_inaczej.append(input(f'Wpisz dane do listy jeszcze {e} razy'))
#     print('Lista teraz:', lista_inaczej)
#     print('i:', i, 'e:', e)
#
# print('Cała lista:', lista_inaczej)


#rozszerzanie listy
lista_do_rozszerzenia = [0, 1]
print('Init', lista_do_rozszerzenia, 'id:', id(lista_do_rozszerzenia))
lista_do_rozszerzenia += [2, 3] #działa na tym samym obiekcie
print('Po instrukcji "lista_do_rozszerzenia += [2, 3]:"', lista_do_rozszerzenia, 'id:', id(lista_do_rozszerzenia))
lista_do_rozszerzenia = lista_do_rozszerzenia + [4, 5] #tworzy nowy obiekt
print('Po instrukcji "lista_do_rozszerzenia = lista_do_rozszerzenia + [4, 5]":', lista_do_rozszerzenia, 'id:', id(lista_do_rozszerzenia))
lista_do_rozszerzenia.extend([6, 7, 8]) #działa na tym samym obiekcie
print('Po instrukcji "lista_do_rozszerzenia.extend([6, 7, 8])":', lista_do_rozszerzenia, 'id:', id(lista_do_rozszerzenia))

samozapelniajaca_sie_lista_1 = list(range(1, 11))
print('Lista 10-elementowa: ', samozapelniajaca_sie_lista_1)

samozapelniajaca_sie_lista_2 = list(range(2, 21, 2))
print('Lista tylko parzystych od 1 do 20', samozapelniajaca_sie_lista_2)


lista_kwadratow_liczb = []
for i in range(1, 11):
    kwadrat_liczby = i**2
    lista_kwadratow_liczb.append(kwadrat_liczby)
    print('Kwadrat liczby', i, 'to', kwadrat_liczby)

print('Wszystkie potęgi od 1 do 10:', lista_kwadratow_liczb)
print('Wartość minimalna to:', min(lista_kwadratow_liczb))
print('Wartość maksymalna to:', max(lista_kwadratow_liczb))
print('Suma kwadratów to:', sum(lista_kwadratow_liczb))


#wycinki list
miesiace = ['Styczeń', 'Luty', 'Marzec', 'Kwiecień', 'Maj', 'Czerwiec', 'Lipiec', 'Sierpień', 'Wrzesień', 'Październik','Listopad', 'Grudzień']
print('Pierwsze 3 m-ce zapisem "miesiace[0:3]":', miesiace[0:3])
print('Pierwsze 3 m-ce zapisem "miesiace[:3]":', miesiace[:3])
print('Ostatnie 3 m-ce zapisem "miesiace[9:12]":', miesiace[9:12])
print('Ostatnie 3 m-ce zapisem "miesiace[9:]":', miesiace[9:])
print('Ostatnie 3 m-ce zapisem "miesiace[-3:]":', miesiace[-3:])


#kopiowanie całej listy
lista_do_skopiowania = [1, 2, 3]
lista_skopiowana = lista_do_skopiowania[:]
print('lista_do_skopiowania', lista_do_skopiowania)
print('lista_skopiowana', lista_skopiowana)