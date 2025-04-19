#lista
dni_tygodnia = ["Pn", "Wt", "Śr", "Czw", "Pt", "So", "Nd"]
liczby_parzyste = [2, 4, 6, 8, 10]

#krotka
dni_tyg = ("Pn", "Wt", "Śr", "Czw", "Pt", "So", "Nd")
liczby_par = (2, 4, 6, 8, 10)

#set
dni = {"Pn", "Wt", "Śr", "Czw", "Pt", "So", "Nd"}
liczby_p = {2, 4, 6, 8, 10}

#słownik
dni_w_tygodniu = {0: "Pn", 1: "Wt", 2: "Śr", 3: "Czw", 4: "Pt", 5: "So", 6: "Nd"}
l_parzyste = {0: 2, 1: 4, 2: 6, 3: 8, 4: 10}

print(dni_tygodnia)
#dni_tygodnia.pop("nwd")

print(liczby_parzyste)
liczby_parzyste.append(12)
print(liczby_parzyste)
liczby_parzyste.insert(0, 0)
print(liczby_parzyste)
liczby_parzyste.remove(0)
print(liczby_parzyste)
del liczby_parzyste
try:
    liczby_parzyste
    print("Lista nadal istnieje")
except NameError:
    print("Lista została usunięta")
