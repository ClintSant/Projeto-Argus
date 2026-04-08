from sentence_transformers import SentenceTransformer, util

modelo = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

def detectar_contradicoes(texto):
    frases = [f.strip() for f in texto.split(".") if len(f.strip()) > 10]
    resultado = []

    for i in range(len(frases)):
        for j in range(i + 1, len(frases)):
            emb1 = modelo.encode(frases[i], convert_to_tensor=True)
            emb2 = modelo.encode(frases[j], convert_to_tensor=True)
            similaridade = util.cos_sim(emb1, emb2).item()

            if similaridade < -0.1:
                resultado.append({
                    "frase_1": frases[i],
                    "frase_2": frases[j],
                    "similaridade": round(similaridade, 2)
                })

    return resultado