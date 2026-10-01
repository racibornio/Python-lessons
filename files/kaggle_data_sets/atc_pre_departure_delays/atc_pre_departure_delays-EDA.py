from pathlib import Path

cwd = Path.cwd()
print(f'Current path is {cwd}')

file_path = cwd / 'files' / 'kaggle_data_sets' / 'atc_pre_departure_delays' / 'atc_pre_departure_delays.csv'

print(f'File path is {file_path.absolute()}')
print(f'File stem is {file_path.stem()}')