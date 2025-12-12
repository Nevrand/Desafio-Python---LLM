
import argparse

# Configuração dos argumentos da linha de comando
def get_arguments():
    parser = argparse.ArgumentParser(
        prog="pdf_extração", 
        description="Extração de PDF para leitura" 
    )
    
    # Comandos que podem ser usados no terminal

    parser.add_argument(
    "--pdf",
    type = str,
    required = True,
    help = "Onde o PDF irá ser extraído"
    )

    parser.add_argument(
    "--detalhes",
    action = "store_true",
    help = "Exibir detalhes sobre o texto extraído do PDF"
    )

    parser.add_argument(
    "--texto",
    action = "store_true",
    help = "Exibir o texto extraído do PDF"
    )

    parser.add_argument(
    "--saida",
    type = str,
    help = "Caminho para salvar o resumo do PDF"
    )

    parser.add_argument(
    "--modelo",
    type = str,
    default = "microsoft/Phi-3-mini-4k-instruct",
    help = "Modelo LLM que foi usado"
    )
    
    return parser