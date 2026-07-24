from datetime import datetime
import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import(
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

def generate_report(df):

    os.makedirs("report",exist_ok=True)

    filename = datetime.now().strftime(
        "report/Final_Report_%Y%m%d_%H%M%S.pdf"
    )

    pdf = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()
    elements = []

    #Titale
    elements.append(
        Paragraph(
            "Employee Exploratory Data Analysis Report",
            styles["Title"]
        )
    )
    elements.append(Spacer(1,20))

    #Dataset Summery
    elements.append(
        Paragraph(
            "<b>Dataset Summery</b>",
            styles["Heading2"]

        )
    )
    elements.append(
        Paragraph(
            f"Total Employees :{len(df)}",
            styles["BodyText"]
        )
    )
    elements.append(
        Paragraph(
            f"Total columns : {len(df.columns)}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Missing Value: {df.isnull().sum()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Duplicate Rows : {df.duplicated().sum()}",
            styles["BodyText"]
        )
    )
    elements.append(Spacer(1,20))


#Salary Analysis
    elements.append(
        Paragraph(
            "<b>Salary Analysis </b>",
            styles["Heading2"]
        )
    )
    elements.append(
        Paragraph(
            f"Averages Salary :RS {df['Salary'].mean():,.2f}",
            styles["BodyText"]
        )
    )
    
    elements.append(
        Paragraph(
            f"Highest Salary : ₹{df['Salary'].max():,.2f}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Lowest Salary : ₹{df['Salary'].min():,.2f}",
            styles["BodyText"]
        )
    )
    elements.append(Spacer(1,20))

    #Business Insights

    elements.append(
        Paragraph(
            "<b> Business Insights </b>",
            styles["Heading2"]
        )
    )

    elements.append(
        Paragraph(
            f"Highest Paying Department :"
            f"{df.groupby('Department')['Salary'].mean().idxmax()}",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            f"Most Common Workmode : "
            f"{df['Work_Mode'].mode()[0]}",
            styles["BodyText"]
        )
    )
    elements.append(
        Paragraph(
            f"Higest Performance Rating : "
            f"{df['Performance'].max()}",
            styles["BodyText"]
        )
    )
    elements.append(
        Paragraph(
            f"Most common Education :"
            f"{df['Education'].mode()[0]}",
            styles["BodyText"]
        )
    )
    elements.append(Spacer(1,20))

#Recomandations
    elements.append(
        Paragraph(
            "<b>Recommdations</b>",
            styles["Heading2"]
        )
    )
    elements.append(
        Paragraph(
        "1.Review Salary Structure CROSS department.",
        styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            "2. Encourage Employee Skill development.",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            "3.Improve performance evaluation process.",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            "4.Monitor salary outliers regularly.",
            styles["BodyText"]
        )
    )

    elements.append(
        Paragraph(
            "5. Continue data-driven HR decision making.",
            styles["BodyText"]
        )
    )
    

    #Build pdf
    pdf.build(elements)
    print("="*50)
    print(f"Final PDF Report Generated Successfully!")
    print(f"Saved as: {filename}")
    print("="*50)




