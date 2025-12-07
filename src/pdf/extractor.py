import pdfplumber
import os

def extrairTexto(caminhoPdf):
    # Verificando se o PDF existe
    if not os.path.isfile(caminhoPdf):
        print("PDF não encontrado.")
        return {
            "texto": "",
            "numPaginas": 0
        }
    
    textoExtraido = ""
    numPaginas = 0

    # Abrindo o PDF
    try: 
        with pdfplumber.open(caminhoPdf) as pdf:
            numPaginas = len(pdf.pages)
            for pagina in pdf.pages:
                conteudo = pagina.extract_text() or ""
                textoExtraido += conteudo + "\n"
    except Exception as e:
        print("Erro ao abrir o PDF:", e)
        return {
            "texto": "",
            "numPaginas": 0
        }

    return{
        "texto": textoExtraido,
        "numPaginas": numPaginas,
    }