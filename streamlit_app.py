import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

st.title('Mi Chat con Gemini 🚀')

# 1. Obtenemos la llave de los secrets
api_key = st.secrets["GOOGLE_API_KEY"]

def generate_response(input_text):
    # 2. Pasamos la llave directamente al inicializar el modelo
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
    try:
        respuesta = llm.invoke(input_text)
        st.info(respuesta.content)
    except Exception as e:
        st.error(f"Hubo un problema: {e}")

with st.form('my_form'):
    text = st.text_area('¿En qué puedo ayudarte?', '')
    submitted = st.form_submit_button('Enviar')
    if submitted:
        if text:
            generate_response(text)
        else:
            st.warning('Por favor, escribe algo antes de enviar.')
