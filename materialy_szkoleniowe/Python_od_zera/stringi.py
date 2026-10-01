napis = "To jest przykładowy napis w Pythonie."

print(f'Cały napis: {napis}')
print(f'Pierwszy znak napisu: {napis[0]}')
print(f'Ostatni znak napisu: {napis[-1]}')
print(f'Długość napisu: {len(napis)}')
print(f'Adres fizyczny napisu w pamięci: {id(napis)}')
print(f'Adres szesnastkowy: {hex(id(napis))}')
print(f"Napis odwrócony: {napis[::-1]}")
print(f"Napis z wielkimi literami: {napis.upper()}")
print(f"Napis z małymi literami: {napis.lower()}")
print(f"Napis z zamienionymi literami: {napis.swapcase()}")
print(f"Napis z zamienionymi literami na wielkie: {napis.capitalize()}")
print(f"Napis z zamienionymi literami na wielkie i małe: {napis.title()}")

# Stworzenie listy ciągów znaków rozdzielonych przekazanym separatorem
print(napis.split(" "))

# Łączenie stringów separatorem - przyjmuje tablicę jako argument
join_string = " "
print(join_string.join(["a", "b", napis]))

zaczyna_sie_od_t = napis.startswith('t')
zaczyna_sie_od_T = napis.startswith('T')
print(f'Czy zaczyna się od "t"? -> {zaczyna_sie_od_t}')
print(f'Czy zaczyna się od "T"? -> {zaczyna_sie_od_T}')

napis = napis.strip('T')
print(f'Napis po usunięciu "p": {napis}')

zm = 4.4
czyInstancja = isinstance(napis, str)
print(f'Czy instancja? {czyInstancja}')