👁️ Argus — Analisador de Coerência Argumentativa

Argus é uma aplicação web que utiliza Inteligência Artificial para detectar **falácias lógicas** e **contradições** em textos, com base na tradição filosófica aristotélica e na lógica informal de Irving Copi.

 Como funciona

O usuário cola qualquer texto na interface e o Argus:
1. Envia o texto para um LLM via **Groq API** (LLaMA 3.3 70B)
2. A IA identifica falácias com compreensão semântica real — sem depender de palavras-chave fixas
3. Detecta contradições entre frases usando **Sentence Transformers**
4. Explica cada falácia com descrição e exemplo didático

 Falácias detectadas

O Argus detecta falácias da tradição filosófica clássica, incluindo:
- Ad Hominem, Apelo à Autoridade, Falsa Dicotomia
- Post Hoc Ergo Propter Hoc, Ladeira Escorregadia
- Tu Quoque, Homem de Palha, Apelo à Ignorância
- E muitas outras catalogadas por Aristóteles e Copi

 Tecnologias

- **Python** — linguagem principal
- **Streamlit** — interface web
- **Groq API + LLaMA 3.3 70B** — detecção de falácias por IA
- **Sentence Transformers** — detecção de contradições
- **python-dotenv** — gerenciamento de variáveis de ambiente

 Como rodar localmente

1. Clone o repositório:
```bash
git clone https://github.com/ClintSant/Projeto-Argus.git
cd Projeto-Argus
```

2. Crie e ative o ambiente virtual:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Instale as dependências:
```bash
pip install -r requisitos.txt
```

4. Crie um arquivo `.env` com sua chave da Groq:


5. Rode a aplicação:
```bash
streamlit run app.py
```

## 📁 Estrutura do projeto
argus/
├── app.py                  # Interface Streamlit
├── analisador/
│   ├── groq_analyzer.py    # Detecção de falácias via IA
│   ├── contradictions.py   # Detecção de contradições
│   └── fallacies.py        # Versão anterior com dicionário
├── dados/
│   └── fallacies.json      # Dicionário filosófico de falácias
├── .env                    # Chave de API (não versionado)
└── requisitos.txt          # Dependências do projeto

## 👤 Autor

**Clinton Santos**  
Analista de Dados | Cientista de Dados em formação  
[LinkedIn](www.linkedin.com/in/clinton-santos-094b1b214) • [GitHub](https://github.com/ClintSant)
