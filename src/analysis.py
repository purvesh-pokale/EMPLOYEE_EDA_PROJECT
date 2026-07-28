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