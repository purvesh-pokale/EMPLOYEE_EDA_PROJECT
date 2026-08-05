def average_salary(df):
    print("\n Average Salary")
    print(df["Salary"].mean())

def get_highest_salary(df):
    print("\n highest Salary")
    print(df["Salary"].max())

def get_lowest_salary(df):
    print("\n lowest Salary")
    print(df["Salary"].min())

def department_average_salary(df):
    print("\n Average salary by department")
    print(df.groupby("Department")["Salary"].mean())

def city_salary(df):
    print("\n Average salary by city")
    print(df.groupby("City")["Salary"].mean())

def gender_salary(df):
    print("\n Average salary by gender")
    print(df.groupby("Gender")["Salary"].mean())

def education_salary(df):
    print("\n Average salary by education")
    print(df.groupby("Education")["Salary"].mean())

def performance_count(df):
    print("\n Performance count")
    print(df["Performance"].value_counts())

def work_mode_count(df):
    print("\n work mode count")
    print(df["Work_Mode"].value_counts())

def get_top_5_salaries(df):
    print("\nTop 5 Salary")
    print(df.nlargest(5,"Salary"))

def get_bottom_5_salaries(df):
    print("\nBottom 5 lowest paid Employees")
    print(df.nsmallest(5, "Salary"))


def correlation_analysis(df):
    """
    Calculates and displays the correlation matrix
    for the numerical columns in the dataset.
    """

    print("\nCorrelation Analysis")

    numerical_columns = [
        "Age",
        "Experience",
        "Salary",
        "Performance"
    ]

    correlation_matrix = df[numerical_columns].corr()

    print(correlation_matrix)

    return correlation_matrix

def get_correlation_matrix(df):
    numerical_columns = [
        "Age",
        "Experience",
        "Salary",
        "Performance"
    ]

    return df[numerical_columns].corr()


def correlation_analysis(correlation_matrix):
    print("\nCorrelation Analysis")
    print(correlation_matrix)


def detect_outliers_iqr(df, column):
    """
    Detect outliers in a numerical column using the IQR method.
    """

    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)

    iqr = q3 - q1

    lower_limit = q1 - (1.5 * iqr)
    upper_limit = q3 + (1.5 * iqr)

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print(f"\nOutlier Analysis - {column}")
    print(f"Lower Limit : {lower_limit:.2f}")
    print(f"Upper Limit : {upper_limit:.2f}")
    print(f"Number of Outliers : {len(outliers)}")

    if not outliers.empty:
        print(outliers)

    return {
        "column": column,
        "lower_limit": lower_limit,
        "upper_limit": upper_limit,
        "count": len(outliers),
        "data": outliers
    }