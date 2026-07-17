import pandas as pd

def dataset_info(df):
    print("\n--------First 5 row-------")
    print(df.head())


    print("\n--------last 5 row--------")
    print(df.tail())


    print("\n--------dataset info-------")
    print(df.info())

    print("\n--------Shape of dataset-------")
    print(df.shape)

    print("\n------------columns-----------")
    print(df.columns)

    print("\n--------Data Types-------")
    print(df.dtype)


    print("\n--------Stastical summery -------")
    print(df.describe())


def check_missing_values(df):
    print("\n--------check missinf values-------")
    print(df.isnull().sum())


def check_duplicates(df):
    print("\n--------Duplicate Records--------")
    print(df.duplicated().sum())

def remove_duplicates(df):
    df = df.drop_duplicates()
    return df

def seave_clean_data(df):
    df.to_csv("data/employee_cleaned.csv",index=False)
    print("\n clean dataset saved succesfully.")





