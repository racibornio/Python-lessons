#wariant 1 - wypełnij listę podanymi wartościami
lista_do_wypelnienia = []
licznik = 10
for i in range(1, 11):
    lista_do_wypelnienia.append(input(f'Wpisz dane jeszcze {licznik} razy'))
    licznik -= 1
    print('Lista teraz:', lista_do_wypelnienia)

print('Cała lista to', lista_do_wypelnienia)


#wariant 2 - wypełnij listę podanymi wartościami - szybsza
lista_inaczej = []
for i, e in enumerate(range(10, 0, -1)):
    lista_inaczej.append(input(f'Wpisz dane do listy jeszcze {e} razy'))
    print('Lista teraz:', lista_inaczej)
    print('i:', i, 'e:', e)

print('Cała lista:', lista_inaczej)