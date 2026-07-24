import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("images",exist_ok = True)   #it creat image folder automatically to save graps

def age_distribution(df):
    plt.figure(figsize = (8,5))
    sns.histplot(df["Age"],bins = 10, kde = True)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.savefig("images/age_distribution.png")
    plt.show()


def salary_distribution(df):
    plt.figure(figsize = (8,5))
    sns.histplot(df["Salary"],bins = 10, kde = True)
    plt.title("Salary Distribution")
    plt.xlabel("Salary")
    plt.ylabel("Count")
    plt.savefig("images/Salary_distribution.png")
    plt.show()

def department_count(df):
    plt.figure(figsize=(8,5))
    sns.countplot(x = "Department",data = df)
    plt.title("Department Count")
    plt.xlabel("Department")
    plt.ylabel("Employees")
    plt.xticks(rotation = 45)
    plt.savefig("images/department_count.png")
    plt.show()

def gender_count(df):
    plt.figure(figsize=(6,5))
    sns.countplot(x= "Gender", data = df)
    plt.title("Gender Distribution")
    plt.xlabel("Gender")
    plt.ylabel("count")
    plt.savefig("images/gender_distribution_count.png")
    plt.show()

def education_count(df):
    plt.figure(figsize=(8,5))
    sns. countplot(x="Education",data = df)
    plt.title("Education Distribution")
    plt.xlabel("Education")
    plt.ylabel("Count")
    plt.savefig("images/education_distribution.png")
    plt.show()

def workmode_count(df):
    plt.figure(figsize=(8,5))
    sns.countplot(x="Work_Mode",data=df)
    plt.title("Work Mode Distrubution")
    plt.xlabel("Work Mode")
    plt.ylabel("Count")
    plt.savefig("images/workmode_Distribution.png")
    plt.show()


def performance_count(df):
    plt.figure(figsize=(8,5))
    sns.countplot(x="Performance",data=df)
    plt.title("Performace Distribution")
    plt.xlabel("Performance Rateing")
    plt.ylabel("Count")
    plt.savefig("images/performance_distribution.png")
    plt.show()

def salary_boxplot(df):
    plt.figure(figsize=(8,5))
    sns.boxplot(y=df["Salary"])
    plt.title("Salary Boxplot")
    plt.savefig("images/salary_boxplot.png")
    plt.show()

def age_boxplot(df):
    plt.figure(figsize=(8,5))
    sns.boxplot(y=df["Age"])
    plt.title("Age Boxplot")
    plt.savefig("images/age_boxplot.png")
    plt.show()

def experiance_vs_salary(df):
    plt.figure(figsize=(8,5))
    sns.scatterplot(
        x= "Experience",
        y = "Salary",
        hue= "Department",
        data = df
    )
    plt.title("Experience vs Salary")
    plt.savefig("images/experiance_vs_salary.png")
    plt.show()

def department_salary(df):
    plt.figure(figsize=(8,5))
    sns.barplot(

        x= "Department",
        y= "Salary",
        data= df
    )
    plt.title("Department vs Salary")
    plt.xticks(rotation = 45)
    plt.savefig("images/department_salary.png")
    plt.show()


def city_salary(df):
    plt.figure(figsize=(8,5))
    sns.barplot(
        x = "City",
        y = "Salary",
        data = df
    )
    plt.title("City vs Salary")
    plt.xticks(rotation = 45)
    plt.savefig("images/city_salary.png")
    plt.show()

def departmenat_pie(df):
    plt.figure(figsize=(7,7))
    df["Department"].value_counts().plot(
        kind = "pie",
        autopct = "%1.1f%%"
    )
    plt.title('Depatment_distribution')
    plt.ylabel("")
    plt.savefig("images/departmenat_pie.png")
    plt.show() 