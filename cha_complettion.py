from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

cliente = InferenceClient(model="meta-llama/Llama-3.2-3B-Instruct")

mensagens = [
    {"role": "system", "content": "Responda as perguntas de forma correta e precisa"},
]

while True:
    prompt = input("Digite a sua mensagem: ")
    mensagem_usuario = {"role": "user", "content": prompt}
    mensagens.append(mensagem_usuario)

    resposta = cliente.chat_completion(mensagens, stream=True)
    
    content_resposta = ""
    for chunk in resposta:
        print(chunk.choices[0].delta.content, end="")
        content_resposta += chunk.choices[0].delta.content

    dicionario_resposta_ia = {"role": "assistant", "content": content_resposta}
    mensagens.append(dicionario_resposta_ia)

    