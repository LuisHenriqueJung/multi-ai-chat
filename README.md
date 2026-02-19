# HuggingFace Study Project

Este é um projeto de estudos sobre a API do HuggingFace, explorando diferentes tarefas de processamento de linguagem natural (NLP) usando o HuggingFace Inference API.

## Funcionalidades

O projeto inclui implementações para:

- **Geração de Texto**: Gera texto baseado em um prompt fornecido.
- **Resumo de Texto**: Resume textos longos usando modelos de sumarização.
- **Chat Completion**: Permite conversas interativas com um modelo de IA.
- **Interface Web**: Uma aplicação Streamlit para acessar todas as funcionalidades de forma fácil.

## Estrutura do Projeto

- `main.py`: Aplicação principal em Streamlit que integra todas as funcionalidades.
- `hfapi_textgeneration.py`: Script para geração de texto.
- `hfapi_summarization.py`: Script para sumarização de texto.
- `hfapi_chatcompletion.py`: Script para chat completion (sem streaming).
- `cha_complettion.py`: Script para chat completion com streaming via linha de comando.

## Requisitos

- Python 3.8 ou superior
- Conta no HuggingFace com token de API

## Instalação

1. Clone ou baixe o repositório.
2. Instale as dependências:

   ```bash
   pip install streamlit huggingface_hub python-dotenv
   ```

3. Crie um arquivo `.env` na raiz do projeto e adicione seu token do HuggingFace:

   ```
   HF_TOKEN=seu_token_aqui
   ```

## Como Usar

### Via Interface Web (Recomendado)

Execute a aplicação Streamlit:

```bash
streamlit run main.py
```

Acesse a interface no navegador e selecione a funcionalidade desejada.

### Via Scripts Individuais

Você pode executar os scripts diretamente no terminal:

- Para geração de texto: importe e use `gerar_texto(prompt)` de `hfapi_textgeneration.py`
- Para sumarização: importe e use `resumir(texto)` de `hfapi_summarization.py`
- Para chat: execute `python cha_complettion.py` para chat com streaming

## Modelos Utilizados

- **meta-llama/Llama-3.2-3B-Instruct**: Usado para geração de texto e chat completion.
- **facebook/bart-large-cnn**: Usado para sumarização.

## Contribuição

Este é um projeto de estudos. Sinta-se à vontade para modificar e experimentar com diferentes modelos e funcionalidades.

## Licença

Este projeto é para fins educacionais e não possui licença específica.