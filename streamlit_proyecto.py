#comando que me ayudara a ver los resultados en la pagina que devo poner en la terminal: py -m streamlit run "streamlit proyecto.py"
import streamlit as st
import os

# ==========================
# CONFIG
# ==========================
st.set_page_config(
    page_title="Playlist Musical con Pilas",
    page_icon="🎵",
    layout="wide"
)

# ==========================
# ESTILO
# ==========================
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
}

/* TARJETAS */
div[data-testid="stVerticalBlock"] {
    background-color: #181818 !important;
    border: 2px solid #1DB954 !important;
    border-radius: 12px !important;
    padding: 10px !important;
    margin-bottom: 10px !important;
}

/* BOTONES */
.stButton > button {
    background-color: transparent !important;
    color: white !important;
    border: none !important;
    border-radius: 8px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #1DB954 !important;
    color: black !important;
}

</style>
""", unsafe_allow_html=True)

# ==========================
# BIBLIOTECA
# ==========================
canciones = [
    {"titulo": "Delirium - Anno Domini Beats", "imagen": "imagenes/Delirium.jpg", "audio": "musica/Delirium.mp3"},
    {"titulo": "Ten - Anno Domini Beats", "imagen": "imagenes/Ten.jpeg", "audio": "musica/Ten.mp3"},
    {"titulo": "To The End Of The World - National Sweetheart", "imagen": "imagenes/World.jpeg", "audio": "musica/World.mp3"},
    {"titulo": "Care Is Heavy - Jeremy Korpas, Rick Barry", "imagen": "imagenes/Care Is Heavy.jpg", "audio": "musica/Care Is Heavy.mp3"},
    {"titulo": "Elysian Fields - Jeremy Korpas, Rick Barry", "imagen": "imagenes/Elysian.jpg", "audio": "musica/Elysian.mp3"},
    {"titulo": "Tonight Again - Rod Kim", "imagen": "imagenes/Tonight Again.jpg", "audio": "musica/Tonight.mp3"},
    {"titulo": "The Fog - Trey Xavier", "imagen": "imagenes/The Fog.jpeg", "audio": "musica/The Fog.mp3"},
    {"titulo": "Working - Cory Barker", "imagen": "imagenes/Working.jpeg", "audio": "musica/Working.mp3"},
    {"titulo": "Taught Her How To Leave - Bill Douglas", "imagen": "imagenes/Taught.jpeg", "audio": "musica/Taught Her How To Leave.mp3"}
]

# ==========================
# STATE
# ==========================
if "playlist" not in st.session_state:
    st.session_state.playlist = []

# ==========================
# TÍTULO
# ==========================
st.markdown("""
<div style='text-align:center;'>
<h1 style='color:#1DB954;'>🎵 PLAYLIST MUSICAL CON PILAS</h1>
<h3>Alumno: Luis Fernando Rivera | Prof: Adriel Pastelino | Universidad Azteca</h3>
</div>
""", unsafe_allow_html=True)

# ==========================
# LAYOUT
# ==========================
col1, col2 = st.columns([3, 2])

# ==========================
# BIBLIOTECA
# ==========================
with col1:
    st.subheader("📚 Biblioteca Musical")

    for cancion in canciones:
        fila1, fila2, fila3 = st.columns([1, 4, 1])

        with fila1:
            st.image(cancion["imagen"], width=90)

        with fila2:
            st.markdown(
                f"<div class='glow-text'>{cancion['titulo']}</div>",
                unsafe_allow_html=True
            )

        with fila3:
            if st.button("➕", key=f"add_{cancion['titulo']}"):
                st.session_state.playlist.append(cancion)
                st.rerun()
# ==========================
# PLAYLIST LIMPIA
# ==========================
with col2:
    st.subheader("🎧 Mi Playlist")

    st.write(f"📊 Canciones en la pila: {len(st.session_state.playlist)}")

    if not st.session_state.playlist:
        st.info("Tu playlist está vacía")

    # ==========================
    # 🗑 VACÍAR (CENTRADO REAL)
    # ==========================
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)

    if st.button("🗑 Vaciar Playlist", use_container_width=False):
        st.session_state.playlist = []
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    # ==========================
    # ▶ REPRODUCIR (CENTRADO REAL)
    # ==========================
    st.markdown("<div style='text-align:center;'>", unsafe_allow_html=True)

    if st.button("▶ Reproducir", use_container_width=False):
        if st.session_state.playlist:
            cancion = st.session_state.playlist[-1]

            st.image(cancion["imagen"], width=280)

            st.markdown(
                f"<div class='glow-text'>🎧 REPRODUCIENDO: {cancion['titulo']}</div>",
                unsafe_allow_html=True
            )

            st.audio(cancion["audio"])
        else:
            st.warning("No hay canciones")

    st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    # ==========================
    # LISTA
    # ==========================
    for i in range(len(st.session_state.playlist)-1, -1, -1):
        cancion = st.session_state.playlist[i]

        col_nombre, col_boton = st.columns([8, 1])

        with col_nombre:
            st.write(cancion["titulo"])

        with col_boton:
            if st.button("❌", key=f"del_{i}"):
                st.session_state.playlist.pop(i)
                st.rerun()