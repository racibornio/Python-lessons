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


sns.lmplot(
    data=tips_df,
    x='total_bill',
    y='tip',
    col='time',
    hue='smoker'
)
plt.show()