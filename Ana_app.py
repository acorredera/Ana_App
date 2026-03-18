import streamlit as st
from PIL import Image, ImageOps
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Foto para Ana", page_icon="📸")

# Estilo personalizado con CSS para que sea más vistoso
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
    }
    h1 {
        color: #ff4b4b;
        text-align: center;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #555;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Cabecera dedicada
st.title("📸 App de Fotos de Ana")
st.markdown("<p class='subtitle'>¡Captura un momento especial y dale un toque mágico! ✨</p>", unsafe_allow_html=True)

# Sidebar para opciones
st.sidebar.header("🎨 Ajustes de Imagen")
filtro = st.sidebar.selectbox(
    "Elige un efecto:",
    ["Original", "Blanco y Negro", "Sepia", "Invertir Colores"]
)

# Componente de cámara
foto_capturada = st.camera_input("Hazte una foto")

if foto_capturada:
    # Abrir la imagen con PIL
    img = Image.open(foto_capturada)
    
    # Aplicar filtros según la selección
    if filtro == "Blanco y Negro":
        img = ImageOps.grayscale(img)
    elif filtro == "Invertir Colores":
        img = ImageOps.invert(img.convert("RGB"))
    elif filtro == "Sepia":
        # Filtro sepia manual
        sepia_data = np.array(img.convert("RGB"))
        t = [0.393, 0.769, 0.189, 0.349, 0.686, 0.168, 0.272, 0.534, 0.131]
        new_img = sepia_data.dot(np.array(t).reshape(3,3).T)
        new_img /= new_img.max()
        img = Image.fromarray((new_img * 255).astype(np.uint8))

    # Mostrar resultado
    st.success("¡Foto capturada con éxito! 🎉")
    st.image(img, caption=f"Versión: {filtro}", use_container_width=True)
    
    # Botón de descarga
    st.download_button(
        label="💾 Descargar foto para Ana",
        data=foto_capturada,
        file_name="foto_ana.png",
        mime="image/png"
    )
else:
    st.info("👆 Pulsa el botón de arriba para activar la cámara.")

# Pie de página
st.markdown("---")
st.caption("Hecho con ❤️ para Ana")