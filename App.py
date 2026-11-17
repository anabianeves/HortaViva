
import streamlit as st

st.set_page_config(
    page_title="HortaViva",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 HortaViva")
st.subheader("Cultive sua própria alimentação!")

st.write(
    "Descubra como criar e cuidar da sua horta "
    "com ajuda de um planejamento personalizado."
)

st.divider()

st.header("🌿 Monte sua horta")

espaco = st.selectbox(
    "Onde você pretende plantar?",
    ["Varanda", "Quintal", "Apartamento", "Jardim"]
)

luz = st.selectbox(
    "Quanto sol seu espaço recebe?",
    ["Pouco sol", "Sol parcial", "Sol direto"]
)

experiencia = st.selectbox(
    "Qual sua experiência com plantas?",
    ["Iniciante", "Intermediário", "Avançado"]
)

plantas = st.multiselect(
    "O que você gostaria de plantar?",
    ["Alface", "Tomate", "Cebolinha",
     "Coentro", "Manjericão", "Couve"]
)

if st.button("🌱 Criar minha horta"):
    st.success("Seu planejamento foi criado!")

    st.subheader("Seu perfil de cultivo")

    st.write("Espaço:", espaco)
    st.write("Iluminação:", luz)
    st.write("Experiência:", experiencia)
    st.write("Plantas escolhidas:", plantas)

    st.balloons()
