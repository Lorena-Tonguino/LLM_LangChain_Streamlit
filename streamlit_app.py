import streamlit as st
import google.generativeai as genai

st.title('Mi Chat con Gemini 🚀')

# 1. Configuración directa con la librería de Google
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

def generate_response(input_text):
    try:
        # Usamos la configuración más estándar posible
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(input_text)
        st.info(response.text)
    except Exception as e:
        st.error(f"Hubo un problema: {e}")

with st.form('my_form'):
    text = st.text_area('¿En qué puedo ayudarte?', '')
    submitted = st.form_submit_button('Enviar')
    if submitted:
        if text:
            generate_response(text)
        else:
            st.warning('Por favor, escribe algo.')
