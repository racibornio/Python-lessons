napis = 'fjdla fds ajljfdklsafj'

print(napis[0], napis[-1], napis[15], len(napis), napis[7:9])
czy_x = 'x' in napis
print(czy_x)
czy_a = 'a' in napis
print(czy_a)


#konkatenacja
imie = 'Patryk'
wiek = 100
print('Mam na imię ' + imie + ' i mam ' + str(wiek) + ' lat.')

#interpolacja tekstu
print('Mam na imię %s i mam %d lat.' % (imie, wiek))

#ciąg formatowany
print(f'Mam na imię {imie} i mam {wiek} lat.')

wpisz = input('Wpisz słowo')
if  wpisz.islower():
    print('Wpisałeś małymi literami')
elif wpisz.isupper():
    print('Wpisałeś wielkimi literami')
elif wpisz.istitle():
    print('Wpisałeś tytularnie')
else:
    print('Namieszałeś...')


wpisz.isalpha() #jeśli tylko litery i niepusty
wpisz.isalnum() #jeśli litery i cyfry i niepusty
wpisz.isdecimal() #jeśli tylko cyfry i niepusy
wpisz.isspace() #jeśli tylko spacje, taby i znaki nowego wiersza i niepusty


# startswith, endswith
dlugi_napis = '1d1a fdjsak 0o'
czy_od_1a = dlugi_napis.startswith('1')
print('Czy zaczyna się od "1"?: ', czy_od_1a)
czy_koniec_o = dlugi_napis.endswith('o')
print('Czy koniec na "o"?:', czy_koniec_o)


# join(), split() i partition()
# join() to metoda łańcuchowa, wywoływana na separatorze, a nie funkcja przyjmująca wiele argumentów
tekst_1 = "fjdkal"
tekst_2 = "fud0s9a"
tekst_3 = "f0dsafdsa0"
tekst_laczony = "-".join([tekst_1, tekst_2, tekst_3])
print(tekst_laczony)

# split()
tekst_do_rozbicia = "jeden dwa trzy cztery, pięć sześć; siedem i osiem."
print(tekst_do_rozbicia.split())
tekst_do_rozbicia_z_parametrem = "dwaq piętnqaście q osiemq qurde"
print(tekst_do_rozbicia_z_parametrem.split('q')) # jako argument może przyjąć znak nowego wiersz - \n

# partition() - wyszukuje w ciągu tekstowym przekazany jej separator, a następnie zwraca krotkę
# trzech podciągów tekstowych: „tekst przed separatorem”, „separator”, „tekst po separatorze”
tekst_do_podzialu_metoda_partition = "to jest do podziału tekst"
krotka_po_wyodrebnieniu = tekst_do_podzialu_metoda_partition.partition('do')
print(krotka_po_wyodrebnieniu)
print('Wynik działania krotki:', krotka_po_wyodrebnieniu[0], 'separator:', krotka_po_wyodrebnieniu[1], 'reszta:', krotka_po_wyodrebnieniu[2])