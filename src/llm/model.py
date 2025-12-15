import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Modelo que irá ser utilizado para o projeto
modelo = "Qwen/Qwen2.5-0.5B-Instruct"

def carregarModelo(modelo: str = modelo):
    # Utilizar a CPU pois pode não haver GPU em alguns casos
    device = torch.device("cpu")
    
    # Carregando o modelo LLM utilizando transformers
    tokenizer = AutoTokenizer.from_pretrained(modelo)
    model = AutoModelForCausalLM.from_pretrained(modelo, torch_dtype = torch.float32)
    
    model.to(device)
    return tokenizer, model


def gerarResumo(tokenizer, model, texto: str):
    # Prompt para ser usado pelo modelo
    prompt = f"Faça um resumo claro e conciso do seguinte texto:\n\n{texto}\n\n"
    
    # Entrada do modelo
    entrada = tokenizer(prompt, return_tensors = "pt", truncation = True)
    entrada = {k: v.to(model.device) for k, v in entrada.items()}
    
    # Saída do modelo
    saida = model.generate(**entrada, max_new_tokens = 512, do_sample = False)
    
    # Decodificando a saída do modelo
    return tokenizer.decode(saida[0], skip_special_tokens = True)
    