import os
import json
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).parent.parent / ".env")

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def detectar_contradicoes(texto):
    prompt = f"""Você é um especialista em lógica e análise de textos.
Analise o texto abaixo e identifique pares de frases que se contradizem diretamente.

Para cada contradição encontrada, responda EXATAMENTE neste formato JSON:
[
  {{
    "frase_1": "primeira frase",
    "frase_2": "segunda frase que contradiz a primeira",
    "explicacao": "breve explicação de por que se contradizem"
  }}
]

Se não houver contradições, retorne apenas: []

Texto para análise:
{texto}

Retorne APENAS o JSON, sem explicações adicionais."""

    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    conteudo = resposta.choices[0].message.content.strip()

    try:
        conteudo = conteudo.replace("```json", "").replace("```", "").strip()
        return json.loads(conteudo)
    except:
        return []
