import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import(
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

def generate_report(df):

    os.makedirs("report",exist_ok=True)

    pdf = SimpleDocTemplate(
        "report/Final_Report.pdf"
    )
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

    pdf.build(elements)


print("PDF Report Generated Successfully!")

