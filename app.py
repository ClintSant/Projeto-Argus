import streamlit as st
from analyzer.groq_analyzer import detectar_falacias_ia
from analyzer.contradictions import detectar_contradicoes

st.set_page_config(page_title="Argus", page_icon="👁️", layout="centered")

st.markdown("""
    <style>
        .titulo { font-size: 2.5rem; font-weight: 800; color: #7C3AED; }
        .subtitulo { font-size: 1.1rem; color: #9CA3AF; margin-bottom: 2rem; letter-spacing: 0.02em; }
        .card-falacia { background-color: #FEF2F2; border-left: 4px solid #EF4444; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; color: #111827; }
        .card-contradicao { background-color: #FFFBEB; border-left: 4px solid #F59E0B; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; color: #111827; }
        .card-ok { background-color: #F0FDF4; border-left: 4px solid #22C55E; padding: 1rem; border-radius: 8px; color: #111827; }
        .tag { display: inline-block; background: #EDE9FE; color: #7C3AED; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; }
        .trecho { background-color: #FEF2F2; border-left: 3px solid #EF4444; padding: 6px 10px; border-radius: 4px; font-style: italic; color: #374151; margin-top: 6px; font-size: 0.9rem; }
        .contador { font-size: 0.85rem; color: #9CA3AF; margin-bottom: 0.75rem; }
        .stButton > button {
            background-color: #7C3AED;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 0.6rem 1.5rem;
            font-size: 1rem;
            font-weight: 600;
            width: 100%;
            transition: background-color 0.2s;
        }
        .stButton > button:hover {
            background-color: #6D28D9;
            color: white;
        }
        .stTextArea label {
            font-size: 1rem;
            font-weight: 600;
            color: #E5E7EB;
        }
    </style>
""", unsafe_allow_html=True)

col_img, col_titulo = st.columns([1, 4])
with col_img:
    st.image("https://raw.githubusercontent.com/ClintSant/Projeto-Argus/main/assets/assests.argus.jpg", width=80)
with col_titulo:
    st.markdown('<div class="titulo">Argus</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitulo">Analisador de coerência argumentativa — detecta falácias e contradições em textos</div>', unsafe_allow_html=True)

texto = st.text_area("Cole o texto que deseja analisar:", height=200, placeholder="Ex: Todo mundo sabe que isso é verdade...")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    analisar = st.button("🔍 Analisar texto", use_container_width=True)

if analisar:
    if not texto.strip():
        st.warning("Digite ou cole um texto primeiro.")
    else:
        st.markdown("---")

        with st.spinner("🔍 Analisando com IA..."):
            falacias = detectar_falacias_ia(texto)
            contradicoes = detectar_contradicoes(texto)

        st.markdown("### Texto analisado")
        st.markdown(f'<div class="texto-analisado">{texto}</div>', unsafe_allow_html=True)

        st.markdown("---")

        col_a, col_b = st.columns(2)

        with col_a:
            st.markdown("### Falácias")
            if falacias:
                st.markdown(f'<div class="contador">{len(falacias)} falácia(s) encontrada(s)</div>', unsafe_allow_html=True)
                for f in falacias:
                    trecho = f.get("trecho", "")[:120]
                    st.markdown(f"""
                        <div class="card-falacia">
                            <strong>{f['falacia']}</strong><br>
                            <span style="color:#6B7280;font-size:0.9rem">{f['descricao']}</span>
                            <div class="trecho">❝ {trecho} ❞</div>
                        </div>
                    """, unsafe_allow_html=True)
                    with st.expander("Ver exemplo didático"):
                        st.markdown(f['exemplo_didatico'])
            else:
                st.markdown('<div class="card-ok">Nenhuma falácia detectada.</div>', unsafe_allow_html=True)

        with col_b:
            st.markdown("### Contradições")
            if contradicoes:
                st.markdown(f'<div class="contador">{len(contradicoes)} par(es) de contradição encontrado(s)</div>', unsafe_allow_html=True)
                for i, c in enumerate(contradicoes, start=1):
                    base = (i - 1) * 2
                    st.markdown(f"""
                        <div class="card-contradicao">
                            <strong>Frase {base + 1}:</strong> {c['frase_1']}<br><br>
                            <strong>Frase {base + 2}:</strong> {c['frase_2']}<br><br>
                            <strong>Por que se contradizem:</strong> {c.get('explicacao', '')}
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown('<div class="card-ok">Nenhuma contradição detectada.</div>', unsafe_allow_html=True)
