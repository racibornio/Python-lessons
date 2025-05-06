#unordered

slownik_1 = {}

print(slownik_1)

slownik_2 = {
    "litera_a": "A",
    "litera_b": "B"
}

print(slownik_2)

print('litera_a', slownik_2["litera_a"])
slownik_2["litera_c"] = "C"
print('Po dodaniu C:', slownik_2)

litery_i_liczby = {
    "litery": {'a', 'b', 'c'},
    "liczby": {1, 2, 3}
}


print("Litery i liczby:", litery_i_liczby)

#nadpisuje
#litery_i_liczby = {"litery": 'd'}
#litery_i_liczby = {"liczby": 4}

#dodaje - nie nadpisuje
litery_i_liczby["litery"].add('d')
litery_i_liczby["liczby"].add(4)
print("Litery i liczby po dodaniu 4-tej:", litery_i_liczby)

samochody = {
    "Alfa": {"Rok_prod" : 2000, "Pojemność" : 1.6},
    "Toyota": {"Rok_prod" : 2017, "Pojemność" : 1.8}
}

print(samochody)
print(samochody["Toyota"])

samochody["Mazda"] = {"Rok_prod" : 1999, "Pojemność" : 1.4}
print(samochody)
print(samochody["Mazda"])

for marka, dane in samochody.items():
    print(f"Marka: {marka}, Rok produkcji: {dane['Rok_prod']}, Pojemność: {dane['Pojemność']}")


czy_seat = samochody.get("Seat", "Nie ma Seata")
print(czy_seat)

samochody.pop("Seat", None)

# ludzie = {"Ludź 1"}
# print(ludzie)
#
# ludz_1 = input("Wpisz ludzia 1")
# ludzie["Ludź 1"].add(ludz_1)
# print(ludzie)

#utwórz nowy pusty słownik
nowy_slownik = {}
print("Pusty słownik poprzez 'nowy_slownik = {}':", nowy_slownik)

#dodaj pierwszą parę klucz:wartość
nowy_slownik["Pierwszy klucz"] = "Pierwsza wartość"
print("Dodanie pierwszej pary danych poprzez 'nowy_slownik[\"Pierwszy klucz\"] = \"Pierwsza wartość\"':", nowy_slownik)

#dodaj drugą parę klucz:wartość
nowy_slownik["Drugi klucz"] = "Druga wartość"
print("Dodanie drugiej pary danych poprzez 'nowy_slownik[\"Drugi klucz\"] = \"Druga wartość\"':", nowy_slownik)

#usuń drugą parę klucz:wartość
del nowy_slownik["Drugi klucz"]
print("Słownik po usunięciu 'del nowy_slownik[\"Drugi klucz\"]'", nowy_slownik)

#dodaj wiele par naraz - zdefiniowanie słownika na nowo, bo usuwa to co było
nowy_slownik = {"k1" : "v1", "k2" : "v2"}
print("Dodanie nowych pozycji poprzez 'nowy_slownik = {\"k1\" : \"v1\", \"k2\" : \"v2\"}'", nowy_slownik, "- wywaliło to co było")

#słownik list
slownik_list = {
    "listaNiepar" : [1, 3, 5, 7, 9],
    "listaPar" : [2, 4, 6, 8, 10]
}
print("Wyświetlenie słownika list", slownik_list)
print("Wyświetlenie 2-giej pozycji 1-go słownika", slownik_list["listaNiepar"][1])

calkiem_nowy_slownik = {}
print('Nowy słownik', calkiem_nowy_slownik, 'jego id', id(calkiem_nowy_slownik))
calkiem_nowy_slownik["klucz a"] = {"wartość a"}
klucz = next(iter(calkiem_nowy_slownik))
wartosc_wartosci = calkiem_nowy_slownik["klucz a"]
print('Nowy słownik', calkiem_nowy_slownik, 'jego id', id(calkiem_nowy_slownik), 'id klucza', id(klucz), 'id wartości', id(wartosc_wartosci))

calkiem_nowy_slownik["a"] = "a"
print('Wyświetlamy nowy słownik', calkiem_nowy_slownik)
calkiem_nowy_slownik["b"] = "b"
print('Wyświetlamy nowy słownik', calkiem_nowy_slownik)
calkiem_nowy_slownik[1] = 1
print('Wyświetlamy nowy słownik', calkiem_nowy_slownik)

slownik_3 = {"a-K" : "a-V", "b-K" : "b-V"}
print(slownik_3)
slownik_3["c-K"] = "c-V"
print(slownik_3)
print(slownik_3["a-K"])

przykladowy_slownik = {
    1 : "a",
    2 : "b",
    3 : "c"
}

print(przykladowy_slownik)

slownik_adresow_pamieci = {}

for k, v in przykladowy_slownik.items():
    slownik_adresow_pamieci[id(k)] = id(v)
    print(id(k), ':', id(v))

for i in przykladowy_slownik.keys():
    print('Klucze słownika:', i)


for i in przykladowy_slownik.values():
    print('Wartości słownika', i)


for i in przykladowy_slownik.items():
    print('Pary klucz-wartość słownika', i)


przykladowy_slownik[4] = "d"
print(przykladowy_slownik)

for i in range(0, 11):
    if i in przykladowy_slownik:
        print(i, 'znajduje się')
    else:
        print(i, 'nie znajduje się')


for i in range(0, 11):
    print(i, przykladowy_slownik.get(i, 'nie ma wartości'))


print(przykladowy_slownik.setdefault(0, '0  nie istnieje'))
przykladowy_slownik[0] = 0

print(przykladowy_slownik.setdefault(0, '0  nie istnieje'))