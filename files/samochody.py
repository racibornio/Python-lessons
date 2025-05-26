from cProfile import label

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

df = pd.read_csv('samochody.csv')

print(df)

df['rok'] = df['rok'].astype(int)
df.plot(kind='scatter', x='sprzedanych', y='rok', c='silnik')
plt.show()


df['model_size'] = df['model'].map({'Aygo' : 50, 'Auris' : 100, 'Corolla' : 150})
scatter_plot = df.plot(
    kind='scatter',
    x='silnik',
    y='sprzedanych',
    c='rok',
    s='model_size',
    cmap='plasma',
    alpha=0.7,
    figsize=(10,6),
    title='Sprzedaż'
)

char = plt.colorbar(scatter_plot.collections[0], label='Rok')
char.set_ticks(sorted(df['rok'].unique()))
char.set_ticklabels(sorted(df['rok'].unique()))

plt.xlabel('Pojemność silnika [L]')
plt.ylabel('Liczba sprzedanych sztuk')
plt.grid()

legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Aygo', markersize=5),
    Line2D([0], [0], marker='o', color='w', label='Auris', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='Corolla', markersize=15)
]

plt.legend(handles=legend_elements, title='Model (rozmiar punktu)', loc='upper left')
plt.show()