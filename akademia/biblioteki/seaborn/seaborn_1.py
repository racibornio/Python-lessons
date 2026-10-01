from turtle import pen
import seaborn as sns
import matplotlib.pyplot as plt

tips_df = sns.load_dataset('tips')
print(tips_df.sample(10))

sns.relplot(
    data=tips_df,
    x='total_bill',
    y='tip',
    col='time',
    hue='smoker',
    style='smoker',
    size='size'
)
plt.show()
print()


sns.lmplot(
    data=tips_df,
    x='total_bill',
    y='tip',
    col='time',
    hue='smoker'
)
plt.show()
print()


sns.displot(
    data=tips_df,
    x='total_bill',
    col='time',
    #kind='kde',
    kind='hist'
)
plt.show()
print()


sns.catplot(
    data=tips_df,
    kind='swarm',
    x='day',
    y='total_bill',
    hue='smoker'
)
plt.show()
print()


sns.catplot(
    data=tips_df,
    kind='violin',
    x='day',
    y='total_bill',
    hue='smoker',
    split=True
)
plt.show()
print()


sns.catplot(
    data=tips_df,
    kind='bar',
    x='day',
    y='total_bill',
    hue='smoker'
)
plt.show()
print()


fmri_df = sns.load_dataset('fmri')
print(fmri_df.sample(10))

sns.relplot(
    data=fmri_df,
    kind='line',
    x='timepoint',
    y='signal',
    col='region',
    hue='event',
    style='event'
)
plt.show()
print()


penguins_df = sns.load_dataset('penguins')
print(penguins_df.sample(10))

sns.jointplot(
    data=penguins_df,
    x='flipper_length_mm',
    y='bill_length_mm',
    hue='species'
)
plt.show()
print()


sns.pairplot(
    data=penguins_df,
    hue='species'
)
plt.show()
print()