import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

csv_path = Path(__file__).parent / "used_car_dataset.csv"

initial_df = pd.read_csv(csv_path)

df = initial_df.copy()
print(df.head())
print(df.info())
print()

unique_years_list = sorted(df['Year'].unique().tolist())
print(f'Unique years: {unique_years_list}')
print()


print('Sample price:', df['AskPrice'].sample())
print()
print(df['AskPrice'].dtype)
df['AskPrice'] = (df['AskPrice'].astype(str).str.replace('₹', '').str.replace(',', '').str.strip().astype(float))
print('Sample price:', df['AskPrice'].sample())
print()
ask_price_mean = (df['AskPrice']).mean()
print(f'Average price is {round(ask_price_mean, 2)}')
print()
ask_price_median = (df['AskPrice']).median()
print(f'Median price is {round(ask_price_median, 2)}')
print()


# minimal price
minimal_price_per_year = df.groupby(['Year'])['AskPrice'].min()
print(f'Minimal price per year:')
print(minimal_price_per_year)
print()

minimal_price_per_year.to_dict()
print('Minimal price per year as a dictionary:')
print(minimal_price_per_year)
print()

rows_for_minimum = []

for year, minimal_yearly_price in minimal_price_per_year.items():
    print(f'In {year} the minimal price was {minimal_yearly_price}')
    rows_for_minimum.append({'year': year, 'minimal_yearly_price' : minimal_yearly_price})


min_yr_price_df = pd.DataFrame(rows_for_minimum)
print()
print('New data frame - yearly min prices:')
print(min_yr_price_df)
print()

min_yr_price_df.plot(kind='line', x='year', y='minimal_yearly_price')
plt.title="Yearly lowest price"
plt.xlabel="Year"
plt.ylabel="Price"
plt.show()


# maximum price
maximum_price_per_year = df.groupby(['Year'])['AskPrice'].max()
print(f'Maximum price per year:')
print(maximum_price_per_year)
print()

rows_for_maximum = []

for year, maximum_yearly_price in maximum_price_per_year.items():
    print(f'In {year} the maximum price was {maximum_yearly_price}')
    rows_for_maximum.append({'year' : year, 'maximum_yearly_price' : maximum_yearly_price})
    

max_yr_price_df = pd.DataFrame(rows_for_maximum)
print()
print('New data frame - yearly max prices:')
print(max_yr_price_df)
print()

max_yr_price_df.plot(kind='line', x='year', y='maximum_yearly_price')
plt.title="Yearly highest price"
plt.xlabel="Year"
plt.ylabel="Price"
plt.show()


# merge into one data frame
merged_df = pd.merge(min_yr_price_df, max_yr_price_df, on='year')
print('po zmerdżowaniu')
print(merged_df)
merged_df.plot(kind='line', x='year', y=['minimal_yearly_price', 'maximum_yearly_price'])
plt.title='Min. vs. max. price - yearly'
plt.xlabel='Year'
plt.ylabel='Price'
plt.grid()
plt.show()