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