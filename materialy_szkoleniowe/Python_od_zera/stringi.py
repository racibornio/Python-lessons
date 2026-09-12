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