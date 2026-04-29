import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

st.title('Mi Chat con Gemini 🚀')

# Configuración de la llave desde los Secrets de Streamlit
google_api_key = st.secrets["GOOGLE_API_KEY"]

def generate_response(input_text):
    # Usamos el modelo de Google en lugar de OpenAI
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=google_api_key)
    respuesta = llm.invoke(input_text).content
    st.info(respuesta)

with st.form('my_form'):
    text = st.text_area('¿En qué puedo ayudarte?', '')
    submitted = st.form_submit_button('Enviar')
    if submitted:
        if google_api_key:
            generate_response(text)
        else:
            st.warning('Por favor, configura la GOOGLE_API_KEY en los Secrets.')
