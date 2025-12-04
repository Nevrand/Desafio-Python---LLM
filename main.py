
from cli.arguments import get_arguments

def main():
    # Pegar argumentos
    args = get_arguments()
    
    # Verificando se está funcionando
    print("PDF escolhido:", args.pdf_path)
    print("Saída:", args.out)

    if __name__ == "__main__":
        main()