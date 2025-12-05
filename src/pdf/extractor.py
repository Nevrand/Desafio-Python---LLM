# Importando o pdfplumber como nossa ferramenta principal para extração de texto
import pdfplumber

# Caminho do arquivo PDF a ser extraído
pdf_path = 'exemplos_pdf/exemplo.pdf'

# Extração de texto do PDF
texto = ''
with pdfplumber.open(pdf_path) as pdf:
    # Percorre todas as páginas do PDF
    for page in pdf.pages:
        texto += page.extract_text()
        
print(texto)