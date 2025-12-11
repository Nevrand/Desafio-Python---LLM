# Desafio-Python - LLM
Desafio em Python para avaliação de capacidade de organizar um projeto em Python, manipular arquivos, extrair informações estruturais de um PDF e integrar uma LLM local usando Hugging Face.

Imports
Instalar pdfpulmber com py -m pip install pdfplumber ou pip install pdfplumber
Rodar com o py ./src/pdf/extractor.py
Instalar pip install torch ou py -m pip install torch
Instalar pip install transformers ou py -m pip install transformers

Modelo
Usar o microsoft/phi-3.5-mini-instruct

Testando extractor.py para ver se funciona
py -c "from src.pdf.extractor import extrairTexto; print(extrairTexto('exemplos_pdf/exemplo.pdf')['numPaginas'])"

Testando model.py para ver se funciona
py -c "from src.llm.model import carregarModelo, gerarResumo; tok, mod = carregarModelo('microsoft/phi-3.5-mini-instruct'); print(gerarResumo(tok, mod, 'O céu é azul porque...'))"

Testando o summarize.py para ver se funciona
py -m src.llm.summarize --pdf exemplos_pdf/exemplo.pdf --saida resumo.txt --modelo microsoft/phi-3.5-mini-instruct

Testando o images.py para ver se funciona
py -m src.pdf.images --pdf .\exemplos_pdf\testarExtracao.pdf --saida imagens   

