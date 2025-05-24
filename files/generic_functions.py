import pandas as pd

df = pd.read_csv('metody_df.csv')

def sumNumbersOfEachColumn(df):
    print(f'Function sumNumbersOfEachColumn starts...')
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


    print(f'Function sumNumbersOfEachColumn has ended.')
    print()


def sumNotEmptyAndNullAndNotNull(df):
    print(f'Function sumNotEmptyAndNullAndNotNull starts...')
    for column in df.columns:
        column_count = df[column].count()
        null_count = df[column].isnull().sum()
        not_null_count = df[column].notnull().sum()
        print(f'The column {column} contains {column_count} not empty values,'
              f' {null_count} values null and {not_null_count} values not null.')


    print(f'Function sumNotEmptyAndNullAndNotNull has ended.')
    print()


sumNumbersOfEachColumn(df)
sumNotEmptyAndNullAndNotNull(df)