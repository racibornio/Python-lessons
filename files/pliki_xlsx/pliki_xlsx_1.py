import pandas as pd
from pathlib import Path

curr_path = Path.cwd()
print(f'We are in {curr_path}')
print()

df = pd.read_excel(curr_path / 'files' / 'pliki_xlsx' / 'DataBleed.xlsx', sheet_name='DataBleed')
print('Entire sheet:')
print(df)
print()

print('Only 10 first rows of data:')
print(pd.read_excel(curr_path / 'files' / 'pliki_xlsx' / 'DataBleed.xlsx', sheet_name='DataBleed', skiprows=1, nrows=10))



# new excel file with my notes
notes_df = pd.DataFrame([
    {"note" : "first entry"},
    {"note" : "second entry"},
    {"note" : "third entry"}
])

notes_df.to_excel(curr_path / 'files' / 'pliki_xlsx' / 'my_notes.xlsx', index=False)

# this is the excel writer - not like the creator above - that adds data into the file
with pd.ExcelWriter(curr_path / 'files' / 'pliki_xlsx' / 'my_notes.xlsx', mode='a', if_sheet_exists='replace') as writer:
    notes_df.to_excel(writer, sheet_name='notes', index=False, startrow=2, startcol=2)