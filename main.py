 #import Modules
from src.load_data import load_data
from src.preprocessing import *
from src.analysis import *
from src.visualization import *
from src.report import generate_report

import os
def main():
    try:

        #create the required floder
        os.makedirs("images",exist_ok=True)
        os.makedirs("report",exist_ok=True)

        #lode the dateset
        print("\n"+"="*60)
        print("Lodeing Dataset")
        print("="*60)

        df= load_data("data/employee_data.csv")

        validate_dataset(df)

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

        get_highest_salary(df)

        get_lowest_salary(df)

        department_average_salary(df)

        city_salary(df)

        gender_salary(df)

        education_salary(df)

        performance_count(df)

        work_mode_count(df)

        get_top_5_salaries(df)

        get_bottom_5_salaries(df)


        print("\n" + "="*60)
        print("DATA VISUALIZATION")
        print("="*60)

        plot_age_distribution(df)

        plot_salary_distribution(df)

        plot_department_count(df)

        plot_gender_count(df)

        plot_education_count(df)

        plot_workmode_count(df)

        plot_performance_count(df)

        plot_salary_boxplot(df)

        plot_age_boxplot(df)

        plot_experiance_vs_salary(df)

        plot_department_salary(df)

        plot_city_salary(df)

        plot_departmenat_pie(df)

        #Genert PDF Report

        print("\n" +"="*60)
        print("Genert PDF Repor")
        print("=" * 60)

        generate_report(df)

        #Project Completed
        print("\n" +"="*60)
        print("Project Completed successfully")
        print("="*60)

    except Exception as error:
        print("\n" + "=" * 60)
        print("An unexpected error occurred.")
        print(f"Error: {error}")
        print("Project terminated safely.")
        print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Unexpected error: {error}")