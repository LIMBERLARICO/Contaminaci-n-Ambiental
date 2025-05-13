import streamlit as st

contaminaciones = {
    "Contaminación del aire": {
        "Descripción": "Presencia de sustancias nocivas en la atmósfera.",
        "Causas": ["Emisiones de vehículos", "Industrias", "Quema de basura"],
        "Consecuencias": ["Problemas respiratorios", "Lluvia ácida", "Cambio climático"],
        "Soluciones": ["Transporte público", "Regulación de emisiones", "Energías limpias"],
        "Fórmulas químicas": ["CO₂", "SO₂", "NO₂", "PM₂.₅"],
        "Ejemplo histórico": {
            "Nombre": "Gran Smog de Londres",
            "Año": 1952,
            "Lugar": "Reino Unido",
            "Descripción": "Miles de muertes por una nube tóxica de carbón."
        },
        "Impacto militar": [
            "Las emisiones de guerra aumentan la polución.",
            "Guerra del Golfo: quema de pozos petroleros.",
            "Ejercicios militares generan gases contaminantes."
        ],
        "Imagen": "https://upload.wikimedia.org/wikipedia/commons/3/33/Air_pollution_by_industry.jpg"
    },
    "Contaminación del agua": {
        "Descripción": "Contaminación química o biológica de cuerpos de agua.",
        "Causas": ["Vertidos industriales", "Aguas residuales", "Agricultura intensiva"],
        "Consecuencias": ["Enfermedades", "Muerte acuática", "Falta de agua potable"],
        "Soluciones": ["Tratamiento de aguas", "Leyes ambientales", "Educación"],
        "Fórmulas químicas": ["Hg", "Pb", "NO₃⁻", "PO₄³⁻"],
        "Ejemplo histórico": {
            "Nombre": "Desastre de Minamata",
            "Año": 1956,
            "Lugar": "Japón",
            "Descripción": "Contaminación por mercurio devastó la bahía de Minamata."
        },
        "Impacto militar": [
            "Guerras destruyen infraestructuras de agua.",
            "Fuentes de agua como armas (envenenamiento).",
            "Bases militares contaminan ríos cercanos."
        ],
        "Imagen": "https://upload.wikimedia.org/wikipedia/commons/f/f2/Water_pollution_in_Rio_de_Janeiro_2014.jpg"
    },
    # Agrega los demás tipos igual...
}

# Interfaz Streamlit
st.set_page_config(page_title="Contaminación y Conflictos", layout="centered")
st.title("🌍 Contaminación Ambiental y su Impacto Militar")

tipo = st.selectbox("🔍 Buscar o seleccionar tipo de contaminación:", list(contaminaciones.keys()))

if tipo:
    data = contaminaciones[tipo]

    st.subheader(f"📘 {tipo}")
    
    # Mostrar imagen si existe
    if "Imagen" in data:
        st.image(data["Imagen"], use_column_width=True, caption=f"Ejemplo visual de {tipo.lower()}")

    st.markdown(f"**🧾 Descripción:** {data['Descripción']}")

    st.markdown("**🔥 Causas:**")
    for causa in data["Causas"]:
        st.write(f"- {causa}")

    st.markdown("**⚠️ Consecuencias ambientales:**")
    for efecto in data["Consecuencias"]:
        st.write(f"- {efecto}")

    st.markdown("**✅ Soluciones propuestas:**")
    for solucion in data["Soluciones"]:
        st.write(f"- {solucion}")

    st.markdown("**🧪 Fórmulas químicas asociadas:**")
    for formula in data["Fórmulas químicas"]:
        st.write(f"- {formula}")

    st.markdown("**📚 Ejemplo histórico relevante:**")
    ejemplo = data["Ejemplo histórico"]
    st.write(f"📌 **{ejemplo['Nombre']}** ({ejemplo['Año']}, {ejemplo['Lugar']})")
    st.info(ejemplo["Descripción"])

    st.markdown("**🔰 Impacto militar asociado:**")
    for impacto in data["Impacto militar"]:
        st.write(f"- {impacto}")
