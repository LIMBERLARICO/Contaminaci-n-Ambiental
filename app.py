import streamlit as st

# Conceptos de cada tipo de contaminación
conceptos = {
    "Contaminación del suelo": "La contaminación del suelo ocurre cuando productos químicos, desechos peligrosos o basura alteran la calidad natural de la tierra, afectando la agricultura, el agua subterránea y la salud humana.",
    "Contaminación del aire": "La contaminación del aire se refiere a la presencia de sustancias tóxicas en la atmósfera que afectan la salud humana y el equilibrio ecológico, principalmente debido a la quema de combustibles fósiles.",
    "Contaminación del agua": "La contaminación del agua es la introducción de sustancias nocivas en ríos, lagos y océanos, afectando la vida acuática, la potabilidad del agua y el equilibrio ecológico.",
    "Contaminación por plásticos": "Los plásticos no biodegradables se acumulan en ambientes naturales, especialmente en océanos, causando daños irreparables a la fauna marina y entrando en la cadena alimentaria.",
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
            "Impacto militar": "Este desastre demostró la necesidad de vigilancia en la limpieza de productos químicos peligrosos cerca de instalaciones militares.",
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
            "Impacto militar": "Chernobyl evidenció la importancia de protocolos de seguridad nuclear, vital para la protección de instalaciones militares que manejan materiales radiactivos.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/a/a0/Chernobyl_Nuclear_Power_Plant.jpg"
        },
        {
            "Ejemplo": "Derrame de petróleo en Alaska (1989)",
            "Lugar": "Alaska, EE.UU.",
            "Descripción": "El derrame de petróleo en el Golfo de Alaska dejó grandes cantidades de petróleo en el suelo, afectando gravemente los ecosistemas.",
            "Consecuencias": [
                "Destrucción de hábitats naturales",
                "Contaminación de las aguas subterráneas",
                "Destrucción de ecosistemas marinos"
            ],
            "Impacto militar": "El desastre afectó las operaciones de las bases militares cercanas debido a la contaminación ambiental y los daños a las instalaciones.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Exxon_valdez_oil_spill.jpg"
        },
        {
            "Ejemplo": "Desastre de Bhopal (1984)",
            "Lugar": "India",
            "Descripción": "La fuga de gas tóxico de una planta de pesticidas en Bhopal contaminó el suelo y afectó gravemente la salud de miles de personas.",
            "Consecuencias": [
                "Miles de muertes",
                "Contaminación del aire y el suelo",
                "Reformas en la legislación industrial"
            ],
            "Impacto militar": "Este evento subrayó la necesidad de controlar las instalaciones industriales cercanas a zonas militares para evitar catástrofes ambientales.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Bhopal_disaster_cup.jpg"
        },
        {
            "Ejemplo": "Derrame de residuos tóxicos en el río Tinto (1998)",
            "Lugar": "España",
            "Descripción": "Un derrame masivo de residuos tóxicos contaminó el suelo y el agua, afectando el ecosistema del río Tinto.",
            "Consecuencias": [
                "Destrucción de fauna local",
                "Contaminación de los recursos hídricos",
                "Contaminación a largo plazo"
            ],
            "Impacto militar": "El desastre mostró cómo los derrames tóxicos pueden afectar los recursos naturales cruciales para las fuerzas militares.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/6/6b/R%C3%ADo_Tinto.jpg"
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
            "Impacto militar": "Este evento resaltó cómo la contaminación del aire puede afectar la salud de las tropas y disminuir la visibilidad, lo que sería un desafío para las operaciones militares urbanas.",
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
        },
        {
            "Ejemplo": "Contaminación por dióxido de nitrógeno en Beijing (2013)",
            "Lugar": "Beijing, China",
            "Descripción": "Un pico en la contaminación por dióxido de nitrógeno cubrió Beijing, alcanzando niveles peligrosos para la salud.",
            "Consecuencias": [
                "Aumento de enfermedades respiratorias",
                "Alertas sanitarias en la ciudad",
                "Estrategias para reducir la contaminación industrial"
            ],
            "Impacto militar": "La contaminación redujo la visibilidad, lo que dificultó las operaciones militares y afectó la preparación de las fuerzas armadas.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/a/a9/Beijing_air_pollution_in_2013.jpg"
        },
        {
            "Ejemplo": "Smog de Los Ángeles (1943)",
            "Lugar": "Los Ángeles, EE.UU.",
            "Descripción": "La combinación de dióxido de azufre, óxidos de nitrógeno y compuestos orgánicos volátiles generó uno de los smogs más graves en la historia de la ciudad.",
            "Consecuencias": [
                "Miles de casos de enfermedades respiratorias",
                "Aumento de las restricciones de emisiones",
                "Mejora de la legislación sobre calidad del aire"
            ],
            "Impacto militar": "El smog afectó la visibilidad y la salud de las tropas, demostrando cómo la contaminación del aire puede afectar las operaciones militares.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/3/3c/Smog_in_Los_Angeles_1940.jpg"
        },
        {
            "Ejemplo": "Contaminación por partículas finas en Nueva Delhi (2019)",
            "Lugar": "Nueva Delhi, India",
            "Descripción": "La ciudad alcanzó niveles extremos de contaminación por partículas finas (PM2.5), lo que generó una crisis sanitaria.",
            "Consecuencias": [
                "Problemas respiratorios masivos",
                "Alertas sanitarias y cierres temporales de escuelas",
                "Incremento de enfermedades cardiovasculares"
            ],
            "Impacto militar": "El aire extremadamente contaminado afectó las capacidades operativas en la ciudad, obstaculizando las actividades logísticas de las fuerzas armadas.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/7/7b/Delhi_smog_2019.jpg"
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
        },
        {
            "Ejemplo": "Derrame de residuos en el río Napo (1991)",
            "Lugar": "Amazonas, Ecuador",
            "Descripción": "La contaminación del agua del río Napo debido a residuos de una empresa petrolera afectó a miles de personas.",
            "Consecuencias": [
                "Contaminación de agua potable",
                "Destrucción de ecosistemas acuáticos",
                "Problemas de salud en la población local"
            ],
            "Impacto militar": "El desastre afectó la disponibilidad de agua para las operaciones militares en la región.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/2/28/Oil_spill_in_the_amazon.jpg"
        },
        {
            "Ejemplo": "Fugas radiactivas en el río Techa (1957)",
            "Lugar": "Rusia",
            "Descripción": "La planta de plutonio de Mayak vertió desechos radiactivos en el río Techa, afectando el agua y los habitantes cercanos.",
            "Consecuencias": [
                "Contaminación radiactiva",
                "Enfermedades de la piel y cáncer",
                "Reubicación de comunidades cercanas"
            ],
            "Impacto militar": "Este desastre evidenció los riesgos de las instalaciones de producción de armas nucleares cercanas a fuentes de agua.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/7/73/Mayak_radioactive_waste_storage_1957.jpg"
        },
        {
            "Ejemplo": "Contaminación del río Ganges (India)",
            "Lugar": "India",
            "Descripción": "El Ganges es uno de los ríos más contaminados del mundo, recibiendo residuos industriales, humanos y agrícolas.",
            "Consecuencias": [
                "Enfermedades gastrointestinales",
                "Contaminación masiva de ecosistemas acuáticos",
                "Impacto en el acceso al agua potable"
            ],
            "Impacto militar": "El río Ganges es crucial para muchas bases militares en India; su contaminación afecta la seguridad del agua.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/d/d7/Ganges_river.jpg"
        }
    ]
    # Continúa agregando más ejemplos para plástico, petróleo y ruido
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
