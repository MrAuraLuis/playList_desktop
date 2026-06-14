import streamlit as st
import os
st.set_page_config(
    page_title="Playlist Musical con Pilas",
    page_icon="🎵",
    layout="wide"
)
#comando que me ayudara a ver los resultados en la pagina que devo poner en la terminal: py -m streamlit run "streamlit proyecto.py"
#comando que me ayudara a ver los resultados en la pagina que devo poner en la terminal: python -m streamlit run streamlit_proyecto.py
# ===============================================================================
# ESTILO:
st.markdown("""
<style>

/* ANIMACIÓN GLOW */
@keyframes glowGreen {
    0% { text-shadow: 0 0 2px #1DB954; }
    50% { text-shadow: 0 0 10px #1DB954, 0 0 20px #1DB954; }
    100% { text-shadow: 0 0 2px #1DB954; }
}

/* TEXTO GLOW */
.glow-text {
    color: #1DB954;
    font-size: 24px;
    font-weight: 800;
    animation: glowGreen 1.8s infinite ease-in-out;
    text-shadow: 0 0 5px #1DB954, 0 0 15px #1DB954;
}

/* FONDO */
.stApp {
    background: linear-gradient(to right, #0f0f0f, #1a1a1a);
}

/* TEXTO */
p, span, div {
    color: #D6D6D6 !important;
}

/* TÍTULOS */
h1, h2, h3 {
    color: #FFFFFF !important;
    line-height: 1.3 !important;
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    overflow: visible !important;
}

/* TARJETAS */
div.block-container {
    background-color: #181818;
    border-radius: 12px;
    padding: 10px;
}

/* BOTONES */
.stButton > button {
    background-color: #1DB954 !important;
    color: black !important;
    border: none !important;
    border-radius: 8px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #17a74a !important;
    color: white !important;
}

/* RESPONSIVE PARA CELULARES */
@media (max-width: 768px) {

    .glow-text {
        font-size: 18px !important;
    }

    h1 {
        font-size: 28px !important;
    }

    h3 {
        font-size: 14px !important;
    }

    button {
        width: 100% !important;
    }

    div[data-testid="column"] {
        width: 100% !important;
        display: block !important;
    }

    .block-container {
        padding-left: 2rem;
        padding-right: 2rem;
    }

}

/* AYUDA EXTRA PARA EVITAR TÍTULOS CORTADOS */
div[data-testid="stMarkdownContainer"] {
    overflow: visible !important;
}

</style>
""", unsafe_allow_html=True)
# =======================================
# BIBLIOTECA:
RUTA_BASE = os.path.dirname(__file__)

st.write("RUTA_BASE =", RUTA_BASE)

st.write("Contenido de imagenes:")
st.write(os.listdir(os.path.join(RUTA_BASE, "imagenes")))

st.write("Contenido de musica:")
st.write(os.listdir(os.path.join(RUTA_BASE, "musica")))
canciones = [
    {
        "titulo": "Delirium - Anno Domini Beats",
        "imagen": os.path.join(RUTA_BASE, "imagenes", "delirium.jpg"),
        "audio": os.path.join(RUTA_BASE, "musica", "delirium.mp3"),
        "video": "https://youtu.be/qWW8sWC6xh0"
    },

    {
        "titulo": "Ten - Anno Domini Beats",
        "imagen": os.path.join(RUTA_BASE, "imagenes", "ten.jpg"),
        "audio": os.path.join(RUTA_BASE, "musica", "ten.mp3"),
        "video": "https://youtu.be/1uSqUmNbXD8"
    },

    {
        "titulo": "To The End Of The World - National Sweetheart",
        "imagen": os.path.join(RUTA_BASE, "imagenes", "world.jpg"),
        "audio": os.path.join(RUTA_BASE, "musica", "world.mp3"),
        "video": "https://youtu.be/Pm50tO-0yNs"
    },

    {
        "titulo": "Care Is Heavy - Jeremy Korpas, Rick Barry",
        "imagen": os.path.join(RUTA_BASE, "imagenes", "care is heavy.jpg"),
        "audio": os.path.join(RUTA_BASE, "musica", "care is heavy.mp3"),
        "video": "https://youtu.be/G5yOo4WLQPY"
    },

    {
        "titulo": "Elysian Fields - Jeremy Korpas, Rick Barry",
        "imagen": os.path.join(RUTA_BASE, "imagenes", "elysian.jpg"),
        "audio": os.path.join(RUTA_BASE, "musica", "elysian.mp3"),
        "video": "https://youtu.be/mFrADn0LNPY"
    },

    {
        "titulo": "Tonight Again - Rod Kim",
        "imagen": os.path.join(RUTA_BASE, "imagenes", "tonight.jpg"),
        "audio": os.path.join(RUTA_BASE, "musica", "tonight.mp3"),
        "video": "https://youtu.be/dd5A-1xdRIo"
    },

    {
        "titulo": "The Fog - Trey Xavier",
        "imagen": os.path.join(RUTA_BASE, "imagenes", "the fog.jpg"),
        "audio": os.path.join(RUTA_BASE, "musica", "the fog.mp3"),
        "video": "https://youtu.be/LOW48xnRZHM"
    },

    {
        "titulo": "Working - Cory Barker",
        "imagen": os.path.join(RUTA_BASE, "imagenes", "working.jpg"),
        "audio": os.path.join(RUTA_BASE, "musica", "working.mp3"),
        "video": "https://youtu.be/Zqo4DDYH4V0"
    },

    {
        "titulo": "Taught Her How To Leave - Bill Douglas",
        "imagen": os.path.join(RUTA_BASE, "imagenes", "taught.jpg"),
        "audio": os.path.join(RUTA_BASE, "musica", "taught.mp3"),
        "video": "https://youtu.be/UJaxd3W17GU"
    },

    {
        "titulo": "Lost Myself - Lalanne",
        "imagen": os.path.join(RUTA_BASE, "imagenes", "lost myself.jpg"),
        "audio": os.path.join(RUTA_BASE, "musica", "lost myself.mp3"),
        "video": "https://youtu.be/Baoa-2zEJHw"
    },
    
    {
        "titulo": "Gone Away - Blue Beat",
        "imagen": os.path.join(RUTA_BASE, "imagenes", "gone away.jpg"),
        "audio": os.path.join(RUTA_BASE, "musica", "gone away.mp3"),
        "video": "https://youtu.be/D2yUW4ckhrA"
    }
]
for cancion in canciones:
    if not os.path.exists(cancion["imagen"]):
        st.error(f"❌ Falta imagen: {cancion['imagen']}")
    if not os.path.exists(cancion["audio"]):
        st.error(f"❌ Falta audio: {cancion['audio']}")
# ====================================================
# STATE:
if "playlist" not in st.session_state:
    st.session_state.playlist = []
if "reproduciendo" not in st.session_state:
    st.session_state.reproduciendo = None
# ==========================
# ESPACIO SUPERIOR
st.markdown("""
<div style="height:100px;"></div>
""", unsafe_allow_html=True)
# =========================================
# TÍTULO:
st.markdown("""
<div style='text-align:center;'>
<h1 style='color:#1DB954;'> PLAYLIST MUSICAL CON PILAS</h1>
<h3>Alumno: Luis Fernando Rivera | Prof: Adriel Pastelino  Universidad Azteca</h3>
</div>
""", unsafe_allow_html=True)
# ===========================================================
# LAYOUT:
col1, col2 = st.columns([4, 1], gap="large")
# ============================================================
with col1:
    st.subheader("Biblioteca Musical:")
    cols = st.columns(3)
    for i, cancion in enumerate(canciones):
        with cols[i % 3]:
            st.markdown(
                """
                <div style='background:#181818; padding:10px; border-radius:12px;'>
                """,
                unsafe_allow_html=True
            )
            if os.path.exists(cancion["imagen"]):
                st.image(cancion["imagen"], use_container_width=True)
            else:
                st.warning(f"No existe: {cancion['imagen']}")
            st.markdown(
                f"<p style='text-align:center; font-weight:600'>{cancion['titulo']}</p>",
                unsafe_allow_html=True
            )
            if st.button("➕ Agregar", key=f"add_{i}"):
                st.session_state.playlist.append(cancion)
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)
#=========================================================================
# PLAYLIST LIMPIA:
with col2:
    st.subheader("Mi Playlist")
    st.write(f"Canciones en la pila: {len(st.session_state.playlist)}")
    if not st.session_state.playlist:
        st.info("Tu playlist está vacía")
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    if st.button("Vaciar Playlist", use_container_width=True):
        st.session_state.playlist = []
        st.session_state.reproduciendo = None
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
    st.write("")
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)
    if st.button("Reproducir", use_container_width=True):
        if st.session_state.playlist:
            st.session_state.reproduciendo = st.session_state.playlist[-1]
        else:
            st.warning("No hay canciones")
    st.markdown("</div>", unsafe_allow_html=True)
    st.divider()
# ==========================================
# REPRODUCTOR:
    if st.session_state.reproduciendo:
        cancion = st.session_state.reproduciendo
        st.markdown(
            f"<div class='glow-text'>🎧 REPRODUCIENDO: {cancion['titulo']}</div>",
            unsafe_allow_html=True
        )

# VIDEO DE YOUTUBE:
        if cancion.get("video", "").strip():
            st.video(cancion["video"])

# AUDIO + PORTADA:
        else:
            if os.path.exists(cancion["audio"]):
                st.audio(cancion["audio"])
            else:
                st.error(f"Audio no encontrado: {cancion['audio']}")
            if os.path.exists(cancion["imagen"]):
                st.image(
                    cancion["imagen"],
                    use_container_width=True
                )
            else:
                st.error(f"Imagen no encontrada: {cancion['imagen']}")
# =========================================================================
# LISTA:
    st.divider()
    st.subheader("Canciones")
    for i in range(len(st.session_state.playlist)-1, -1, -1):
        cancion = st.session_state.playlist[i]
        col_nombre, col_boton = st.columns([8, 1])
        with col_nombre:
            st.write(cancion["titulo"])
        with col_boton:
            if st.button("❌", key=f"del_{i}"):
                st.session_state.playlist.pop(i)
                if not st.session_state.playlist:
                    st.session_state.reproduciendo = None
                st.rerun()
