from cli.arguments import get_arguments
from llm.summarize import rodarSummarize

def main():
    args = get_arguments()

    print("PDF:", args.pdf)
    print("Saída:", args.saida)
    print("Modelo:", args.modelo)
    print("-" * 40)

    rodarSummarize(args)

if __name__ == "__main__":
    main()
