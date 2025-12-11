import pdfplumber
import os
import argparse

from src.utils.files import tamanhoArquivo
from src.utils.text import (limparTexto, textoMinusculo, separarPalavras, removerStopwords, vocabularioUnico, contarPalavras, contarPalavrasComuns)

def extrairTexto(caminhoPdf: str):
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

def analisarPdf(caminhoPdf: str):
    dados = extrairTexto(caminhoPdf)

    if not dados:
        print("Nenhum dado extraído do PDF.")
        return
    
    texto = dados["texto"]
    numPaginas = dados["numPaginas"]

    textoLimpo = limparTexto(texto)
    textoMinusculo = textoMinusculo(textoLimpo)
    palavras = separarPalavras(textoMinusculo)
    palavrasSemStopwords = removerStopwords(palavras)

    totalPalavras = contarPalavras(palavrasSemStopwords)
    vocabulario = vocabularioUnico(palavrasSemStopwords)
    palavrasComuns = contarPalavrasComuns(palavrasSemStopwords, n = 10)
    tamanhoBytes = tamanhoArquivo(caminhoPdf)

    print(f"Número de páginas: {numPaginas}")
    print(f"Tamanho do arquivo: {tamanhoBytes} bytes")
    print(f"Número total de palavras (sem stopwords): {totalPalavras}")
    print(f"Número de palavras únicas: {len(vocabulario)}")
    print(f"Palavras mais comuns: {palavrasComuns}")

def rodarExtrairTexto():
    parser = argparse.ArgumentParser(prog = "extractor", description = "Extrair texto de um arquivo PDF")
    
    parser.add_argument("--pdf", type = str, help = "Caminho do arquivo PDF")

    args = parser.parse_args()
    analisarPdf(args.pdf)

if __name__ == "__main__":
    rodarExtrairTexto()