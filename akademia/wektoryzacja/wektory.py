import pandas as pd
from datetime import datetime

df = pd.DataFrame([
    {"cena" : 1, "nazwa" : "A"},
    {"cena" : 6, "nazwa" : "B"},
    {"cena" : 17, "nazwa" : "C"},
    {"cena" : 61, "nazwa" : "D"}
])

print('Data frame do wektoryzacji:')
print(df)
print('Dodanie kolejnego wektora - df["cena"] + 5:')
print(df["cena"] + 5)
print()

print('Ponowne wywołanie samego df:')
print(df)
print()

print('Trwała zmiana wartości - df["cena"] += 5:')
df['cena'] += 5
print(df)
print()

print('Dodanie nowej kolumny z identycznymi wartościami:')
df['ilość'] = 45
print(df)
print()

# użycie wektora do pracy z datami
now = datetime.now()
print('Pokaż now():')
print(now)
print()

hire_date = [datetime(2024, 1, 13), datetime(2024, 2, 13), datetime(2024, 3, 13)]
nowy_df = pd.DataFrame( {"hire date" : hire_date} )
print('Nowy data frame:')
print(now - nowy_df["hire date"])

godzina_zdarzenia = datetime(2025, 5, 13, 13, 4, 55, 518219)
print('Godzina zdarzenia:', godzina_zdarzenia)
roznica = now - godzina_zdarzenia
sekundy = roznica.total_seconds()
minuty = roznica.total_seconds() / 60
godziny = roznica.total_seconds() / 3600
print('Upłynęło sekund:', sekundy, 'w przybliżeniu', round(sekundy)) # opcjonalny drugi argument - ilość miejsc po przecinku
print('Upłynęło minut:', minuty, 'w przybliżeniu', round(minuty)) # opcjonalny drugi argument - ilość miejsc po przecinku
print('Upłynęło godzin:', godziny, 'w przybliżeniu', round(godziny)) # opcjonalny drugi argument - ilość miejsc po przecinku