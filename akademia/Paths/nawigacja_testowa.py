from pathlib import Path

cwd_path = Path.cwd()

print(f'Obecna ścieżka to {cwd_path}')
print('Name:', cwd_path.name)
print('Stem:', cwd_path.stem)
print('Suffix:', cwd_path.suffix)
print('Full path:', cwd_path.resolve())
print()


curr_file_path = Path('nawigacja_testowa.py')

print(f'Nowe przypisanie: {curr_file_path}')
print('Name:', curr_file_path.name)
print('Stem:', curr_file_path.stem)
print('Suffix:', curr_file_path.suffix)
print('Full path:', curr_file_path.resolve())