import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Read data from CSV
data = pd.read_csv('data.csv')

# Create a PDF
c = canvas.Canvas("report.pdf", pagesize=letter)
width, height = letter

# Title
c.setFont("Helvetica-Bold", 16)
c.drawString(180, height - 50, "Student Performance Report")

# Content
c.setFont("Helvetica", 12)
y = height - 100

for index, row in data.iterrows():
    text = f"Name: {row['Name']} | Grade: {row['Grade']} | Marks: {row['Marks']}"
    c.drawString(50, y, text)
    y -= 20
    if y < 50:
        c.showPage()
        c.setFont("Helvetica", 12)
        y = height - 50

c.save()
print("✅ PDF successfully generated as 'report.pdf'")


