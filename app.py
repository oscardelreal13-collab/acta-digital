import streamlit as st
import hashlib, time, json, os

# --- Función para generar hash SHA-256 ---
def get_hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# --- Interfaz principal ---
st.title("📜 Registro de Documentos Digitales")
st.write("Simulación de un registro tipo *blockchain* para documentos o actas digitales.")

# --- Campos de entrada ---
owner = st.text_input("👤 Propietario del documento:")
content = st.text_area("📝 Contenido del documento:")

# --- Botón para registrar el documento ---
if st.button("Registrar Documento"):
    if owner.strip() and content.strip():
        # Crear el registro
        record = {
            "owner": owner,
            "hash": get_hash(content),
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        # Guardar cada registro en una línea independiente (simulando blockchain)
        with open("blockchain.json", "a") as f:
            f.write(json.dumps(record) + "\n")

        st.success("✅ Documento registrado con éxito.")
        st.subheader("🔒 Detalles del registro:")
        st.json(record)
    else:
        st.warning("Por favor, completa todos los campos antes de registrar.")

# --- Mostrar todos los documentos registrados ---
if st.button("📂 Ver documentos registrados"):
    if os.path.exists("blockchain.json") and os.path.getsize("blockchain.json") > 0:
        with open("blockchain.json", "r") as f:
            lines = f.readlines()
            data = [json.loads(line) for line in lines]
        st.write(f"Se han encontrado {len(data)} documentos registrados:")
        st.json(data)
    else:
        st.info("Aún no hay documentos registrados en la blockchain.")




st.write("Timestamp:", time.time())
st.write("Ejemplo JSON:", json.dumps({"ok": True, "msg": "listo"}))
