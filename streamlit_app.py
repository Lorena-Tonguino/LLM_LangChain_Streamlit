import streamlit as st
from langchain_openai import ChatOpenAI
from datetime import datetime

# 1. Título de la aplicación
st.title('🦜🔗 Mi Primera App con LangChain')

# 2. Configuración de la API Key desde los secretos (Seguridad)
# Ya no necesitamos pedirla en la barra lateral porque se lee del archivo .toml
openai_api_key = st.secrets["OPENAI_API_KEY"]

# 3. Función para generar la respuesta con estampa de tiempo
def generate_response(input_text):
    # Usamos el modelo gpt-4o-mini
    llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=openai_api_key)
    
    # Generar la respuesta del modelo
    respuesta = llm.invoke(input_text).content
    
    # Obtener y formatear la hora: 2022-12-01 4:00:00 PM
    # %I es para formato 12h, %p para AM/PM
    ahora = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    
    # Mostrar la respuesta en el cuadro azul
    st.info(respuesta)
    
    # Mostrar la hora debajo de la respuesta
    st.caption(f"Consulta realizada el: {ahora}")

# 4. Formulario de entrada de usuario
with st.form('my_form'):
    text = st.text_area('Introduce tu pregunta:', '¿Cuáles son los 3 puntos clave del ciclo de vida de un LLM?')
    submitted = st.form_submit_button('Enviar')
    
    if submitted:
        # Verificamos que la llave se haya cargado correctamente desde secretos
        if openai_api_key:
            generate_response(text)
        else:
            st.error("Error: No se encontró la API Key en los secretos configurados.")