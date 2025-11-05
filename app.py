st.title("Acta Digital 🧾")
st.write("Bienvenido a tu primera app con Streamlit.")

import streamlit as st
import hashlib, time, json

st.title("Acta Digital — Import Test")

st.write("✅ Librerías importadas:")
st.code("streamlit, hashlib, time, json")

text = st.text_input("Texto a hashear (SHA-256):", "hola mundo")
if text:
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
    st.write("Hash:", sha)

st.write("Timestamp:", time.time())
st.write("Ejemplo JSON:", json.dumps({"ok": True, "msg": "listo"}))
