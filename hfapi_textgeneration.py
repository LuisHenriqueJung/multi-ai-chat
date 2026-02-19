from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

def gerar_texto(prompt):
    cliente = InferenceClient(model="meta-llama/Llama-3.2-3B-Instruct")
    resposta = cliente.text_generation([{"role": "user", "content": prompt}],model="meta-llama/Llama-3.2-3B-Instruct")
    return resposta["generated_text"]
    