import streamlit as st
from google import genai

st.title('Mi Chat con Gemini 🚀')

# Configuración del cliente nuevo de Google
api_key = st.secrets["GOOGLE_API_KEY"]
client = genai.Client(api_key=api_key)

def generate_response(input_text):
    try:
        # Esta sintaxis es la oficial para 2026 y no falla con el 404
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=input_text
        )
        st.info(response.text)
    except Exception as e:
        st.error(f"Error técnico: {e}")

with st.form('my_form'):
    text = st.text_area('¿En qué puedo ayudarte?', '')
    submitted = st.form_submit_button('Enviar')
    if submitted:
        if text:
            generate_response(text)
        else:
            st.warning('Escribe una pregunta.')
