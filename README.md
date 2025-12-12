# Desafio Python - LLM
Desafio em Python para avaliação de capacidade de organizar um projeto em Python, manipular arquivos, extrair informações estruturais de um PDF e integrar uma LLM local usando Hugging Face. Este projeto foi desenvolvido para extrair texto e imagens de arquivo de um PDF e gerar um resumo usando uma LLM local.

A ideia seria testar comandos através do terminal para os objetivos propostos.

# Estrutura do projeto
Utilizei a mesma estrutura do projeto proposto, com algumas exceções de uma pasta com pdfs de exemplos para teste, um com texto (exemplo.pdf) e o outro com imagem (testarExtracao.pdf). 

Desafio-Python---LLM
    exemplos_pdf/
        exemplo.pdf
        testarExtracao.pdf
    imagens/
    src/
        pdf/
            extractor.py
            images.py
        llm/
            model.py
            summarize.py
        cli/
            arguments.py
        utils/
            text.py
            files.py
    main.py

# Dependências
Como alguns imports usados no projeto, aqui temos:
- PDFPlumber
- Torch
- Transformers

Podem ser instalados com os seguintes comandos respectivamente:
- pip install pdfplumber ou py -m pip install pdfplumber
- pip install torch ou py -m pip install torch
- pip install transformers ou py -m pip install transformers

# Modelo
Como o modelo poderia ser de escolha minha, fui com a recomendação do GPT de usar o microsoft/Phi-3-mini-4k-instruct no projeto.

# Executando
Como é necessário ter comando para se usar no terminal, aqui temos alguns para testes:
- Testar a extraçãp de textp: py -c "from src.pdf.extractor import extrairTexto; print(extrairTexto('exemplos_pdf/exemplo.pdf')['numPaginas'])"
- Resumir o pdf: py -m src.llm.summarize --pdf exemplos_pdf/exemplo.pdf --saida resumo.txt
- Extrair imagens do PDF: py -m src.pdf.images --pdf exemplos_pdf/testarExtracao.pdf (Isso irá salvar na pasta imagens)

# No geral ou Conclusão/Limitações
O projeto seria minha primeira vez mexendo em LLM e também aprendendo mais sobre quais comandos a usar para mexer com IA em Python. Então, pedi auxílio ao GPT para confirmar quais comandos usar, o que fazer em certas situações, checar erros e também qual modelo de LLM utilizar pois desconheço sobre modelos LLM. Serviu como forma de treinar no desenvolvimento de usar uma LLM local e também mexer mais em Python.


