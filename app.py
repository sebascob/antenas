import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Configuración de la página web
st.set_page_config(page_title="Simulador de Radiopropagación", layout="wide")

st.title("📡 Plataforma Educativa y Simulador de Radiopropagación")
st.markdown("Bienvenida al simulador técnico para ingeniería de enlaces.")

# Menú lateral para navegar entre tus módulos
modulo = st.sidebar.selectbox(
    "Selecciona un Eje Temático",
    ["1. Pérdidas en Espacio Libre", "2. Línea de Vista (Tierra Curva)", "3. Presupuesto de Enlace (Link Budget)"]
)

# -----------------------------------------------------------------
# MÓDULO 1: ESPACIO LIBRE
# -----------------------------------------------------------------
if modulo == "1. Pérdidas en Espacio Libre":
    st.header("✨ Modelo de Pérdidas en Trayectoria (Friis)")
    
    # Submódulo Educativo
    with st.expander("📖 Ver Fundamento Teórico y Fórmulas"):
        st.write("La ecuación de Friis determina las pérdidas que sufre una onda electromagnética...")
        st.latex(r"FSPL (dB) = 32.44 + 20\log_{10}(d_{km}) + 20\log_{10}(f_{MHz})")

    # Controles Interactivos (Inputs del usuario)
    col1, col2 = st.columns(2)
    with col1:
        frecuencia = st.slider("Frecuencia de operación (MHz)", min_value=100, max_value=6000, value=2400, step=100)
    with col2:
        distancia_max = st.slider("Distancia máxima a graficar (km)", min_value=1, max_value=50, value=10)

    # Motor de Cálculo & Simulación Gráfica
    distancias = np.linspace(0.1, distancia_max, 200)
    perdidas = 32.44 + 20 * np.log10(distancias) + 20 * np.log10(frecuencia)

    # Crear gráfico interactivo con Plotly
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=distancias, y=perdidas, mode='lines', name='FSPL (dB)'))
    fig.update_layout(title=f"Pérdidas vs Distancia a {frecuencia} MHz", xaxis_title="Distancia (km)", yaxis_title="Pérdidas (dB)")
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Resultado numérico puntual
    st.metric(label=f"Pérdida calculada a {distancia_max} km", value=f"{perdidas[-1]:.2f} dB")
