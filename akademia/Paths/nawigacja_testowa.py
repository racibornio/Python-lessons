from pathlib import Path

cwd_path = Path.cwd()

print(f'Obecna ścieżka to {cwd_path}')
print('Name:', cwd_path.name)
print('Stem:', cwd_path.stem)
print('Suffix:', cwd_path.suffix)
print('Full path:', cwd_path.resolve())
print('Czy plik?', cwd_path.is_file())
print()


#curr_file_path = Path('nawigacja_testowa.py')
curr_file_path = Path(__file__).resolve()

print(f'Nowe przypisanie: {curr_file_path}')
print('Name:', curr_file_path.name)
print('Stem:', curr_file_path.stem)
print('Suffix:', curr_file_path.suffix)
print('Full path:', curr_file_path.resolve())
print('Czy plik?', curr_file_path.is_file())
print()


print("Iteracja po katalogu:")
for file_path in cwd_path.iterdir():
    print(file_path)


print()
duplikaty_path = Path( cwd_path / 'akademia' / 'oczyszczanie_danych' / 'pandas_duplikaty.py')
print("Czy plik istnieje?", duplikaty_path.exists())
print()
print("Ścieżka do pliku duplikaty:")
print(duplikaty_path.resolve())
print()

print("Same pliki .odt:")
katalog_wyslane = Path("C:/Users/Patryk/Documents/CV/wysłane")
for plik in katalog_wyslane.rglob("*.odt"):
    print(plik.name)
    print(plik.resolve())