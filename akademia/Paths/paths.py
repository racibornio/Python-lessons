from pathlib import Path

DATA_PATH = Path.cwd()
print(DATA_PATH)
print(DATA_PATH.exists())

DATA_PATH = Path("raw")
print(DATA_PATH)
print(DATA_PATH.exists())

DATA_TITANIC = DATA_PATH / "import_pliku_csv.py"
print(DATA_TITANIC)
print(DATA_TITANIC.exists())
print(f'Czy DATA_PATH to katalog?: {DATA_PATH.is_dir()}')
print(f'Czy DATA_PATH to plik?: {DATA_PATH.is_file()}')
print(f'Czy DATA_TITANIC to katalog?: {DATA_TITANIC.is_dir()}')
print(f'Czy DATA_TITANIC to plik?: {DATA_TITANIC.is_file()}')

TOP = DATA_PATH / "../"
print(TOP)
for subpath in TOP.iterdir():
    print(f'iterdir(): {subpath}')


for subpath in DATA_PATH.glob("**/*.csv"):
    print(f'glob("**/*.csv"): {subpath}')


print(DATA_TITANIC.name)
print(DATA_TITANIC.stem)
print(DATA_TITANIC.suffix)