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

#df = pd.read_csv('25__iris.csv')
df = pd.read_csv('26__titanic.csv')

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

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

sumNumbersOfEachColumn(df)
sumNotEmptyAndNullAndNotNull(df)
dropAllNas(df)
fillMissingData(df)