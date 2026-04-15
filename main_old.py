import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

numero_de_dias = 7
numero_criancas = 2
atividade = 'música'

prompt = f"Crie um roteiro de viagem de {numero_de_dias} dias, para uma família com {numero_criancas} crianças, que gosta de {atividade}"

cliente = OpenAI()

resposta = cliente.chat.completions.create(
    model="gpt-3.5-turbo",
    messages = [
        {
            "role": "system",
            "content": "Você é um assistente de roteiro de viagens."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(resposta.choices[0].message.content)