import os 
from typing import List, Optional

def verificarArquivo(arquivo: str) -> bool:
    # Verifica se o arquivo existe no caminho fornecido
    if not os.path.isfile(arquivo):
        print("Arquivo não encontrado:", arquivo)
        return False
    return True

def criarPasta(pasta: str) -> None:
    # Cria a pasta se não existir
    os.makedirs(pasta, exist_ok = True)


def salvarArquivo(caminhoSaida: str, conteudo: str) -> bool:
    # Salva o conteúdo em um arquivo no caminhoSaida
    try:
        with open(caminhoSaida, "w", encoding = "utf-8") as arquivo:
            arquivo.write(conteudo)
        return True
    except Exception as e:
        print("Erro ao salvar o arquivo:", e)
        return False
    
    
def lerArquivo(caminhoArquivo: str) -> Optional[str]:
    # Lê o conteúdo de um arquivo e retorna como string
    try:
        with open(caminhoArquivo, "r", encoding = "utf-8") as arquivo:
            return arquivo.read()
    except Exception as e:
        print("Erro ao ler o arquivo:", e)
        return None
    
    
def listarArquivos(pasta: str) -> List[str]:
    # Lista todos os pdfs em uma pasta
    pdfs = []

    if not os.path.isdir(pasta):
        print("Pasta não encontrada:", pasta)
        return pdfs
    
    # Listando os arquivos na pasta
    try:
        for arquivo in os.listdir(pasta):
            if arquivo.endswith(".pdf"):
                pdfs.append(os.path.join(pasta, arquivo))
    except Exception as e:
        print("Erro ao listar arquivos na pasta:", e)
    return pdfs


def tamanhoArquivo(arquivo: str) -> int:
    # Retorna o tamanho do arquivo em bytes
    try:
        return os.path.getsize(arquivo)
    except Exception:
        return 0
    
    
def nomeArquivo(arquivo: str) -> str:
    # Retorna o nome do arquivo sem o caminho
    nome = os.path.basename(arquivo)
    return os.path.splitext(nome)[0]
