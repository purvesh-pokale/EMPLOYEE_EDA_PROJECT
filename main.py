 #import Modules
from src.load_data import load_data
from src.preprocessing import *
from src.analysis import *
from src.visualization import *
from src.report import generate_report


#create the required floder
os.makedirs("images",exist_ok=True)
os.makedirs("report",exist_ok=True)

#lode the dateset
print("\n"+"="*60)
print("Lodeing Dataset")
print("="*60)

df= load_data("data/employee_data.csv")


# Data Preprocessing
print("\n"+"="*60)
print("DATA .PREPROCESSING")
print("="*60)

dataset_info(df)

check_missing_values(df)

check_duplicates(df)

df = remove_duplicates(df)

save_clean_data(df)

#Analysis
print("\n" +"="*60)
print("BUSINESS ANALYSIS")
print("="*60)

average_salary(df)

highest_salary(df)

lowest_salary(df)

department_salary(df)

city_salary(df)

gender_salary(df)

education_salary(df)

performance_count(df)

work_mode_count(df)

top_5_salary(df)

bottom_5_salary(df)


print("\n" + "="*60)
print("DATA VISUALIZATION")
print("="*60)

age_distribution(df)

salary_distribution(df)

department_count(df)

gender_count(df)

education_count(df)

workmode_count(df)

performance_count(df)

salary_boxplot(df)

age_boxplot(df)

experiance_vs_salary(df)

department_salary(df)

city_salary(df)

departmenat_pie(df)

#Genert PDF Report

print("\n" +"="*60)
print("Genert PDF Repor")
print("=" * 60)

generate_report(df)

#Project Completed
print("\n" +"="*60)
print("Project Completed successfully")
print("="*60)