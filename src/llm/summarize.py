import os
from src.cli.arguments import get_arguments
from src.llm.model import carregarModelo, gerarResumo
from src.pdf.extractor import extrairTexto

# Salvando o resumo em um texto
def salvarResumo(caminhoSaida: str, resumo: str) -> None:
    try:
        with open(caminhoSaida, "w", encoding="utf-8") as arquivo:
            arquivo.write(resumo)
        print(f"Resumo salvo em: {caminhoSaida}")
    except Exception as e:
        print("Erro ao salvar o resumo:", e)

def rodarSummarize(args):

    print("Extraindo o texto do PDF")
    dados = extrairTexto(args.pdf)

    if not dados or not dados.get("texto"):
        print("Nenhum texto extraído do PDF")
        return
    
    texto = dados["texto"]

    # Carregando o modelo
    tokenizer, model = carregarModelo(args.modelo)

    # Gerando o resumo
    resumo = gerarResumo(tokenizer, model, texto)

    # Salvando o resumo
    salvarResumo(args.saida, resumo) 

if __name__ == "__main__":
    args = get_arguments()
    rodarSummarize(args)


