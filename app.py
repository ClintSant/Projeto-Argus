import streamlit as st
import re
from analyzer.groq_analyzer import detectar_falacias_ia
from analyzer.contradictions import detectar_contradicoes

st.set_page_config(page_title="Argus", page_icon="👁️", layout="centered")

st.markdown("""
    <style>
        .titulo { font-size: 2.5rem; font-weight: 800; color: #7C3AED; }
        .subtitulo { font-size: 1rem; color: #6B7280; margin-bottom: 2rem; }
        .card-falacia { background-color: #FEF2F2; border-left: 4px solid #EF4444; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; color: #111827; }
        .card-contradicao { background-color: #FFFBEB; border-left: 4px solid #F59E0B; padding: 1rem; border-radius: 8px; margin-bottom: 1rem; color: #111827; }
        .card-ok { background-color: #F0FDF4; border-left: 4px solid #22C55E; padding: 1rem; border-radius: 8px; color: #111827; }
        .tag { display: inline-block; background: #EDE9FE; color: #7C3AED; padding: 2px 8px; border-radius: 4px; font-size: 0.8rem; }
        .destaque { background-color: #FCA5A5; padding: 2px 4px; border-radius: 4px; font-weight: bold; color: #111827; }
        .texto-analisado { font-size: 1rem; line-height: 1.8; background: #F9FAFB; padding: 1rem; border-radius: 8px; border: 1px solid #E5E7EB; color: #111827; }
        .contador { font-size: 0.85rem; color: #6B7280; margin-bottom: 0.5rem; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="titulo">👁️ Argus</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitulo">Analisador de coerência argumentativa — detecta falácias e contradições em textos</div>', unsafe_allow_html=True)

texto = st.text_area("Cole o texto que deseja analisar:", height=200, placeholder="Ex: Todo mundo sabe que isso é verdade...")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    analisar = st.button("🔍 Analisar texto", use_container_width=True)

def destacar_trechos(texto, falacias):
    texto_destacado = texto
    for f in falacias:
        trecho = f.get("trecho", "")
        if trecho:
            texto_destacado = re.sub(
                f"({re.escape(trecho)})",
                r'<span class="destaque" title="' + f["falacia"] + r'">\1</span>',
                texto_destacado,
                flags=re.IGNORECASE
            )
    return texto_destacado

if analisar:
    if not texto.strip():
        st.warning("Digite ou cole um texto primeiro.")
    else:
        st.markdown("---")

        with st.spinner("🔍 Analisando com IA..."):
            falacias = detectar_falacias_ia(texto)

        st.markdown("### 📝 Texto analisado")
        if falacias:
            texto_destacado = destacar_trechos(texto, falacias)
            st.markdown(f'<div class="texto-analisado">{texto_destacado}</div>', unsafe_allow_html=True)
            st.caption("🔴 Trechos em vermelho indicam falácias detectadas pela IA")
        else:
            st.markdown(f'<div class="texto-analisado">{texto}</div>', unsafe_allow_html=True)

        st.markdown("---")

        col_a, col_b = st.columns(2)

        with col_a:
            st.markdown("### 🚨 Falácias")
            if falacias:
                st.markdown(f'<div class="contador">🔢 {len(falacias)} falácia(s) encontrada(s)</div>', unsafe_allow_html=True)
                for f in falacias:
                    st.markdown(f"""
                        <div class="card-falacia">
                            <strong>{f['falacia']}</strong><br>
                            <span style="color:#6B7280;font-size:0.9rem">{f['descricao']}</span><br><br>
                            <span class="tag">"{f.get('trecho', '')[:60]}..."</span>
                        </div>
                    """, unsafe_allow_html=True)
                    with st.expander("💡 Ver exemplo didático"):
                        st.markdown(f['exemplo_didatico'])
            else:
                st.markdown('<div class="card-ok">✅ Nenhuma falácia detectada.</div>', unsafe_allow_html=True)

        with col_b:
            st.markdown("### ⚡ Contradições")
            contradicoes = detectar_contradicoes(texto)
            if contradicoes:
                st.markdown(f'<div class="contador">🔢 {len(contradicoes)} contradição(ões) encontrada(s)</div>', unsafe_allow_html=True)
                for c in contradicoes:
                    st.markdown(f"""
                        <div class="card-contradicao">
                            <strong>Frase 1:</strong> {c['frase_1']}<br><br>
                            <strong>Frase 2:</strong> {c['frase_2']}<br><br>
                            <span class="tag">similaridade: {c['similaridade']}</span>
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.markdown('<div class="card-ok">✅ Nenhuma contradição detectada.</div>', unsafe_allow_html=True)