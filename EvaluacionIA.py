import os
import streamlit as st
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("Evaluador de Madurez en Ciberseguridad con IA")

st.write("Responde las siguientes preguntas para evaluar el nivel de madurez en ciberseguridad de tu organización:")

# Preguntas del formulario
pregunta1 = st.text_input("1. ¿Con qué frecuencia actualizan los sistemas y parches de seguridad?")
pregunta2 = st.text_input("2. ¿Existe un responsable designado para la gestión de ciberseguridad?")
pregunta3 = st.text_input("3. ¿Se capacita al personal en buenas prácticas de seguridad?")
pregunta4 = st.text_input("4. ¿Se miden los tiempos de respuesta ante incidentes?")
pregunta5 = st.text_input("5. ¿Se realizan auditorías o revisiones periódicas de seguridad?")

if st.button("Evaluar"):
    respuestas = {
        "actualizaciones": pregunta1,
        "responsable": pregunta2,
        "capacitacion": pregunta3,
        "medicion_incidentes": pregunta4,
        "auditorias": pregunta5
    }

    prompt = f"""
    Evalúa el nivel de madurez en ciberseguridad (bajo, medio o alto)
    con base en estas respuestas: {respuestas}.
    Da una breve justificación en lenguaje claro.
    """

    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        resultado = respuesta.choices[0].message.content
        st.subheader("Resultado del análisis:")
        st.write(resultado)
    except Exception as e:
        st.error(f"Ocurrió un error: {e}")
