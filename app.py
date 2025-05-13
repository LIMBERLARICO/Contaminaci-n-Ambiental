import streamlit as st

# Conceptos de cada tipo de contaminación
conceptos = {
    "Contaminación del suelo": "La contaminación del suelo ocurre cuando productos químicos, desechos peligrosos o basura alteran la calidad natural de la tierra, afectando la agricultura, el agua subterránea y la salud humana.",
    "Contaminación del agua": "La contaminación del agua es la introducción de sustancias nocivas en ríos, lagos y océanos, que afectan la vida acuática, la potabilidad del agua y el equilibrio ecológico.",
    "Contaminación por plásticos": "Los plásticos no biodegradables se acumulan en ambientes naturales, especialmente en océanos, causando daños irreparables a la fauna marina y entrando en la cadena alimenticia.",
    "Contaminación por ruido": "El exceso de ruido proveniente del tráfico, industrias o actividades humanas afecta la salud auditiva, mental y la calidad de vida, especialmente en zonas urbanas.",
    "Contaminación por petróleo": "Se refiere a los derrames de crudo o sus derivados en cuerpos de agua o suelo, causando desastres ecológicos, muerte de especies y graves impactos económicos y sociales."
}

# Ejemplos históricos relacionados
ejemplos = {
    "Contaminación del suelo": {
        "ejemplo": "Love Canal (EE.UU., 1978)",
        "Lugar": "Nueva York, EE.UU.",
        "Descripción": "Una empresa enterró más de 20,000 toneladas de residuos químicos, lo que provocó problemas de salud graves en la población.",
        "Consecuencias": [
            "Evacuación masiva",
            "Enfermedades como cáncer y mutaciones",
            "Creación del programa Superfondo"
        ],
        "Impacto militar": [
            "Sirvió como ejemplo para limpiar residuos tóxicos en bases militares.",
            "Aumentó la vigilancia sobre armas químicas almacenadas."
        ],
        "Imagen": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Love_Canal_Contamination.jpg"
    },
    "Contaminación del agua": {
        "ejemplo": "Río Ganges (India)",
        "Lugar": "India",
        "Descripción": "El Ganges, un río sagrado, sufre de alta contaminación debido a residuos industriales y aguas negras.",
        "Consecuencias": [
            "Enfermedades transmisibles",
            "Muerte de especies acuáticas",
            "Riesgo a la salud de millones"
        ],
        "Impacto militar": [
            "Contaminación estratégica de fuentes de agua puede agravar tensiones sociales.",
            "Impacto en logística de tropas que dependen del río."
        ],
        "Imagen": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Pollution_in_the_Ganges_river.jpg"
    },
    "Contaminación por plásticos": {
        "ejemplo": "Gran Mancha del Pacífico",
        "Lugar": "Océano Pacífico",
        "Descripción": "Millones de toneladas de plástico flotan en esta zona, afectando la biodiversidad marina y los ecosistemas.",
        "Consecuencias": [
            "Animales enredados o asfixiados",
            "Microplásticos en alimentos",
            "Alteración de cadenas tróficas"
        ],
        "Impacto militar": [
            "Contaminación de rutas marítimas estratégicas.",
            "Desechos plásticos de operaciones militares no tratadas."
        ],
        "Imagen": "https://upload.wikimedia.org/wikipedia/commons/1/13/Plastic_pollution.jpg"
    },
    "Contaminación por ruido": {
        "ejemplo": "Tráfico urbano mundial",
        "Lugar": "Ciudades del mundo",
        "Descripción": "La urbanización y el aumento del tráfico generan niveles perjudiciales de ruido que afectan a millones.",
        "Consecuencias": [
            "Pérdida auditiva",
            "Estrés crónico",
            "Problemas cardíacos"
        ],
        "Impacto militar": [
            "Uso de sonido como arma psicológica.",
            "Fatiga y reducción del rendimiento en tropas urbanas."
        ],
        "Imagen": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Noise_pollution.jpg"
    },
    "Contaminación por petróleo": {
        "ejemplo": "Derrame del Golfo de México (2010)",
        "Lugar": "Golfo de México",
        "Descripción": "La explosión de una plataforma petrolera liberó millones de barriles al mar, con consecuencias devastadoras.",
        "Consecuencias": [
            "Daño a ecosistemas marinos y costeros",
            "Muerte masiva de especies",
            "Pérdidas económicas en turismo y pesca"
        ],
        "Impacto militar": [
            "Despliegue de unidades navales para contención.",
            "Vulnerabilidad de infraestructuras energéticas en tiempos de guerra."
        ],
        "Imagen": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Deepwater_Horizon_oil_spill_-_May_24%2C_2010.jpg"
    }
}

# Interfaz de usuario
st.set_page_config(page_title="🌍 Tipos de Contaminación Ambiental", layout="centered")
st.title("🌱 Tipos de Contaminación Ambiental y Ejemplos Históricos")

# Selección de tipo de contaminación
tipo = st.selectbox("📚 Selecciona un tipo de contaminación:", list(conceptos.keys()))

# Mostrar concepto
st.subheader(f"🧾 Concepto de {tipo}")
st.markdown(conceptos[tipo])

# Mostrar ejemplo asociado
data = ejemplos[tipo]
st.markdown("---")
st.subheader(f"📌 Ejemplo histórico: {data['ejemplo']}")
st.image(data["Imagen"], use_container_width=True, caption=f"{tipo} – {data['Lugar']}")
st.markdown(f"**📍 Lugar:** {data['Lugar']}")
st.markdown(f"**📝 Descripción:** {data['Descripción']}")

st.markdown("**⚠️ Consecuencias:**")
for c in data["Consecuencias"]:
    st.write(f"- {c}")

st.markdown("**🪖 Impacto militar:**")
for im in data["Impacto militar"]:
    st.write(f"- {im}")
