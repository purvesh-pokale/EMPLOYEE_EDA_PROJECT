import os

from datetime import datetime
from reportlab.lib import colors
from reportlab.platypus import PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import(
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    PageBreak,
    KeepTogether
)


def add_page_number(canvas, doc):
    """
    Adds the current page number to the bottom-right corner of each page.
    """
    page_num = canvas.getPageNumber()

    canvas.drawRightString(
        550,
        20,
        f"Page {page_num}"
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

    # Dataset Summary
    elements.append(
        Paragraph(
            "<b>Dataset Summary :-</b>",
            styles["Heading2"]

        )
    )

    summary_data = [
        ["Metric", "Value"],
        ["Total Employees", len(df)],
        ["Total Columns", len(df.columns)],
        ["Missing Values", int(df.isnull().sum().sum())],
        ["Duplicate Rows", df.duplicated().sum()]
    ]

    summary_table = Table(summary_data)
    summary_table.hAlign = "LEFT"

    summary_table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

        ("GRID", (0, 0), (-1, -1), 1, colors.black),

        ("BACKGROUND", (0, 1), (-1, -1), colors.beige)
    ])
    )

    elements.append(summary_table)
    
    elements.append(Spacer(1,20))


    #Salary Analysis
    elements.append(
        Paragraph(
            "<b>Salary Analysis :- </b>",
            styles["Heading2"]
        )
    )

    salary_data = [
    ["Salary Metric", "Amount"],
    ["Average Salary", f"Rs {df['Salary'].mean():,.2f}"],
    ["Highest Salary", f"Rs{df['Salary'].max():,.2f}"],
    ["Lowest Salary", f"Rs {df['Salary'].min():,.2f}"]
    ]

    salary_table = Table(salary_data)
    salary_table.hAlign = "LEFT"

    salary_table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige)
    ])
    )

    elements.append(salary_table)
    
    elements.append(Spacer(1,20))



    #Business Insights

    elements.append(
        Paragraph(
            "<b> Business Insights :- </b>",
            styles["Heading2"]
        )
    )

    business_insights_data =[
        ["Business Insight", "Value"],
        ["Highest Paying Department", f"{df.groupby('Department')['Salary'].mean().idxmax()}"],
        ["Most Common Work Mode", f"{df['Work_Mode'].mode()[0]}"],
        ["Highest Performance Rating", f"{df['Performance'].max()}"],
        ["Most Common Education", f"{df['Education'].mode()[0]}"]
    ]

    business_insights_table= Table(business_insights_data)
    business_insights_table.hAlign= "LEFT"

    business_insights_table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige)
    ])
    )

    elements.append(business_insights_table)
    elements.append(Spacer(1,20))

#Recomandations
    elements.append(
        Paragraph(
            "<b>Recommdations :-</b>",
            styles["Heading2"]
        )
    )

    recommendations = [
        "1. Review salary structure across departments.",
        "2. Encourage employee skill development.",
        "3. Improve performance evaluation process.",
        "4. Monitor salary outliers regularly.",
        "5. Continue data-driven HR decision making."
    ]

    for rec in recommendations:
        elements.append(
            Paragraph(
                rec,
                styles["BodyText"]
            )
        )

    
#charts
    elements.append(PageBreak())

    elements.append(
        Paragraph(
            "<b>Charts</b>",
            styles["Heading2"]
        )
    )

    elements.append(Spacer(1, 15))


    charts = [
        ("Age Distribution", "images/age_distribution.png"),
        ("Department Count", "images/department_count.png"),
        ("Gender Distribution", "images/gender_distribution_count.png"),
        ("Work Mode Distribution", "images/workmode_Distribution.png"),
        ("Salary Distribution", "images/Salary_distribution.png"),
        ("Salary Boxplot", "images/salary_boxplot.png"),
        ("Experience vs Salary", "images/experiance_vs_salary.png")
    ]

    for chart_title, chart_path in charts:

        chart_elements = []

        chart_elements.append(
            Paragraph(
                f"<b>{chart_title}</b>",
                styles["Heading3"]
            )
        )

        if os.path.exists(chart_path):
            chart_elements.append(
                Image(
                    chart_path,
                    width = 400,
                    height = 230, 
                )
            )
        else:
            chart_elements.append(
                Paragraph(
                    f"Image not found : {chart_path}",
                    styles["BodyText"]
                )
            )

        chart_elements.append(
            Spacer(1, 20)
        )

        elements.append(
            KeepTogether(chart_elements)
        )

    #Build pdf
    try:
        pdf.build(
            elements,
            onFirstPage=add_page_number,
            onLaterPages=add_page_number
        )
    
        print("=" * 50)
        print("Final PDF Report Generated Successfully!")
        print(f"Saved as: {filename}")
        print("=" * 50)
    
    except PermissionError:
        print("Permission denied. Please close the PDF file and try again.")
    
    except OSError as error:
        print(f"Unable to generate PDF report: {error}")
    






