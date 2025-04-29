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


print(litery_i_liczby)

#nadpisuje
#litery_i_liczby = {"litery": 'd'}
#litery_i_liczby = {"liczby": 4}

#nadpisuje
litery_i_liczby["litery"].add('d')
litery_i_liczby["liczby"].add(4)
print(litery_i_liczby)

samochody = {
    "Alfa": {"Rok_prod" : 2000, "Pojemność" : 1.6},
    "Toyota": {"Rok_prod" : 2017, "Pojemność" : 1.8}
}

print(samochody)
print(samochody["Toyota"])

samochody["Mazda"]=  {"Rok_prod" : 1999, "Pojemność" : 1.4}
print(samochody)
print(samochody["Mazda"])

for marka, dane in samochody.items():
    print(f"Marka: {marka}, Rok produkcji: {dane['Rok_prod']}, Pojemność: {dane['Pojemność']}")


czy_seat = samochody.get("Seat", "Nie ma Seata")
print(czy_seat)

samochody.pop("Seat", None)

ludzie = {"Ludź 1"}
print(ludzie)

ludz_1 = input("Wpisz ludzia 1")
ludzie["Ludź 1"].add(ludz_1)
print(ludzie)