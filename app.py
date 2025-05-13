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
            "Impacto militar": "El desastre de Love Canal subrayó la necesidad de supervisar la limpieza de productos químicos y desechos peligrosos cerca de bases militares, para evitar daños a los ecosistemas y personas cercanas a instalaciones sensibles.",
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
            "Impacto militar": "La catástrofe demostró la necesidad de protocolos estrictos de seguridad en instalaciones nucleares militares, ya que la contaminación radiactiva puede comprometer la seguridad de las fuerzas armadas y su capacidad operativa.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/a/a0/Chernobyl_Nuclear_Power_Plant.jpg"
        },
        {
            "Ejemplo": "Desastre de Bhopal (1984)",
            "Lugar": "Bhopal, India",
            "Descripción": "Un escape de gas tóxico de una planta de pesticidas causó la muerte de miles de personas y contaminó el suelo con productos químicos peligrosos.",
            "Consecuencias": [
                "Miles de muertes y enfermedades a largo plazo",
                "Contaminación del suelo con productos químicos",
                "Cambios en la legislación y control de químicos industriales"
            ],
            "Impacto militar": "Este desastre mostró la vulnerabilidad de las bases militares cercanas a fábricas químicas, que pueden enfrentar riesgos de contaminación accidental de materiales peligrosos.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/0/0a/Bhopal_disaster.jpg"
        },
        {
            "Ejemplo": "Desastre de Fukushima (2011)",
            "Lugar": "Fukushima, Japón",
            "Descripción": "El tsunami y el colapso de la planta nuclear Fukushima liberaron materiales radiactivos al suelo, causando daños a largo plazo en la agricultura y el ecosistema.",
            "Consecuencias": [
                "Contaminación radiactiva del suelo",
                "Evacuación masiva de residentes",
                "Impacto en la economía local"
            ],
            "Impacto militar": "La contaminación radiactiva del suelo dificultó la respuesta militar y las misiones de rescate, mostrando cómo desastres nucleares pueden comprometer las zonas de operaciones.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/f/f5/Fukushima_Nuclear_Plant_after_earthquake.jpg"
        },
        {
            "Ejemplo": "Desastre de Cidra (1977)",
            "Lugar": "Cidra, Puerto Rico",
            "Descripción": "Un accidente de derrame de productos químicos industriales afectó el suelo y el agua en Cidra, resultando en una gran crisis ambiental.",
            "Consecuencias": [
                "Contaminación del agua y del suelo",
                "Desplazamiento de familias",
                "Mayor regulación sobre la disposición de desechos industriales"
            ],
            "Impacto militar": "El desastre afectó la capacidad de las fuerzas militares para realizar entrenamientos en el área y destacó la importancia de la seguridad medioambiental en instalaciones militares.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Cidra_PR.jpg"
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
            "Impacto militar": "El humo y las cenizas impactaron la visibilidad y las operaciones militares, dificultando el desplazamiento y la efectividad en la región afectada.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/e/e1/California_Wildfires_2018.jpg"
        },
        {
            "Ejemplo": "Contaminación del aire en Pekín (2013)",
            "Lugar": "Pekín, China",
            "Descripción": "Niveles extremadamente altos de contaminación del aire afectaron la salud de millones de personas y causaron miles de muertes prematuras.",
            "Consecuencias": [
                "Aumento de enfermedades respiratorias",
                "Desplazamiento de actividades al aire libre",
                "Restricciones en el tráfico"
            ],
            "Impacto militar": "La mala calidad del aire también afectó las operaciones militares, especialmente en cuanto a visibilidad y salud de los soldados.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/7/79/Beijing_smog_2013.jpg"
        },
        {
            "Ejemplo": "Smog de Los Ángeles (1940s)",
            "Lugar": "Los Ángeles, EE.UU.",
            "Descripción": "La quema de combustibles fósiles en una ciudad altamente industrializada creó niveles de smog peligrosos.",
            "Consecuencias": [
                "Problemas respiratorios generalizados",
                "Desarrollo de políticas para combatir la contaminación"
            ],
            "Impacto militar": "Este tipo de contaminación afectó la capacidad de las fuerzas militares para entrenar y operar en áreas urbanas debido a la mala calidad del aire.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Los_Angeles_smog.jpg"
        },
        {
            "Ejemplo": "Quema de combustibles en la Guerra del Golfo (1991)",
            "Lugar": "Irak",
            "Descripción": "Irak prendió fuego a pozos petroleros, creando enormes nubes de humo que afectaron el aire de la región.",
            "Consecuencias": [
                "Contaminación atmosférica masiva",
                "Problemas de salud en la población y las tropas"
            ],
            "Impacto militar": "El humo denso dificultó las operaciones militares, afectando la visibilidad y la calidad del aire para los soldados.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/4/47/Kuwait_oil_fires.jpg"
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
            "Ejemplo": "Derrame de Exxon Valdez (1989)",
            "Lugar": "Alaska, EE.UU.",
            "Descripción": "El derrame de petróleo de Exxon Valdez causó una devastación ecológica en las aguas de Alaska.",
            "Consecuencias": [
                "Muerte de miles de aves y mamíferos marinos",
                "Impacto económico devastador para la pesca",
                "Mejoras en la regulación de derrames de petróleo"
            ],
            "Impacto militar": "Este desastre llevó a un mayor enfoque en la protección de las zonas costeras estratégicas y la intervención rápida en caso de emergencias petroleras.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/0/04/Exxon_Valdez_oil_spill.jpg"
        },
        {
            "Ejemplo": "Derrame en el Río Amazonas (2015)",
            "Lugar": "Brasil",
            "Descripción": "Un derrame de desechos mineros contaminó las aguas del Amazonas, afectando la biodiversidad local.",
            "Consecuencias": [
                "Muerte de peces y animales acuáticos",
                "Impacto en la salud de las comunidades locales",
                "Destrucción de ecosistemas acuáticos"
            ],
            "Impacto militar": "Las fuerzas militares locales tuvieron que intervenir para asistir en la limpieza y prevención de más daños ecológicos en una de las regiones más biodiversas del planeta.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Rio_dos_Mendes_-_contaminado.jpg"
        },
        {
            "Ejemplo": "Derrame en la costa de Nigeria (2008)",
            "Lugar": "Delta del Níger, Nigeria",
            "Descripción": "Varios derrames de petróleo afectaron las aguas y ecosistemas locales en el Delta del Níger.",
            "Consecuencias": [
                "Destrucción de hábitats marinos",
                "Contaminación masiva de recursos hídricos",
                "Problemas económicos y sociales para las comunidades locales"
            ],
            "Impacto militar": "Los derrames dificultaron las operaciones militares en la región, especialmente en cuanto al acceso a recursos y seguridad local.",
            "Imagen": "https://upload.wikimedia.org/wikipedia/commons/d/d6/Nigerian_oil_spill.jpg"
        }
    ],
    # Aquí puedes seguir agregando más ejemplos para la contaminación por plásticos y por ruido de la misma forma...
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
