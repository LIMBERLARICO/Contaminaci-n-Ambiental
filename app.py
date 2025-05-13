import streamlit as st

# Conceptos de cada tipo de contaminación
conceptos = {
    "Contaminación del suelo": "La contaminación del suelo ocurre cuando productos químicos, desechos peligrosos o basura alteran la calidad natural de la tierra, afectando la agricultura, el agua subterránea y la salud humana.",
    "Contaminación del aire": "La contaminación del aire se refiere a la presencia de sustancias tóxicas en la atmósfera que afectan la salud humana y el equilibrio ecológico, principalmente debido a la quema de combustibles fósiles.",
    "Contaminación del agua": "La contaminación del agua es la introducción de sustancias nocivas en ríos, lagos y océanos, afectando la vida acuática, la potabilidad del agua y el equilibrio ecológico.",
    "Contaminación por plásticos": "Los plásticos no biodegradables se acumulan en ambientes naturales, especialmente en océanos, causando daños irreparables a la fauna marina y entrando en la cadena alimenticia.",
    "Contaminación por petróleo": "Se refiere a los derrames de crudo o sus derivados en cuerpos de agua o suelo, causando desastres ecológicos, muerte de especies y graves impactos económicos y sociales.",
    "Contaminación por ruido": "El exceso de ruido proveniente del tráfico, industrias o actividades humanas afecta la salud auditiva, mental y la calidad de vida, especialmente en zonas urbanas."
}

# Ejemplos históricos de contaminación
ejemplos = {
    "Contaminación del suelo": [
        {
            "Ejemplo": "Love Canal (EE.UU., 1978)",
            "Lugar": "Nueva York, EE.UU.",
            "Descripción": "La contaminación del suelo en Love Canal se debió a la eliminación irresponsable de productos químicos industriales, lo que causó enfermedades graves en la población.",
            "Consecuencias": [
                "Evacuación de cientos de familias",
                "Aumento de cánceres y malformaciones",
                "Creación del programa Superfondo"
            ],
            "Impacto militar": "Impacto en la limpieza de residuos tóxicos en instalaciones militares.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/f/fc/Love_Canal_Contamination.jpg"
        },
        {
            "Ejemplo": "Desastre de Chernobyl (1986)",
            "Lugar": "Ucrania",
            "Descripción": "El desastre nuclear de Chernobyl contaminó extensas áreas del suelo con radiación, afectando ecosistemas y poblaciones cercanas.",
            "Consecuencias": [
                "Evacuación de miles de personas",
                "Contaminación de suelos y vegetación",
                "Riesgo de cáncer y enfermedades a largo plazo"
            ],
            "Impacto militar": "El accidente demostró la necesidad de medidas estrictas de seguridad en bases nucleares militares.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/a/a0/Chernobyl_Nuclear_Power_Plant.jpg"
        }
    ],
    "Contaminación del aire": [
        {
            "Ejemplo": "Gran Smog de Londres (1952)",
            "Lugar": "Reino Unido",
            "Descripción": "Un denso smog tóxico causado por la quema masiva de carbón cubrió Londres, causando miles de muertes por enfermedades respiratorias.",
            "Consecuencias": [
                "Miles de muertes por enfermedades respiratorias",
                "Mejora en las normativas de calidad del aire",
                "Mayor conciencia ambiental"
            ],
            "Impacto militar": "Demostró cómo la contaminación urbana puede tener efectos letales a gran escala, similar a los efectos de un ataque químico.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/6/68/Smog_London_1952.jpg"
        },
        {
            "Ejemplo": "Incendios forestales en California (2018)",
            "Lugar": "California, EE.UU.",
            "Descripción": "Los incendios forestales en California liberaron grandes cantidades de CO2 y partículas finas, afectando la calidad del aire en millones de personas.",
            "Consecuencias": [
                "Contaminación atmosférica masiva",
                "Enfermedades respiratorias y cardiovasculares",
                "Destrucción de ecosistemas"
            ],
            "Impacto militar": "El humo y las cenizas impactaron la visibilidad en zonas estratégicas y afectaron las operaciones militares en la región.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/e/e1/California_Wildfires_2018.jpg"
        }
    ],
    "Contaminación del agua": [
        {
            "Ejemplo": "Desastre de Minamata (1956)",
            "Lugar": "Japón",
            "Descripción": "La contaminación del agua en Minamata fue causada por la descarga de mercurio por una planta industrial, lo que afectó gravemente a la fauna y flora acuática.",
            "Consecuencias": [
                "Enfermedades neurológicas en humanos y animales",
                "Muerte de miles de especies marinas",
                "Reformas en la legislación ambiental japonesa"
            ],
            "Impacto militar": "El desastre demostró los peligros de los desechos industriales y la necesidad de monitorear las aguas cercanas a bases militares.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Minamata_disease_victims.jpg"
        },
        {
            "Ejemplo": "Derrame de petróleo en el Golfo de México (2010)",
            "Lugar": "Golfo de México, EE.UU.",
            "Descripción": "El derrame de BP fue el mayor desastre petrolero en la historia de EE.UU., afectando gravemente las aguas y la vida marina del Golfo.",
            "Consecuencias": [
                "Muerte de fauna marina",
                "Impacto en la economía local",
                "Regulaciones más estrictas en perforaciones petroleras"
            ],
            "Impacto militar": "La respuesta militar fue esencial para contener el derrame y evitar que se extendiera a áreas de importancia estratégica.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Deepwater_Horizon_oil_spill_-_May_24%2C_2010.jpg"
        }
    ],
    "Contaminación por plásticos": [
        {
            "Ejemplo": "Gran Mancha de Basura del Pacífico",
            "Lugar": "Océano Pacífico",
            "Descripción": "La acumulación de plásticos en el Pacífico está afectando gravemente a los ecosistemas marinos.",
            "Consecuencias": [
                "Pérdida de biodiversidad marina",
                "Microplásticos en la cadena alimentaria",
                "Daños irreparables a los ecosistemas oceánicos"
            ],
            "Impacto militar": "Los desechos plásticos interfieren con las operaciones navales y marítimas.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/1/13/Plastic_pollution.jpg"
        }
    ],
    "Contaminación por ruido": [
        {
            "Ejemplo": "Contaminación por ruido en ciudades",
            "Lugar": "Ciudades del mundo",
            "Descripción": "El crecimiento urbano y el tráfico vehicular generan altos niveles de ruido que afectan la salud de millones de personas.",
            "Consecuencias": [
                "Trastornos del sueño",
                "Pérdida auditiva",
                "Estrés y enfermedades cardiovasculares"
            ],
            "Impacto militar": "El ruido constante afecta la moral y concentración de las tropas durante operaciones en zonas urbanas.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/f/f6/Noise_pollution.jpg"
        }
    ],
    "Contaminación por petróleo": [
        {
            "Ejemplo": "Guerra del Golfo (1991)",
            "Lugar": "Kuwait",
            "Descripción": "Durante la Guerra del Golfo, Irak prendió fuego a pozos petroleros, liberando grandes cantidades de humo y contaminando la atmósfera.",
            "Consecuencias": [
                "Contaminación atmosférica masiva",
                "Daño a la salud de miles de personas",
                "Destrucción de recursos naturales"
            ],
            "Impacto militar": "El humo dificultó las operaciones militares y las estrategias de combate.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/b/b8/Kuwait_Oil_Fires.jpg"
        }
    ]
}

# Selector de categorías
tipo = st.selectbox("📚 Selecciona un tipo de contaminación:", list(conceptos.keys()))

# Mostrar concepto de contaminación
st.subheader(f"🧾 Concepto de {tipo}")
st.markdown(conceptos[tipo])

# Selección de ejemplo
ejemplo_seleccionado = st.selectbox(f"🔎 Selecciona un ejemplo de {tipo}:", [ejemplo["Ejemplo"] for ejemplo in ejemplos[tipo]])

# Mostrar el ejemplo seleccionado
for ejemplo in ejemplos[tipo]:
    if ejemplo["Ejemplo"] == ejemplo_seleccionado:
        st.subheader(f"📌 {ejemplo['Ejemplo']}")
        st.image(ejemplo["Imagen"], use_container_width=True, caption=ejemplo["Ejemplo"])
        st.markdown(f"**📍 Lugar:** {ejemplo['Lugar']}")
        st.markdown(f"**📝 Descripción:** {ejemplo['Descripción']}")
        st.markdown("**⚠️ Consecuencias:**")
        for c in ejemplo["Consecuencias"]:
            st.write(f"- {c}")
        st.markdown("**🪖 Impacto militar:**")
        st.write(ejemplo["Impacto militar"])
