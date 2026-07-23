import os
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import(
    SimpleDocTemplate,
    paragraph,
    Spacer
)

def genert_report(df):

    os.makedirs("reports",exist_ok=True)

    pdf = SimpleDocTemplate(
        "report/Final_Report.pdf"
    )
    styles = getSampleStyleSheet()
    elements = []

    #Titale
    elements.append(
        paragraph(
            "Employee Exploratory Data Analysis Report",
            styles["Title"]
        )
    )
    elements.append(Spacer(1,20))

    #Dataset Summery
    elements.append(
        paragraph(
            "<b>Dataset Summery</b>",
            styles["Heading2"]

        )
    )
    elements.append(
        paragraph(
            f"Total Employees :{len(df)}",
            styles["BodyText"]
        )
    )
    elements.append(
        paragraph(
            f"Total columns : {len(df.columns)}",
            styles["BodyText"]
        )
    )

    elements.append(
        paragraph(
            f"Missing Value: {df.isnull().sum()}",
            styles["BodyText"]
        )
    )

    elements.append(
        paragraph(
            f"Duplicate Rows : {df.duplicated().sum()}",
            styles["BodyText"]
        )
    )
    elements.append(Spacer(1,20))


#Salary Analysis
    elements.append(
        paragraph(
            "<b>Salary Analysis </b>",
            styles["Heading2"]
        )
    )
    elements.append(
        paragraph(
            f"Averages Salary :RS {df["Salary"].mean():,.2f}",
            styles=["BodyText"]
        )
    )
    
    elements. append(
        paragraph(
            f"Highest Salary : ₹{df['Salary'].max():,.2f}",
            styles["BodyText"]
        )
    )

    elements.append(
        paragraph(
            f"Lowest Salary : ₹{df['Salary'].min():,.2f}",
            styles["BodyText"]
        )
    )
    elements.append(Spacer(1,20))

    #Business Insights

    elements.append(
        paragraph(
            "<b> Business Insights </b>",
            styles["Heading2"]
        )
    )

    elements.append(
        paragraph(
            f"Highest Paying Department :"
            f"{df.groupby("Department")["Salary".mean().idxmax]}",
            styles["BodyText"]
        )
    )


