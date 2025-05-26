import matplotlib.pyplot as plt
import pandas as pd


""" Clean my data frame - custom module by Patryk Ostrowski
The purpose of this module is for you to conduct initial data frame analysis by:

1) summarizing sum of numeric values in each column.
Method name: sumNumbersOfEachColumn()
Method argument: data frame

2) counting all empty and not empty values - the method gives you count of values not empty as integer
and also series of values null and another series of values not null.
Method name: sumNotEmptyAndNullAndNotNull()
Method argument: data frame

3) getting rid of all rows that contain at least one null; in some cases the data set may be purged -  
because of that the method shows how much data left.
At the end the method generates .csv file with a result data frame.
Method name: dropAllNas()
Method argument: data frame

4) filling up all cells that contain null.
In the contrary to the previous method you will never loose a single bit of data.
At the end the method generates .csv file with a result data frame.
Method name: fillMissingData()
Method argument: data frame.
"""


"""
Read your .csv file here
"""
#df = pd.read_csv('25__iris.csv')
df = pd.read_csv('26__titanic.csv')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


"""
Explore the data set - summarize values in each numeric column.
"""
def sumNumbersOfEachColumn(df):
    print(f'Summarizing each column procedure is starting...')
    for column in df.columns:
        column_type = df[column].dtype
        if column_type != 'object':
            column_sum = df[column].sum()
            column_avg = df[column].mean()
            column_median = df[column].median()
            column_min = df[column].min()
            column_max = df[column].max()
            print(f'The column {column} sum is: {column_sum}.')
            print(f'The column {column} average value is: {column_avg}.')
            print(f'The column {column} median is: {column_median}.')
            print(f'The column {column} minimum value is: {column_min}.')
            print(f'The column {column} maximum value is: {column_max}.')


    print(f'Summarizing done.')
    print()


"""
Explore the data set - count not empty values, null and notnull.
"""
def sumNotEmptyAndNullAndNotNull(df):
    print(f'Verifying empty values procedure is starting...')
    for column in df.columns:
        column_count = df[column].count()
        null_count = df[column].isnull().sum()
        not_null_count = df[column].notnull().sum()
        print(f'The column {column} contains {column_count} not empty values,'
              f' {null_count} values null and {not_null_count} values not null.')


    print(f'Empty values counted.')
    print()


"""
Get rid of all rows containing no data - this method may result in an empty data set.
Get the .csv file as the outcome.
"""
def dropAllNas(df):
    print(f'Getting rid of missing data procedure is starting...')
    intial_df_length = len(df)
    df_copy = df.copy()
    df_copy = df_copy.dropna()
    print(f'All empty values dropped - the data set looks like that:')
    print(df_copy.to_string())
    print(f'All missing data dropped.')
    final_df_length = len(df_copy)
    difference = intial_df_length - final_df_length
    print(f'The data frame was {intial_df_length} long. Now it is {final_df_length} long. {difference} rows have been removed.')
    df_copy.to_csv('Data frame with no null.csv', index=False)
    print()


"""
Replace missing information with fake generic information. Get the .csv file as the outcome. 
"""
def fillMissingData(df):
    print(f'Filling up missing data with dummy data procedure is starting...')
    df_copy = df.copy()
    modifications_counter = 0
    for column in df_copy.columns:
        column_type = df_copy[column].dtype
        if column_type == 'int64':
            df_copy[column] = df_copy[column].fillna(0)
            modifications_counter += 1
        elif column_type == 'float64':
            df_copy[column] = df_copy[column].fillna(0)
            modifications_counter += 1
        elif column_type == 'object':
            df_copy[column] = df_copy[column].fillna("dummy value")
            modifications_counter += 1
        else:
            df_copy[column] = df_copy[column].fillna(-1)
            modifications_counter += 1


    print(f'All missing values filled in - the data set looks like that:')
    print(df_copy.to_string())
    print()
    print(f'{modifications_counter} modifications against the data frame have been applied.')
    df_copy.to_csv('Data frame with empty values overriden.csv', index=False)
    print(f'The program has ended.')
    print()


"""
Run them all
"""
# sumNumbersOfEachColumn(df)
# sumNotEmptyAndNullAndNotNull(df)
# dropAllNas(df)
# fillMissingData(df)


# histogram
# df.hist()
# plt.show()
#
# df['pclass'].hist(bins=3)
# plt.title('Class histogram')
# plt.xlabel('Class number')
# plt.ylabel('Sum of')
# plt.show()
#
# df['survived'].hist(bins=2)
# plt.title('Survived/not survived histogram')
# plt.xlabel('Survived or not')
# plt.ylabel('Sum of')
# plt.show()
#
# df['age'].hist(bins=20)
# plt.title('Age histogram')
# plt.xlabel('Age value')
# plt.ylabel('Sum of')
# plt.show()
#
# df['sibsp'].hist(bins=10)
# plt.title('Siblings/spouse histogram')
# plt.xlabel('Siblings or spouse')
# plt.ylabel('Sum of')
# plt.show()
#
# df['parch'].hist(bins=10)
# plt.title('Parents/children histogram')
# plt.xlabel('Parents or children')
# plt.ylabel('Sum of')
# plt.show()
#
# df['ticket'].hist(bins=100)
# plt.title('Ticket no. histogram')
# plt.xlabel('Ticket no.')
# plt.ylabel('Sum of')
# plt.show()
#
# df['fare'].hist(bins=100)
# plt.title('Fare price histogram')
# plt.xlabel('Price')
# plt.ylabel('Sum of')
# plt.show()
#
# df['cabin'].hist(bins=100)
# plt.title('Cabin no. histogram')
# plt.xlabel('Cabin no.')
# plt.ylabel('Sum of')
# plt.show()
#
# df['embarked'].hist(bins=3)
# plt.title('Embarkment port histogram')
# plt.xlabel('Port')
# plt.ylabel('Sum of')
# plt.show()
#
# df['boat'].hist(bins=100)
# plt.title('Boat no. histogram')
# plt.xlabel('Boat no.')
# plt.ylabel('Sum of')
# plt.show()
#
# df['body'].hist(bins=50)
# plt.title('Body no. histogram')
# plt.xlabel('Body no.')
# plt.ylabel('Sum of')
# plt.show()


# pie chart
df['pclass'].value_counts().sort_index().plot(
    kind='pie',
    autopct='%1.1f%%',
    labels=['1st class', '2nd class', '3rd class'],
    legend=False
)
plt.title('Classes')
plt.ylabel('')
plt.show()

df['survived'].value_counts().sort_index().plot(
    kind='pie',
    autopct='%1.1f%%',
    labels=['Did not survive', 'Survived'],
    legend=False
)
plt.title('Survivors vs. non-survivors')
plt.ylabel('')
plt.show()

df['age'].value_counts().sort_index().plot(
    kind='pie',
    autopct='%1.1f%%',
    label='Age',
    legend=False
)
plt.title('Age distribution')
plt.ylabel('')
plt.show()


# line plot
df.plot(kind='line', y='survived', x='age')
plt.title('Age of survivors')
plt.ylabel('Sum of')
plt.xlabel('Age')
plt.grid()
plt.show()


# bar plot
df.plot(kind='bar', y='survived', x='age')
plt.title('Age of survivors')
plt.ylabel('Sum of')
plt.xlabel('Age')
plt.grid()
plt.show()


# scatter plot
df.plot(kind='scatter', y='survived', x='age')
plt.title('Age of survivors')
plt.ylabel('Sum of')
plt.xlabel('Age')
plt.grid()
plt.show()

# 3d scatter plot
df['sex_num'] = df['sex'].map({'male' : 0, 'female' : 1})
df.plot(
    kind='scatter',
    x='age',
    y='survived',
    c='sex_num',
    cmap='bwr',
    alpha=0.6,
    title='Survived gender'
)
plt.ylabel('Survived or no')
plt.xlabel('Age')
plt.grid()
plt.show()

# 3d scatter plot
df['sex_num'] = df['sex'].map({'male' : 0, 'female' : 1})
df.plot(
    kind='scatter',
    x='age',
    y='fare',
    c='sex_num',
    cmap='bwr',
    alpha=0.6,
    title='Cost per gender in numbers'
)
plt.ylabel('Cost')
plt.xlabel('Age')
plt.grid()
plt.show()