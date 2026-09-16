moja_lista = [2, 3, 1]

print(f'Lista: {moja_lista}\n')

print(f' ### Użycie metody moja_lista.sort() ###')
print(f'"print(moja_lista.sort())" nie zadziała, bo próbuje zwrócić listę, a nie zdąży jej zwrócić i od razu wyświetlić w jednym wierszu, więc zwróci None.')
print(f'{moja_lista.sort()}\n')

print(f'Trzeba w jednej linii posortować: moja_lista.sort()"')
print(f'i w drugiej linii wyświetlić: print(moja_lista):')
moja_lista.sort()
print(f'{moja_lista}\n')
print(f'Wniosek - metody wywołane "na" obiekcie zmieniają go w miejscu - zmiany są jak widać poniżej trwałe:')
print(f'{moja_lista}\n')

print(f' ### Użycie funkcji print(sorted(moja_lista)) ###')
moja_lista = [2, 3, 1]
print(f'Lista na nowo jest przemieszana: {moja_lista}\n')

print(f'Teraz sorted(moja_lista) - wykona się w print(), ale tylko w locie i zmiany nie będą trwałe: {sorted(moja_lista)}')
print(f'Za dowód nietrwałości zmian - wyświetlamy listę natychmiast po uprzednim użyciu sorted(moja_lista): {moja_lista}\n')

print(f'### Użycie funkcji sorted(list) w osobnej linii ###')
print(f'Przywrócona do zmieszania lista zostaje w osobnej linii posortowana tymczasowo poprzez "sorted(list)", a następnie wyświetlona w "print:(lista)"')
sorted(moja_lista)
print(f'Lista po sorted(moja_lista) w osobnej linii: {moja_lista} -> jak widać sortowanie od razu uciekło i już jest niedostępne.')

tymczasowe_sortowanie_do_zmiennej = sorted(moja_lista)
print(f'Lista po sorted(list) w osobnej linii przypisana do zmiennej: {tymczasowe_sortowanie_do_zmiennej} -> jak widać sortowanie w nowej zmiennej zostaje.')
print(f'Lista pierwotna: {moja_lista}.')
print(f'Nowa zmienna, do której trafiła lista poddana sortowaniu w locie: {tymczasowe_sortowanie_do_zmiennej}.\n')

print(f'### Pierwotna lista wygląda teraz tak: {moja_lista}')
print(f'Posortowanie i odwrócenie od największej poprzez "moja_lista.sort(reverse=True) - oczywiście w osobnej linii przed użyciem":')
moja_lista.sort(reverse=True)
print(f'{moja_lista}\n')

print(f'Lista pozostaje w takim stanie:')
print(f'{moja_lista}')
print(f'Ponowne przemieszanie listy:')
moja_lista = [2, 3, 1]
print(f'{moja_lista}\n')

print(f'Zwykłe odwrócenie listy bez ingerowania w narastającość elementów poprzez "moja_lista.reverse()" - oczywiście w osobnej linii przed użyciem:')
moja_lista.reverse()
print(f'{moja_lista}')
print(f'Efekt jest trwały: {moja_lista}\n')
print(f'Ponowne przemieszanie listy:')
moja_lista = [2, 3, 1]
print(f'{moja_lista}')
print(f'Powyższe dokonano "na obiekcie", a więc jest on zmodyfikowany trwale.\n')

print(f'Teraz posortowanie listy i jej zawrócenie, ale tylko w locie poprzez "sorted(moja_lista, reverse=True)" - oczywiście w osobnej linii przed użyciem:')
print(f'{sorted(moja_lista, reverse=True)}')
print(f'Efekt nie jest trwały: {moja_lista}\n')

print(f'### Uwaga - zapis: "nowa = moja_lista.sort()" spowoduje trwałe posortowanie listy "moja_lista", ale to nowej zmiennej i tak wrzuci None, bo metoda sort() nie zwraca listy, tylko None.')
nowa = moja_lista.sort()
print(f'Lista po "nowa = moja_lista.sort()": {moja_lista}')
print(f'Nowa zmienna "nowa" po "nowa = moja_lista.sort()": {nowa}\n')