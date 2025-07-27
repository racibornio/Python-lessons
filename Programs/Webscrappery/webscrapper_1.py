import requests
import pandas as pd

url = "https://api.nbp.pl/api/exchangerates/tables/A/last/1/?format=json"

resp = requests.get(url)
resp.raise_for_status()

data = resp.json()[0]
rates = data['rates']
effective_date = data['effectiveDate']

df = pd.DataFrame(rates)
df['mid'] = df['mid'].astype(float)

print(f"Kursy z dnia {effective_date}")
print(df[['currency', 'code', 'mid']])
