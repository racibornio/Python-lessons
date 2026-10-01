dni_tygodnia = ['Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', '']
dzisiejszy_dzien = dni_tygodnia[0]
print(dzisiejszy_dzien)


# Tylko poniższa konstrukcja faktycznie sprawdzy czy oba dni występują:
if 'Sobota' in dni_tygodnia and 'Niedziela' in dni_tygodnia:
    print('Weekend występuje na liście.')
else:
    print('Najwyraźniej weekend nie jest pełny.')

if 'Sobota' not in dni_tygodnia and 'Niedziela' not in dni_tygodnia:
    print('Weekend nie występuje na liście.')



# Ten wariant nie zadziała tak jak chcemy - dla Pythona 'Sobota' to coś, co jest TRUE, więc warunek zawsze przejdzie
if 'Sobota' and 'Niedziela' in dni_tygodnia:
    print('Weekend występuje na liście.')


temperatura = 39

if temperatura > 0 and temperatura <= 30:
    print('Jest ciepło.')
elif temperatura > 30:
    print("Jest gorąco.")
else:
    print('Jest zimno.')


zamowienie = ['chleb', 'maslo', 'ser', 'wedlina', 'pomidor']
dostepne_produkty = ['chleb', 'maslo', 'ser']

for produkt in zamowienie:
    if produkt not in dostepne_produkty:
        print(f'{produkt} jest niedostępny.')

# Krótsza wersja powyższego warunku z pętlą
niedostepne_produkty = [p for p in zamowienie if p not in dostepne_produkty]
print(f'Nie mamy produktów: {niedostepne_produkty}')