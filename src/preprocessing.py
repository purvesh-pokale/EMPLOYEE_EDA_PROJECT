import pandas as pd

from src.constants import REQUIRED_COLUMNS


def validate_dataset(df: pd.DataFrame) -> None:
    """
    Validate the employee dataset before analysis.

    Args:
        df (pd.DataFrame): Employee dataset.

    Raises:
        ValueError: If the dataset is empty.
        ValueError: If required columns are missing.
    """

    # Check if the dataset is empty
    if df.empty:
        raise ValueError("The dataset is empty. Please provide a valid dataset.")

    # Check for missing columns
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {', '.join(missing_columns)}"
        )

def dataset_info(df):
    print("\n--------First 5 row-------")
    print(df.head())


    print("\n--------last 5 row--------")
    print(df.tail())


    print("\n--------dataset info-------")
    df.info()

    print("\n--------Shape of dataset-------")
    print(df.shape)

    print("\n------------columns-----------")
    print(df.columns)

    print("\n--------Data Types-------")
    print(df.dtypes)


    print("\n--------Statistical summery -------")
    print(df.describe())


def check_missing_values(df):
    print("\n--------check missing values-------")
    print(df.isnull().sum())


def check_duplicates(df):
    print("\n--------Duplicate Records--------")
    print(df.duplicated().sum())

def remove_duplicates(df):
    df = df.drop_duplicates()
    return df.drop_duplicates()

def save_clean_data(df):
    try:
        df.to_csv("data/employee_cleaned.csv", index=False)
        print("\nClean dataset saved successfully.")

    except PermissionError:
        print("Permission denied. Please close the CSV file and try again.")

    except OSError as error:
        print(f"Unable to save the cleaned dataset: {error}")





