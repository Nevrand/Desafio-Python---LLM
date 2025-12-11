import os
import pdfplumber
from typing import List
from cli.arguments import get_arguments

def extrairImagem(caminhoPdf: str, pastaSaida: str) -> List[str]:
    # Verificando se o PDF existe
    if not os.path.isfile(caminhoPdf):
        print("PDF não encontrado", caminhoPdf)
        return []

    # Criando a pasta de saída se não existir
    os.makedirs(pastaSaida, exist_ok = True)

    caminhoImagem = []
    contador = 1

    # Abrindo o PDF
    try:
        with pdfplumber.open(caminhoPdf) as pdf:
            for numPagina, pagina in enumerate(pdf.pages):
                imagens = pagina.images or []
                if not imagens:
                    continue

                for img in imagens:
                    try:
                        recorte = pagina.crop((img["x0"], img["y0"], img["x1"], img["y1"]))
                        pil_imagem = recorte.to_image(resolution = 150)

                        caminhoImg = os.path.join(pastaSaida, f"pagina_{numPagina + 1}_imagem_{contador}.png")

                        pil_imagem.save(caminhoImg)
                        caminhoImagem.append(caminhoImg)
                        contador += 1

                    except Exception as e:
                        print(f"Erro ao extrair imagem:", e)
                        continue

    except Exception as e:
        print("Erro ao extrair imagens do PDF:", e)
        return []

    return caminhoImagem

def rodarExtrairImagens(args) -> None:
    pasta = os.path.join("imagens", os.path.splitext(os.path.basename(args.pdf))[0])
    print("Extraindo imagens do PDF para:", pasta)
    caminhoImagem = extrairImagem(args.pdf, pasta)

    if caminhoImagem:
        print("Imagens extraídas:")
        for c in caminhoImagem:
            print(" -", c)
    else:
        print("Nenhuma imagem encontrada no PDF.")

if __name__ == "__main__":
    args = get_arguments()
    rodarExtrairImagens(args)