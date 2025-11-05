import streamlit as st
st.title("Acta Digital 🧾")
st.write("Bienvenido a tu primera app con Streamlit.")
import hashlib, time, json


st.title("Acta Digital — Import Test")

st.write("✅ Librerías importadas:")
st.code("streamlit, hashlib, time, json")

import streamlit as st
import hashlib, time, json, os

# --- Función para generar hash único ---
def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# --- Función para guardar el acta en un archivo JSON ---
def save_acta(texto, hash_result, timestamp):
    acta = {"texto": texto, "hash": hash_result, "fecha": timestamp}

    # Si el archivo no existe, crear uno nuevo
    if not os.path.exists("actas.json"):
        with open("actas.json", "w") as f:
            json.dump([], f)

    # Cargar las actas existentes
    with open("actas.json", "r") as f:
        data = json.load(f)

    # Añadir la nueva acta
    data.append(acta)

    # Guardar de nuevo
    with open("actas.json", "w") as f:
        json.dump(data, f, indent=4)

    return acta

# --- Interfaz de la aplicación ---
st.title("📜 Acta Digital con Hash SHA-256")
st.write("Registra actas de forma segura generando una huella digital única.")

# Entrada de texto del usuario
input_text = st.text_area("✍️ Escribe el contenido del acta:")

# Botón principal
if st.button("Generar y guardar acta"):
    if input_text.strip():
        hash_result = get_hash(input_text)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        acta_guardada = save_acta(input_text, hash_result, timestamp)

        st.success("✅ Acta registrada correctamente.")
        st.subheader("🧾 Detalles del registro:")
        st.json(acta_guardada)
    else:
        st.warning("Por favor, escribe algo antes de generar el hash.")

# --- Visualizar actas guardadas ---
if st.button("📂 Ver todas las actas guardadas"):
    if os.path.exists("actas.json"):
        with open("actas.json", "r") as f:
            data = json.load(f)
        st.write(f"Se han encontrado {len(data)} actas registradas:")
        st.json(data)
    else:
        st.info("Aún no hay actas registradas.")

st.write("Timestamp:", time.time())
st.write("Ejemplo JSON:", json.dumps({"ok": True, "msg": "listo"}))
