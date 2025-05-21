import pandas as pd
import matplotlib.pyplot as plt

# Konfiguracja: wyświetlaj wszystko
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


df = pd.read_csv('26__titanic.csv')

# sniff data
print('###################################################')
print('################ MEET THE DATA SET ################')
print('###################################################')
print(df.sample(5).to_string())
print()


# rename columns and sniff data again
print('###################################################')
print('################# RENAMED COLUMNS #################')
print('###################################################')
df.columns = ['class', 'survived', 'full_name', 'sex', 'age', 'siblings/spouse', 'parents/children', 'ticket_no', 'fare_price', 'cabin_no', 'embarked', 'boat_no', 'body_no', 'destination']
print(df.sample(15).to_string())
print()

# analyze facts
print('##################################################')
print('##### A FEW QUICK FACTS ON THE CIRCUMSTANCES #####')
print('##################################################')
total_passengers = 2200
passengers_in_this_set = len(df)
print(f'{total_passengers} traveled in total. This set analyses {passengers_in_this_set} persons who have been found either alive or dead.')
missing_passengers = total_passengers - passengers_in_this_set
print(f'What happened to {missing_passengers} is unknown.')
bodies_not_found = df['body_no'].isnull().sum()
survivors = (df['survived'] == 1).sum()
print(f'{bodies_not_found} bodies have never been found.')
print(f'{survivors} persons out of {passengers_in_this_set} survived.')
non_survivors = (df['survived'] == 0).sum()
print(f'{non_survivors} passengers {passengers_in_this_set} death has been confirmed.')
print()


# data set analysis
print('#################################################')
print('############### DATA SET ANALYSIS ###############')
print('#################################################')
if df['survived'].isnull().sum() > 0:
    print('At least one information on survived/not-survived is missing.')


if df['class'].isnull().sum() > 0:
    print('At least one information on the class assignment is missing.')

print()
print('Data types:')
print(df.dtypes)

print()

# the analysis starts here
print('###################################################')
print('############ PURE ANALYSIS STARTS HERE ############')
print('###################################################')
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
surviving_ratio_first_class = round(first_class_survivors / passengers_in_this_set * 100, 2)
print(f'Your chance to survive as the 1st class passenger was {surviving_ratio_first_class}%')
print()

# 2nd class surviving ratio analysis
second_class_survivors = ( (df['class'] == 2) & (df['survived'] == 1) ).sum()
print('2nd class survivors', second_class_survivors)

second_class_non_survivors = ( (df['class'] == 2) & (df['survived'] == 0) ).sum()
print('2nd class non-survivors', second_class_non_survivors)
surviving_ratio_second_class = round(second_class_survivors / passengers_in_this_set * 100, 2)
print(f'Your chance to survive as the 2nd class passenger was {surviving_ratio_second_class}%')
print()

# 3rd class surviving ratio analysis
third_class_survivors = ( (df['class'] == 3) & (df['survived'] == 1) ).sum()
print('3rd class survivors', third_class_survivors)

third_class_non_survivors = ( (df['class'] == 3) & (df['survived'] == 0) ).sum()
print('3rd class non-survivors', third_class_non_survivors)
surviving_ratio_third_class = round(third_class_survivors / passengers_in_this_set * 100, 2)
print(f'Your chance to survive as the 3rd class passenger was {surviving_ratio_third_class}%')
print()

# correlation
class_survived_corr = df[["class", "survived"]].corr()
print(f'Class vs. survived correlation is:')
print(class_survived_corr)

# new variables for new data frame for charts drawing purposes
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
    'The cheapest tickets by class (excluding zeros): \n', cheapest_tickets_by_class
)
print()

most_expensive_tickets_by_class = prices_not_zero_df.groupby(['class'])['fare_price'].max()
print(
    'The most expensive tickets by class:\n', most_expensive_tickets_by_class
)
print()

# the cheapest vs. the most expensive tickets in 1st class
print(f'1st class cheapest ticket: {cheapest_tickets_by_class[1.0]}')
print(f'1st class most expensive ticket: {most_expensive_tickets_by_class[1.0]}')
print()

# the cheapest vs. the most expensive tickets in 2n class
print(f'2nd class cheapest ticket: {cheapest_tickets_by_class[2.0]}')
print(f'2nd class most expensive ticket: {most_expensive_tickets_by_class[2.0]}')
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

# how many times was the most expensive ticket more expensive than the cheapest in the 1st class
most_expensive_to_cheapest_1st_class = most_expensive_tickets_by_class[1.0] / cheapest_tickets_by_class[1.0]
print(f'The 1st class most expensive ticket was {round(most_expensive_to_cheapest_1st_class, 2)} times more expensive than the cheapest one.')

# how many times was the most expensive ticket more expensive than the cheapest in the 2nd class
most_expensive_to_cheapest_2nd_class = most_expensive_tickets_by_class[2.0] / cheapest_tickets_by_class[2.0]
print(f'The 2nd class most expensive ticket was {round(most_expensive_to_cheapest_2nd_class, 2)} times more expensive than the cheapest one.')

# how many times was the most expensive ticket more expensive than the cheapest in the 3rd class
most_expensive_to_cheapest_3rd_class = most_expensive_tickets_by_class[3.0] / cheapest_tickets_by_class[3.0]
print(f'The 3rd class most expensive ticket was {round(most_expensive_to_cheapest_3rd_class, 2)} times more expensive than the cheapest one.')

print()

# each column from among of 'survived', 'siblings/spouse', and 'parents/children' has nulls so data is not consistent - a new data frame is needed
print('Problematic columns:')
print(df['survived'].isnull().sum(), 'rows is not a number for column "survived"')
print(df['siblings/spouse'].isnull().sum(), 'rows is not a number for column "siblings/spouse"')
print(df['parents/children'].isnull().sum(), 'rows is not a number for column "parents/children"')
print()

# new data frame created because of the above:
not_null_passengers_df = df.copy()
not_null_passengers_df = not_null_passengers_df.dropna(subset=['siblings/spouse', 'parents/children'])

# confirm that the data is consistent around the columns of interest
print('Because of the above, the following data frame has been created to exclude missing data:')
print(not_null_passengers_df['survived'].isnull().sum(), 'rows is not a number for column "survived"')
print(not_null_passengers_df['siblings/spouse'].isnull().sum(), 'rows is not a number for column "siblings/spouse"')
print(not_null_passengers_df['parents/children'].isnull().sum(), 'rows is not a number for column "parents/children"')
print()

# conduct data mining
print('############################################################')
print('# CHANCES TO SURVIVE - ALONE vs. WITH ADULTS vs. WITH KIDS #')
print('############################################################')
traveling_alone = ((not_null_passengers_df['siblings/spouse'] == 0) & (not_null_passengers_df['parents/children'] == 0)).sum()
survivors_traveling_alone = ((not_null_passengers_df['survived'] == 1) & (not_null_passengers_df['siblings/spouse'] == 0) & (not_null_passengers_df['parents/children'] == 0)).sum()
non_survivors_traveling_alone = ((not_null_passengers_df['survived'] == 0) & (not_null_passengers_df['siblings/spouse'] == 0) & (not_null_passengers_df['parents/children'] == 0)).sum()
chance_to_survive_traveling_alone = survivors_traveling_alone / traveling_alone * 100
print(f'{traveling_alone} passengers traveled alone - {survivors_traveling_alone} survived while {non_survivors_traveling_alone} did not survive so traveling alone your chance to survive was {round(chance_to_survive_traveling_alone, 2)}%.')

traveling_with_siblings_spouse = (not_null_passengers_df['siblings/spouse'] != 0).sum()
survivors_traveling_with_siblings_spouse = ((not_null_passengers_df['survived'] == 1) & (not_null_passengers_df['siblings/spouse'] != 0)).sum()
non_survivors_traveling_with_siblings_spouse = ((not_null_passengers_df['survived'] == 0) & (not_null_passengers_df['siblings/spouse'] != 0)).sum()
chance_to_survive_traveling_with_siblings_spouse = survivors_traveling_with_siblings_spouse / traveling_with_siblings_spouse * 100
print(f'{traveling_with_siblings_spouse} passengers traveled with siblings or spouse - {survivors_traveling_with_siblings_spouse} survived while {non_survivors_traveling_with_siblings_spouse} did not survive so traveling with siblings or spouse your chance to survive was {round(chance_to_survive_traveling_with_siblings_spouse, 2)}%')

traveling_with_parents_children = (not_null_passengers_df['parents/children'] != 0).sum()
survivors_traveling_with_parents_children = ((not_null_passengers_df['survived'] == 1) & (not_null_passengers_df['parents/children'] != 0) ).sum()
non_survivors_traveling_with_parents_children = ((not_null_passengers_df['survived'] == 0) & (not_null_passengers_df['parents/children'] != 0)).sum()
chance_to_survive_traveling_with_parents_children = survivors_traveling_with_parents_children / traveling_with_parents_children * 100
print(f'{traveling_with_parents_children} passengers traveled with parents or children - {survivors_traveling_with_parents_children} survived while {non_survivors_traveling_with_parents_children} did not survive so traveling with parents or children your chance to survive was {round(chance_to_survive_traveling_with_parents_children, 2)}%')

print()

# the youngest and the oldest survivors and non-survivors
print('###################################################')
print('# YOUNGEST AND OLDEST SURVIVORS AND NON-SURVIVORS #')
print('###################################################')
youngest_survived = df[df['survived'] == 1]['age'].min()
print(f'The youngest survivor was {round(youngest_survived, 2)} years old.')

oldest_survived = df[df['survived'] == 1]['age'].max()
print(f'The oldest survivor was {round(oldest_survived, 2)} years old.')

average_survivor_age = df[df['survived'] == 1]['age'].mean()
print(f'Survivor average age was {round(average_survivor_age, 2)} years old.')

median_survivor_age = df[df['survived'] == 1]['age'].median()
print(f'Median of the survivor age was {round(median_survivor_age, 2)}.')

print()

youngest_non_survivor = df[df['survived'] == 0]['age'].min()
print(f'The youngest non-survivor was {round(youngest_non_survivor, 2)} years old.')

oldest_non_survivor = df[df['survived'] == 0]['age'].max()
print(f'The oldest non-survivor was {round(oldest_non_survivor, 2)} years old.')

average_non_survivor_age = df[df['survived'] == 0]['age'].mean()
print(f'Non-survivors average age was {round(average_non_survivor_age, 2)} years old.')

median_non_survivor_age = df[df['survived'] == 0]['age'].median()
print(f'Median of non-survivors age was {round(median_non_survivor_age, 2)}.')

print()
print('##################################################')
print('####### AGE & SUM OF SURVIVORS AT EACH AGE #######')
print('##################################################')
df_clean = df[['age', 'survived']].dropna()
df_clean['age'] = df_clean['age'].astype(int)
survivors_by_age = df_clean.groupby('age')['survived'].sum().astype(int)
print(survivors_by_age)

plt.figure(figsize=(12, 6))
survivors_by_age.plot(kind='bar')

plt.title('Number of survivors by age')
plt.xlabel('Age')
plt.ylabel('Number of survivors')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

print()

print('##################################################')
print('############# % OF SURVIVORS PER SEX #############')
print('##################################################')
women_traveled = df[df['sex'] == 'female'].shape[0]
print(f'{int(women_traveled)} woman traveled.')
women_survied = df[df['sex'] == 'female']['survived'].sum()
print(f'{int(women_survied)} woman survived.')
print()

men_traveled = df[df['sex'] == 'male'].shape[0]
print(f'{int(men_traveled)} woman traveled.')
men_survied = df[df['sex'] == 'male']['survived'].sum()
print(f'{int(men_survied)} woman survived.')
print()

women_chance_to_survive = women_survied / women_traveled * 100
print(f'Woman had {round(women_chance_to_survive, 2)}% chance to survive.')
print()

men_chance_to_survive = men_survied / men_traveled * 100
print(f'Men had {round(men_chance_to_survive, 2)}% chance to survive.')
print()