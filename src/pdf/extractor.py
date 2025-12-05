# Importando o pdfplumber como ferramenta principal para extração de texto como torch e transformers
import pdfplumber
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Caminho do arquivo PDF a ser extraído de exemplo para testes
pdf_path = 'exemplos_pdf/exemplo.pdf'

# Extração de texto do PDF
texto = ''
with pdfplumber.open(pdf_path) as pdf:
    # Percorre todas as páginas do PDF
    for page in pdf.pages:
        texto += page.extract_text()

# Modelo que irá ser utilizado para o projeto
modelo = "microsoft/phi-3.5-mini-instruct"

# Carregando o modelo phi-mini-instruct
tokenizer = AutoTokenizer.from_pretrained(modelo)
model = AutoModelForCausalLM.from_pretrained(modelo, torch_dtype=torch.float16, device_map="auto")

# Prompt para ser usado no phi-mini-instruct
prompt = f"Extraia as informações do seguinte texto:\n\n{texto}\n\n"

# Entrada do modelo
entrada = tokenizer(prompt, return_tensors= "pt", truncation = True)

# Saída do modelo
saida = model.generate(**entrada, max_new_tokens=512, temperature=0)

# Decodificando a saída do modelo
resultado = tokenizer.decode(saida[0], skip_special_tokens=True)

print(texto)
print("Número total de páginas extraídas:", len(pdf.pages))
print("Número total de palavras extraídas:", len(texto.split()))
print("Tamanho em bytes do texto extraído:", len(texto.encode('utf-8')))
print("Resultado do modelo phi-mini-instruct:", resultado)