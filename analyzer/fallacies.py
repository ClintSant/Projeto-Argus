import json
import re

def carregar_falacias():
    with open("data/fallacies.json", "r", encoding="utf-8") as f:
        return json.load(f)["falacias"]

def detectar_falacias(texto):
    falacias = carregar_falacias()
    resultado = []
    texto_lower = texto.lower()

    for falacia in falacias:
        for padrao in falacia["padroes"]:
            if re.search(padrao, texto_lower):
                resultado.append({
                    "falacia": falacia["nome"],
                    "descricao": falacia["descricao"],
                    "padrao_encontrado": padrao
                })
                break

    return resultado