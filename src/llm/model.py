import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Modelo que irá ser utilizado para o projeto
modelo = "microsoft/phi-3.5-mini-instruct"

def carregarModelo(modelo: str):
    # Cuda só funciona com GPU da NVIDIA, então caso não houver o GPU, utilizar a CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # Carregando o modelo phi-mini-instruct utilizando transformers
    tokenizer = AutoTokenizer.from_pretrained(modelo)
    model = AutoModelForCausalLM.from_pretrained(modelo, torch_dtype=torch.float16 if device == "cuda" else torch.float32)
    
    return tokenizer, model


def gerarResumo(tokenizer, model, texto: str):
    # Prompt para ser usado no phi-mini-instruct
    prompt = f"Extraia as informações do seguinte texto:\n\n{texto}\n\n"
    
    # Entrada do modelo
    entrada = tokenizer(prompt, return_tensors= "pt", truncation = True)
    entrada = {k: v.to(model.device) for k, v in entrada.items()}
    
    # Saída do modelo
    saida = model.generate(**entrada, max_new_tokens=512, temperature=0)
    
    # Decodificando a saída do modelo
    resultado = tokenizer.decode(saida[0], skip_special_tokens=True)
    
    return resultado