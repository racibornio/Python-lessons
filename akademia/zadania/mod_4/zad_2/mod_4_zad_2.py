import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import legend
from pandas.core.config_init import pc_max_info_rows_doc
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

# Konfiguracja: wyświetlaj wszystko
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


df = pd.read_csv('26__titanic.csv')
total = len(df)
print(df.sample(15).to_string())
print()
df.columns = ['class', 'survived', 'full_name', 'sex', 'age', 'siblings/spouse', 'parents/children', 'ticket_no', 'fare_price', 'cabin_no', 'embarked', 'boat_no', 'body_no', 'destination']
print(df.sample(15).to_string())
print()

survivors = (df['survived'] == 1).sum()
print(f'Survived {survivors} of {total} persons.')
non_survivors = (df['survived'] == 0).sum()
print(f'Not survived {non_survivors} of {total} persons.')
print()


if df['survived'].isnull().sum() > 0:
    print('At least one information on survived/not-survived is missing.')
    print()


if df['class'].isnull().sum() > 0:
    print('At least one information on the class assignment is missing.')
    print()

first_class_passengers = (df['class'] == 1).sum()
second_class_passengers = (df['class'] == 2).sum()
third_class_passengers = (df['class'] == 3).sum()
print(f'Passengers of 1st class: {first_class_passengers}, 2nd class: {second_class_passengers}, 3rd class: {third_class_passengers}')
print()

# 1st class surviving ratio analysis
first_class_survivors = ( (df['class'] == 1) & (df['survived'] == 1) ).sum()
print('1st class survivors', first_class_survivors)

first_class_non_survivors = ( (df['class'] == 1) & (df['survived'] == 0) ).sum()
print('1st class non-survivors', first_class_non_survivors)
surviving_ratio_first_class = round(first_class_survivors / total * 100, 2)
print(f'Your chance to survive as the 1st class passenger was {surviving_ratio_first_class}%')
print()

# 2nd class surviving ratio analysis
second_class_survivors = ( (df['class'] == 2) & (df['survived'] == 1) ).sum()
print('2nd class survivors', second_class_survivors)

second_class_non_survivors = ( (df['class'] == 2) & (df['survived'] == 0) ).sum()
print('2nd class non-survivors', second_class_non_survivors)
surviving_ratio_second_class = round(second_class_survivors / total * 100, 2)
print(f'Your chance to survive as the 2nd class passenger was {surviving_ratio_second_class}%')
print()

# 3rd class surviving ratio analysis
third_class_survivors = ( (df['class'] == 3) & (df['survived'] == 1) ).sum()
print('3rd class survivors', third_class_survivors)

third_class_non_survivors = ( (df['class'] == 3) & (df['survived'] == 0) ).sum()
print('3rd class non-survivors', third_class_non_survivors)
surviving_ratio_third_class = round(third_class_survivors / total * 100, 2)
print(f'Your chance to survive as the 3rd class passenger was {surviving_ratio_third_class}%')
print()


class_survived_corr = df[["class", "survived"]].corr()
print(f'Class vs. survived correlation is {class_survived_corr}.')

class_labels = ['1st class', '2nd class', '3rd class']
survivors_by_class = [first_class_survivors, second_class_survivors, third_class_survivors]
non_survivors_by_class = [first_class_non_survivors, second_class_non_survivors, third_class_non_survivors]
chance_to_survive = [surviving_ratio_first_class, surviving_ratio_second_class, surviving_ratio_third_class]

plot_df = pd.DataFrame({
    'class' : class_labels,
    'survived' : survivors_by_class,
    'not_survived' : non_survivors_by_class,
    'chance_to_survive' : chance_to_survive
})

plot_df.plot(kind="pie", y="survived", labels=plot_df["class"], legend=False)
plt.show()

plot_df.plot(kind="bar", x="class", y=["chance_to_survive"])
plt.show()

print()
print('New data frame:')
print(plot_df)

print()
print('The cheapest tickets price (including zeros):')
print(
    df.groupby(['class'])['fare_price'].min()
)
print()
print('The most expensive tickets price:')
print(
    df.groupby(['class'])['fare_price'].max()
)
print()

# new data frame to replace 0 price with None
prices_not_zero_df = df.copy()
prices_not_zero_df.loc[(prices_not_zero_df['fare_price'] == 0)] = None
prices_not_zero_df = prices_not_zero_df.dropna(subset="fare_price")
print('New data frame with non-zeros for price:')
print(prices_not_zero_df.sample(15).to_string())
print()

cheapest_tickets_by_class = prices_not_zero_df.groupby(['class'])['fare_price'].min()
print(
    'Cheapest tickets by class (excluding zeros): \n', cheapest_tickets_by_class
)
print()

most_expensive_tickets_by_class = prices_not_zero_df.groupby(['class'])['fare_price'].max()
print(
    'Most expensive tickets by class:\n', most_expensive_tickets_by_class
)
print()

# the cheapest vs. the most expensive tickets in 1st class
print(f'1st class cheapest ticket: {cheapest_tickets_by_class[1.0]}')
print(f'1st class most expensive ticket: {most_expensive_tickets_by_class[1.0]}')
print()

# the cheapest vs. the most expensive tickets in 3rd class
print(f'3rd class cheapest ticket: {cheapest_tickets_by_class[3.0]}')
print(f'3rd class most expensive ticket: {most_expensive_tickets_by_class[3.0]}')
print()

# how many percent was the cheapest to the most expensive in the 1st class
cheapest_to_most_expensive_1st_class = (cheapest_tickets_by_class[1.0] / most_expensive_tickets_by_class[1.0]) * 100
print(f'The 1st class cheapest ticket price was {round(cheapest_to_most_expensive_1st_class, 2)}% of the most expensive one.')

# how many percent was the cheapest to the most expensive in the 2nd class
cheapest_to_most_expensive_2nd_class = (cheapest_tickets_by_class[2.0] / most_expensive_tickets_by_class[2.0]) * 100
print(f'The 2nd class cheapest ticket price was {round(cheapest_to_most_expensive_2nd_class, 2)}% of the most expensive one.')

# how many percent was the cheapest to the most expensive in the 3rd class
cheapest_to_most_expensive_3rd_class = (cheapest_tickets_by_class[3.0] / most_expensive_tickets_by_class[3.0]) * 100
print(f'The 3rd class cheapest ticket price was {round(cheapest_to_most_expensive_3rd_class, 2)}% of the most expensive one.')

print()

# how many times was the most expensive more expensive than the cheapest in the 1st class
most_expensive_to_cheapest_1st_class = most_expensive_tickets_by_class[1.0] / cheapest_tickets_by_class[1.0]
print(f'The 1st class most expensive ticket was {round(most_expensive_to_cheapest_1st_class, 2)} times more expensive than the cheapest one.')

# how many times was the most expensive more expensive than the cheapest in the 2nd class
most_expensive_to_cheapest_2nd_class = most_expensive_tickets_by_class[2.0] / cheapest_tickets_by_class[2.0]
print(f'The 2nd class most expensive ticket was {round(most_expensive_to_cheapest_2nd_class, 2)} times more expensive than the cheapest one.')

# how many times was the most expensive more expensive than the cheapest in the 3rd class
most_expensive_to_cheapest_3rd_class = most_expensive_tickets_by_class[3.0] / cheapest_tickets_by_class[3.0]
print(f'The 3rd class most expensive ticket was {round(most_expensive_to_cheapest_3rd_class, 2)} times more expensive than the cheapest one.')

print()
print()



bodies_not_found = df['body_no'].isnull().sum()
print(f"{bodies_not_found} bodies have never been found.")