from re import split
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

cwd = Path.cwd()
print(f'Current path: {cwd}')

file_path = cwd / 'Programs'/ 'Wykresy - temperatura'
temperatura_df = pd.read_csv( file_path / 'temperatura.csv')

print('Data frame:')
print(temperatura_df)


plt.plot(temperatura_df['Godzina'], temperatura_df['Temperatura'])
plt.xlabel('Hour')
plt.ylabel('Temperature')
plt.title('Temperature during the day')
plt.grid(True)
plt.show()


plt.scatter(temperatura_df['Godzina'], temperatura_df['Temperatura'])
plt.xlabel('Hour')
plt.ylabel('Temperature')
plt.title('Temperature during the day')
plt.grid(True)
plt.show()


plt.bar(temperatura_df['Godzina'], temperatura_df['Temperatura'])
plt.xlabel('Hour')
plt.ylabel('Temperature')
plt.title('Temperature during the day')
plt.grid(True)
plt.show()


plt.barh(temperatura_df['Godzina'], temperatura_df['Temperatura'])
plt.xlabel('Hour')
plt.ylabel('Temperature')
plt.title('Temperature during the day')
plt.grid(True)
plt.show()


sns.relplot(
    data=temperatura_df,
    x='Godzina',
    y='Temperatura',
    col='Godzina',
    hue='Temperatura',
    style='Temperatura',
    size='Temperatura'
)
plt.show()


sns.lmplot(
    data=temperatura_df,
    x='Godzina',
    y='Temperatura',
    col='Godzina',
    hue='Temperatura'
)
plt.show()


sns.displot(
    data=temperatura_df,
    x='Godzina',
    y='Temperatura',
    col='Godzina',
    kind='hist'
)
plt.show()


sns.catplot(
    data=temperatura_df,
    kind='swarm',
    x='Godzina',
    y='Temperatura',
    hue='Temperatura'
)
plt.show()


sns.catplot(
    data=temperatura_df,
    kind='violin',
    x='Godzina',
    y='Temperatura',
    hue='Temperatura',
    split=True
)
plt.show()


sns.jointplot(
    data=temperatura_df,
    x='Godzina',
    y='Temperatura',
    hue='Temperatura'
)
plt.show()


sns.pairplot(
    data=temperatura_df,
    hue='Temperatura'
)
plt.show()