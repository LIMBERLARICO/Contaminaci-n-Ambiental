import streamlit as st

contaminaciones = {
    "Contaminación del aire": {
        "Descripción": "La contaminación del aire se produce cuando sustancias nocivas entran a la atmósfera, como gases y partículas que afectan la salud humana y el clima.",
        "Causas": [
            "Emisiones de vehículos",
            "Quema de combustibles fósiles",
            "Industrialización y actividades humanas",
            "Quema de basura",
            "Uso de pesticidas y fertilizantes"
        ],
        "Consecuencias": [
            "Problemas respiratorios (asma, bronquitis, cáncer de pulmón)",
            "Lluvia ácida",
            "Cambio climático global",
            "Mortalidad prematura",
            "Daño a la flora y fauna"
        ],
        "Ejemplo histórico": {
            "Nombre": "Gran Smog de Londres",
            "Año": 1952,
            "Lugar": "Reino Unido",
            "Descripción": "Un espeso smog de dióxido de azufre y partículas de carbón cubrió Londres, causando la muerte de más de 4,000 personas y creando conciencia sobre la contaminación del aire."
        },
        "Impacto militar": [
            "Las emisiones de guerra incrementan la contaminación del aire, afectando a soldados y civiles.",
            "Durante la Guerra del Golfo, se incendiaron pozos petroleros, liberando grandes cantidades de humo tóxico."
        ],
        "Imagen": "https://upload.wikimedia.org/wikipedia/commons/3/33/Air_pollution_by_industry.jpg"
    },
    "Contaminación del agua": {
        "Descripción": "La contaminación del agua se produce cuando el agua se contamina con productos químicos, metales pesados, residuos humanos o industriales.",
        "Causas": [
            "Vertidos industriales",
            "Desperdicio de aguas residuales",
            "Uso excesivo de pesticidas en agricultura",
            "Extracción de petróleo y minería",
            "Basura y plásticos arrojados en ríos y océanos"
        ],
        "Consecuencias": [
            "Contaminación de fuentes de agua potable",
            "Destrucción de ecosistemas acuáticos",
            "Contaminación de alimentos marinos",
            "Enfermedades transmitidas por el agua (cólera, disentería)",
            "Pérdida de biodiversidad acuática"
        ],
        "Ejemplo histórico": {
            "Nombre": "Desastre de Minamata",
            "Año": 1956,
            "Lugar": "Japón",
            "Descripción": "La liberación de mercurio por una industria química en la bahía de Minamata causó enfermedades neurológicas graves a los habitantes y a la vida marina."
        },
        "Impacto militar": [
            "Las guerras destruyen las infraestructuras de tratamiento de agua, afectando a la población civil.",
            "Envenenamiento de fuentes de agua durante conflictos militares."
        ],
        "Imagen": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Pollution_in_the_Ganges_river.jpg"
    },
    "Contaminación del suelo": {
        "Descripción": "La contaminación del suelo ocurre cuando sustancias químicas y desechos sólidos dañan la calidad del suelo, afectando tanto a la salud humana como al medio ambiente.",
        "Causas": [
            "Vertidos de productos químicos industriales",
            "Uso excesivo de pesticidas y fertilizantes",
            "Deforestación y destrucción del hábitat",
            "Residuos de la industria minera",
            "Desechos sólidos urbanos"
        ],
        "Consecuencias": [
            "Degradación de la fertilidad del suelo",
            "Contaminación de cultivos y alimentos",
            "Contaminación de fuentes de agua subterránea",
            "Pérdida de biodiversidad y destrucción de ecosistemas",
            "Riesgos para la salud humana a través de alimentos contaminados"
        ],
        "Ejemplo histórico": {
            "Nombre": "Destrucción de la Tierra por pesticidas en el siglo XX",
            "Año": "1940-1980",
            "Lugar": "Mundial",
            "Descripción": "El uso indiscriminado de pesticidas como el DDT en la agricultura afectó al suelo, a la fauna y a los seres humanos."
        },
        "Impacto militar": [
            "Los conflictos bélicos destruyen grandes áreas de suelo productivo.",
            "La contaminación por residuos de armas y municiones afecta la calidad del suelo en zonas de guerra."
        ],
        "Imagen": "https://upload.wikimedia.org/wikipedia/commons/6/66/Soil_pollution.jpg"
    },
    "Contaminación por plásticos": {
        "Descripción": "El vertido masivo de plásticos en la naturaleza, especialmente en océanos, es una de las formas más graves de contaminación actual.",
        "Causas": [
            "Desechos plásticos no biodegradables",
            "Uso excesivo de plásticos de un solo uso",
            "Falta de infraestructura adecuada de reciclaje",
            "Desperdicio de plásticos en vertederos y mares"
        ],
        "Consecuencias": [
            "Daño a la vida marina (incluso muerte por ingestión de plásticos)",
            "Contaminación visual en playas y océanos",
            "Liberación de sustancias tóxicas al medio ambiente",
            "Inestabilidad de los ecosistemas marinos",
            "Acumulación de microplásticos en alimentos humanos"
        ],
        "Ejemplo histórico": {
            "Nombre": "Isla de plásticos en el Pacífico",
            "Año": "Siglo XXI",
            "Lugar": "Oceano Pacífico",
           "Descripción": "Un gran cúmulo de basura plástica flotante, conocido como la \"Gran Mancha de Basura del Pacífico\", afecta a los ecosistemas marinos y a la vida acuática."
        },
        "Impacto militar": [
            "Las fuerzas armadas a menudo contribuyen a la contaminación de plásticos en zonas conflictivas.",
            "El uso de plásticos en equipos militares genera grandes cantidades de residuos en las zonas de guerra."
        ],
        "Imagen": "https://upload.wikimedia.org/wikipedia/commons/1/13/Plastic_pollution.jpg"
    },
    "Contaminación por ruido": {
        "Descripción": "La contaminación acústica es la presencia de ruidos indeseados que afectan la salud de los seres humanos y la fauna.",
        "Causas": [
            "Tráfico vehicular",
            "Actividad industrial",
            "Construcción y maquinaria pesada",
            "Actividades recreativas ruidosas",
            "Sonido excesivo de maquinaria y equipos"
        ],
        "Consecuencias": [
            "Estrés y trastornos de salud mental",
            "Problemas auditivos (pérdida de audición)",
            "Impacto negativo en animales (desorientación y estrés)",
            "Interferencia con el descanso y sueño",
            "Disminución de la calidad de vida urbana"
        ],
        "Ejemplo histórico": {
            "Nombre": "Contaminación por ruido en grandes ciudades",
            "Año": "Siglo XXI",
            "Lugar": "Ciudades del mundo",
            "Descripción": "El aumento de tráfico en áreas urbanas ha causado niveles alarmantes de contaminación acústica, afectando la salud de los habitantes urbanos."
        },
        "Impacto militar": [
            "El ruido de las operaciones militares genera estrés y afecta la capacidad de los soldados.",
            "En los campos de batalla, el ruido constante puede generar efectos psicológicos negativos en los combatientes."
        ],
        "Imagen": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Noise_pollution.jpg"
    }
}

# Interfaz Streamlit
st.set_page_config(page_title="Contaminación Ambiental Didáctica", layout="centered")
st.title("🌍 Contaminación Ambiental y sus Consecuencias")

tipo = st.selectbox("🔍 Selecciona un tipo de contaminación:", list(contaminaciones.keys()))

if tipo:
    data = contaminaciones[tipo]

    st.subheader(f"📘 {tipo}")
    
    # Mostrar imagen si existe
    if "Imagen" in data:
        st.image(data["Imagen"], use_container_width=True, caption=f"Ejemplo visual de {tipo.lower()}")

    st.markdown(f"**🧾 Descripción:** {data['Descripción']}")

    st.markdown("**🔥 Causas:**")
    for causa in data["Causas"]:
        st.write(f"- {causa}")

    st.markdown("**⚠️ Consecuencias ambientales:**")
    for efecto in data["Consecuencias"]:
        st.write(f"- {efecto}")

    st.markdown("**📚 Ejemplo histórico relevante:**")
    ejemplo = data["Ejemplo histórico"]
    st.write(f"📌 **{ejemplo['Nombre']}** ({ejemplo['Año']}, {ejemplo['Lugar']})")
    st.info(ejemplo["Descripción"])

    st.markdown("**🔰 Impacto militar asociado:**")
    for impacto in data["Impacto militar"]:
        st.write(f"- {impacto}")
