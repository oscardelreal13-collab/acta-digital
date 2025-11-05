import streamlit as st
import hashlib, time, json, os

# --- Función para generar hash SHA-256 ---
def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# --- Función para guardar el acta en un archivo JSON ---
def save_acta(texto, hash_result, timestamp):
    acta = {"texto": texto, "hash": hash_result, "fecha": timestamp}

    # Si el archivo no existe, crearlo
    if not os.path.exists("actas.json"):
        with open("actas.json", "w") as f:
            json.dump([], f)

    # Cargar las actas existentes
    with open("actas.json", "r") as f:
        data = json.load(f)

    # Añadir la nueva acta
    data.append(acta)

    # Guardar todo de nuevo
    with open("actas.json", "w") as f:
        json.dump(data, f, indent=4)

    return acta

# --- Interfaz principal ---
st.title("📜 Acta Digital con Hash SHA-256")
st.write("Genera una huella digital única para tu texto y guárdalo como registro verificable.")

# Campo de texto para el contenido del acta
texto = st.text_area("✍️ Escribe el contenido del acta:")

# Botón para generar el hash
if st.button("Generar Hash y Guardar Acta"):
    if texto.strip():
        hash_result = get_hash(texto)
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        acta_guardada = save_acta(texto, hash_result, timestamp)

        st.success("✅ Acta registrada correctamente.")
        st.subheader("🧾 Detalles del acta:")
        st.json(acta_guardada)
    else:
        st.warning("Por favor, escribe algún texto antes de generar el hash.")

# Botón para ver todas las actas guardadas
if st.button("📂 Ver todas las actas registradas"):
    if os.path.exists("actas.json"):
        with open("actas.json", "r") as f:
            data = json.load(f)
        st.write(f"Se han encontrado {len(data)} actas registradas:")
        st.json(data)
    else:
        st.info("Aún no hay actas guardadas.")




st.write("Timestamp:", time.time())
st.write("Ejemplo JSON:", json.dumps({"ok": True, "msg": "listo"}))
