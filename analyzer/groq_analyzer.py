import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def detectar_falacias_ia(texto):
    prompt = f"""Você é um especialista em lógica e filosofia aristotélica. 
Analise o texto abaixo e identifique todas as falácias lógicas presentes.

Para cada falácia encontrada, responda EXATAMENTE neste formato JSON:
[
  {{
    "falacia": "nome da falácia",
    "descricao": "explicação breve do que é essa falácia",
    "trecho": "trecho exato do texto onde a falácia ocorre",
    "exemplo_didatico": "um exemplo simples e didático dessa falácia"
  }}
]

Se não houver falácias, retorne apenas: []

Texto para análise:
{texto}

Retorne APENAS o JSON, sem explicações adicionais."""

    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    conteudo = resposta.choices[0].message.content.strip()

    import json
    try:
        conteudo = conteudo.replace("```json", "").replace("```", "").strip()
        return json.loads(conteudo)
    except:
        return []