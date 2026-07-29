print("Introduction to Data Engineering in Python\n")

# listy
lista_1 = [1, 2, 3, 4, 5]
print(f'Lista 1: {lista_1}\n')
print(f'Pierwszy element listy: {lista_1[0]}\n')
print(f'Ostatni element listy: {lista_1[-1]}\n')
print(f'Długość listy: {len(lista_1)}\n')
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
# wartości w liście mogą być róóżnych typów
print("Dodajemy element 'Hello' do listy\n")
lista_1.append("Hello")
print(f'Lista 1 po dodaniu elementu: {lista_1}\n')


# krotka / tuple
krotka_1 = (1, 2, 3, 4, 5)
print(f'Krotka 1: {krotka_1}\n')
krotka_1 = (1, 1, 2, 2, 3)
# Próbujemy zmienić pierwszy element z 1 na 99:
krotka_1[0] = 99

# słownik / dictionary
slownik_1 = {'a': 1, 'b': 2, 'c': 3}
print(f'Słownik 1: {slownik_1}\n')
# Słownik - dostęp po kluczu
print(f"Wartość dla 'a': {slownik_1['a']}")
print(f"Wartość dla 'b': {slownik_1['b']}")
print(f"Wartość dla 'c': {slownik_1['c']}")

# zbiór / set
zbior_1 = {1, 2, 3, 4, 5}
print(f'Zbiór 1: {zbior_1}\n')
# Zbiór - automatyczna deduplikacja (kluczowa cecha!)
zbior_2 = {1, 1, 2, 2, 3}
print(f"Zbiór z duplikatami: {zbior_2}")  # Wyświetli: {1, 2, 3}