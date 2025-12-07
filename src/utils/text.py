import re
from typing import List

Stopwords = ["a", "o", "as", "os", "de", "da", "do", "das", "dos", "um", "uma", "uns", "umas", "e", "que", "com", "para"]

def limparTexto(texto: str) -> str:
    # Removendo espaços extras e quebras de linha
    if not texto:
        return ""
    
    # Removendo espaços extras
    texto = re.sub(r'\s+', ' ', texto)
    # Removendo espaços no início e fim
    texto = texto.strip()
    return texto


def textoMinusculo(texto: str) -> str:
    # Converte o texto para minúsculo
    if not texto:
        return ""
    return texto.lower()


def separarPalavras(texto: str) -> List[str]:
    # Separa o texto em uma lista de palavras, removendo pontuações
    if not texto:
        return []
    
    palavras = re.findall(r'\b\w+\b', texto)
    return palavras


def removerStopwords(palavras: List[str]) -> List[str]:
    # Remove as stopwords da lista de palavras
    if not palavras:
        return []
    
    palavrasFiltradas = [palavra for palavra in palavras if palavra.lower() not in Stopwords]
    return palavrasFiltradas

def vocabularioUnico(palavras: List[str]) -> set:
    # Retorna um conjunto de palavras únicas
    if not palavras:
        return set()
    
    return set(palavras)

def contarPalavras(palavras: List[str]) -> int:
    # Conta o número de palavras na lista
    if not palavras:
        return 0
    return len(palavras)

def contarPalavrasComuns(palavras: List[str], n: int = 10) -> List[tuple]:
    # Conta as palavras mais comuns na lista
    if not palavras:
        return []
    
    from collections import Counter
    contandoPalavra = Counter(palavras)
    return contandoPalavra.most_common(n)