from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(vulnerabilities, output_filename="vulnerability_report.pdf"):
    c = canvas.Canvas(output_filename, pagesize=letter)
    c.drawString(100, 750, "Vulnerability Assessment Report")
    c.drawString(100, 720, "Detected Vulnerabilities:")

    y = 700
    for vuln in vulnerabilities:
        c.drawString(100, y, f"- {vuln}")
        y -= 20
    
    c.save()
    print(f"Report saved as {output_filename}")
