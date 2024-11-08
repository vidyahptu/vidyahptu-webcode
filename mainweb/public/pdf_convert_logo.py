import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from PyPDF2 import PdfReader, PdfWriter
from reportlab.lib.units import inch

def add_logo_to_pdf(input_path, logo_path, output_path):
    temp_pdf_path = "temp.pdf"

    # Create a temporary PDF with the logo
    c = canvas.Canvas(temp_pdf_path, pagesize=A4)
    width, height = A4
    c.drawImage(logo_path, x=width/2 - 1*inch, y=height - 2*inch, width=2*inch, height=2*inch)
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 2.5*inch, "Your Title Here")
    c.showPage()
    c.save()

    # Read the original PDF
    reader = PdfReader(input_path)
    writer = PdfWriter()

    # Add the logo page as the first page
    temp_reader = PdfReader(temp_pdf_path)
    writer.add_page(temp_reader.pages[0])

    # Add the rest of the original PDF pages
    for page_num in range(len(reader.pages)):
        writer.add_page(reader.pages[page_num])

    # Write out the new PDF
    with open(output_path, 'wb') as out_f:
        writer.write(out_f)

    # Remove the temporary file
    os.remove(temp_pdf_path)

def process_folder(folder_path, logo_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            input_path = os.path.join(folder_path, filename)
            output_path = os.path.join(folder_path, f"logo_{filename}")
            add_logo_to_pdf(input_path, logo_path, output_path)

# Usage
folder_path = "pdf_output"
logo_path = "Capture.PNG"
process_folder(folder_path, logo_path)
