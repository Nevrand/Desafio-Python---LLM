
import pdfplumber

pdf_path = 'exemplo.pdf'

texto = ''
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        texto = page.extract_text()
        print(texto)
