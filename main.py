from src.cli.arguments import get_arguments
from src.llm.summarize import rodarSummarize
from src.pdf.extractor import analisarPdf
from src.pdf.images import rodarExtrairImagens

def main():
    args = get_arguments()
    # Rodando a análise do PDF
    analisarPdf(args.pdf)
    # Rodando a extração de imagens
    rodarExtrairImagens(args)
    # Rodando o resumo
    rodarSummarize(args)

if __name__ == "__main__":
    main()
