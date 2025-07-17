from turtle import title
import plotly.express as px
import seaborn as sns


tips_df = sns.load_dataset('tips')
print(tips_df.sample(10))

fig = px.histogram(
    tips_df,
    x='total_bill',
    title='Rozkład wartości rachunku',
    width=600,
    height=400
)
fig.show()
print()


nbins = int(len(tips_df) ** (1/2))

fig = px.histogram(
    tips_df,
    x='total_bill',
    title='Rozkład wartości rachunku',
    nbins=nbins,
    width=600,
    height=400
)
fig.show()
print()


fig = px.histogram(tips_df, x='day')
fig.update_layout(
    title='Liczba rachunków w zależności od dnia tygodnia',
    xaxis_title='Dzień tygodnia',
    yaxis_title='Liczba rachunków'
)
fig.show()
print()


tips_df['tip_percentage'] = tips_df['tip'] / tips_df['total_bill'] * 100
mean_tips_df = tips_df.groupby('day', as_index=False)['tip_percentage'].mean()

fig = px.bar(mean_tips_df, x='day', y='tip_percentage')
fig.update_layout(
    title='Średnia napiwku w zależności od dnia tygodnia',
    xaxis_title='Dzień tygodnia',
    yaxis_title='Średnia napiwku'
)
fig.show()
print()


fig = px.box(tips_df, x='day', y='tip')
fig.update_layout(
    title='Rozkład napiwków w zależności od dnia tygodnia',
    xaxis_title='Dzień tygodnia',
    yaxis_title='Napiwek'
)
fig.show()
print()


fig = px.scatter(tips_df, x='total_bill', y='tip')
fig.update_layout(
    title='Zależność napiwku od wartości rachunku',
    xaxis_title='Wartość rachunku',
    yaxis_title='Napiwek'
)
fig.show()
print()


fig = px.scatter(
    tips_df,
    x='total_bill',
    y='tip',
    color='smoker',
    size='size'
)
fig.update_layout(
    title='Zależność napiwku od wartości rachunku',
    xaxis_title='Wartość rachunku',
    yaxis_title='Napiwek'
)
fig.show()
print()


fig = px.imshow(
    tips_df.corr(numeric_only=True),
    color_continuous_scale='Inferno_r'
)
fig.show()
print()