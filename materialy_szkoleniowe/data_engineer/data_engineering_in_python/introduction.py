print("Introduction to Data Engineering in Python\n")

########### LISTY  begin ###########
# listy
lista_1 = [1, 2, 3, 4, 5]
print(f'Lista 1: {lista_1}\n')
print(f'Pierwszy element listy: {lista_1[0]}\n')
print(f'Ostatni element listy: {lista_1[-1]}\n')
print(f'Długość listy: {len(lista_1)}\n')

# możemy sprawdzić adres fizyczny listy w pamięci
print(f'Adres fizyczny listy w pamięci: {id(lista_1)}\n')
print(f'Adres szesnastkowy: {hex(id(lista_1))}\n')

# Mutowalność/edytowalność listy
print("Dodajemy element 6 do listy\n")
lista_1.append(6)
print(f'Lista 1 po dodaniu elementu: {lista_1}\n')
print(f'Długość listy: {len(lista_1)}\n')

# wartości w liście można nadpisać
print("Nadpisujemy pierwszy element listy wartością 10\n")
lista_1[0] = 10
print(f'Lista 1 po nadpisaniu: {lista_1}\n')

# wartości w liście można usuwać
print("Usuwamy ostatni element listy\n")
lista_1.pop()
print(f'Lista 1 po usunięciu: {lista_1}\n')

# wartości w liście można usuwać po indeksie
print("Usuwamy pierwszy element listy\n") 
lista_1.pop(0)
print(f'Lista 1 po usunięciu: {lista_1}\n')

# wartości w liście mogą być różnych typów
print("Dodajemy element 'Hello' do listy\n")
lista_1.append("Hello")
print(f'Lista 1 po dodaniu elementu: {lista_1}\n')

########### LISTY end ###########


########### SŁOWNIKI begin ###########

# słownik / dictionary
slownik_1 = {'a': 1, 'b': 2, 'c': 3}
print(f'Słownik 1: {slownik_1}\n')
# Słownik - dostęp po kluczu
print(f"Wartość dla 'a': {slownik_1['a']}")
print(f"Wartość dla 'b': {slownik_1['b']}")
print(f"Wartość dla 'c': {slownik_1['c']}")

slownik_2 = {1: 'jeden', 2: 'dwa', 3: 'trzy'}
# Słownik - dostęp po kluczu
print(f"Wartość dla 1: {slownik_2[1]}")
print(f"Wartość dla 2: {slownik_2[2]}")
print(f"Wartość dla 3: {slownik_2[3]}")
print ()

# słownik dni tygodnia
dni_tygodnia = {
    1: 'Poniedziałek',
    2: 'Wtorek',
    3: 'Środa',
    4: 'Czwartek',
    5: 'Piątek',
    6: 'Sobota',
    7: 'Niedziela'
}

print(f'Pracujemy w dniach: {dni_tygodnia[1]}, {dni_tygodnia[2]}, {dni_tygodnia[3]}, {dni_tygodnia[4]} i {dni_tygodnia[5]}\n')  # Poniedziałek, Wtorek, Środa, Czwartek, Piąte
print(f'Odpoczywamy w dniach: {dni_tygodnia[6]} i {dni_tygodnia[7]}\n')  # Sobota, Niedziela

########### SŁOWNIKI end ###########

# zbiór / set
zbior_1 = {1, 2, 3, 4, 5}
print(f'Zbiór 1: {zbior_1}\n')
# Zbiór - automatyczna deduplikacja (kluczowa cecha!)
zbior_2 = {1, 1, 2, 2, 3}
print(f"Zbiór z duplikatami: {zbior_2}")  # Wyświetli: {1, 2, 3}


# krotka / tuple
krotka_1 = (1, 2, 3, 4, 5)
print(f'Krotka 1: {krotka_1}\n')
krotka_1 = (1, 1, 2, 2, 3)
# Próbujemy zmienić pierwszy element z 1 na 99:
#krotka_1[0] = 99