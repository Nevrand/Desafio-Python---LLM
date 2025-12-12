import pdfplumber
import os

from src.utils.files import tamanhoArquivo
from src.utils.text import (limparTexto, textoMinusculo, separarPalavras, removerStopwords, vocabularioUnico, contarPalavras, contarPalavrasComuns)
from src.cli.arguments import get_arguments

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

# Função para analisar o PDF e também chamar as funções de text.py para usar no processo de extração
def analisarPdf(caminhoPdf: str):
    dados = extrairTexto(caminhoPdf)

    if not dados:
        print("Nenhum dado extraído do PDF.")
        return
    
    texto = dados["texto"]
    numPaginas = dados["numPaginas"]

    # Chamando as funções de text.py para utilizar no texto extraído
    textoLimpo = limparTexto(texto)
    textoMin = textoMinusculo(textoLimpo)
    palavras = separarPalavras(textoMin)
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

# Se utilizar o comando de arguments.py como detalhes ou texto ou nenhum dos dois e aí irá rodar um dos ifs para fazer certos papéis
def main():
    parser = get_arguments()
    args = parser.parse_args()
    info = extrairTexto(args.pdf)
    
    # Se for detalhes, vai imprirr o número de páginas e tamanho do texto
    if args.detalhes:
        print(f"Número de páginas: {info['numPaginas']}")
        print(f"Tamanho do texto: {len(info['texto'])} caracteres")

    # Se for texto, vai imprimir o texto extraído do PDF
    if args.texto:
        print(f"Texto extraído do PDF: {info['texto']}")
    
    # Se não for nenhum dos dois, vai analisar o PDF
    if not args.detalhes and not args.texto:
        analisarPdf(args.pdf)

if __name__ == "__main__":
    main()