import pandas as pd

# Konfiguracja: wyświetlaj wszystko
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

plik_csv_df = pd.read_csv("pliczek.csv", sep=',')
print(plik_csv_df)

# operacje na danych na już stworzonym data framie

# na koniec export do .csv
#plik_csv_df.to_csv('plik_po_zmianach.csv', index=False)




# plik_xlsx_df = pd.read_excel("pliczek.xlsx", sheet_name='Sheet1')
# print(plik_xlsx_df)

# na koniec export do .xlsx
# plik_xlsx_df.to_excel('plik_po_zmianach.xlsx', index=False, sheet_name='ZmodyfikowaneDane')