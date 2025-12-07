
import argparse

def get_arguments():
    parser = argparse.ArgumentParser(
        prog="pdf_extração", 
        description="Extração de PDF para leitura" 
    )
    
    parser.add_argument(
    "--pdf",
    type = str,
    required = True,
    help = "Onde o PDF irá ser extraído"
    )

    parser.add_argument(
    "--saida",
    type = str,
    required = True,
    help = "Onde o texto extraído do PDF irá para ser salvo"
    )

    parser.add_argument(
    "--modelo",
    type = str,
    default = "microsoft/phi-3.5-mini-instruct",
    help = "Modelo que vai ser utilizado no projeto"
    )

    return parser.parse_args()