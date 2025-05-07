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