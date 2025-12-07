
from cli.arguments import get_arguments
from llm.summarize import rodarSummarize

def main():
    # Pegar argumentos
    args = get_arguments()
    
    # Verificando se está funcionando
    rodarSummarize(args)

    if __name__ == "__main__":
        main()