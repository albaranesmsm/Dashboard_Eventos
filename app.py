import os
import streamlit as st
from utils import (
   cargar_datos,
   grafico_eventos_provincia_poblacion,
   grafico_volumen_eventos,
   grafico_cantidad_equipos,
   grafico_evolucion_entregas_retiradas,
   grafico_plataforma_logistica
)
# === Forzar instalación de dependencias al iniciar ===
os.system('pip install --use-feature=fast-deps -r requirements.txt')
# === Configuración de la aplicación ===
st.title("Dashboard de Eventos Logísticos")
st.markdown("Visualización de datos de eventos logísticos de la compañía.")
# === Subida de archivo CSV ===
archivo = st.file_uploader("Sube el archivo CSV de eventos", type=["csv"])
if archivo:
   data = cargar_datos(archivo)
   st.subheader("Vista Previa de los Datos")
   st.write(data.head())
   # === Opciones de visualización ===
   st.sidebar.title("Visualizaciones Disponibles")
   opciones = [
       "Eventos por Provincia y Población",
       "Volumen Estimado por Evento",
       "Cantidad de Equipos por Evento",
       "Evolución de Entregas y Retiradas",
       "Eventos por Plataforma Logística"
   ]
   seleccion = st.sidebar.selectbox("Selecciona una visualización", opciones)
   # === Mostrar gráficos seleccionados ===
   if seleccion == "Eventos por Provincia y Población":
       st.subheader("Top 10 Provincias con más Eventos")
       grafico_eventos_provincia_poblacion(data)
   elif seleccion == "Volumen Estimado por Evento":
       st.subheader("Top 10 Eventos por Volumen Estimado")
       grafico_volumen_eventos(data)
   elif seleccion == "Cantidad de Equipos por Evento":
       st.subheader("Top 10 Eventos por Cantidad de Equipos")
       grafico_cantidad_equipos(data)
   elif seleccion == "Evolución de Entregas y Retiradas":
       st.subheader("Evolución de Entregas y Retiradas")
       grafico_evolucion_entregas_retiradas(data)
   elif seleccion == "Eventos por Plataforma Logística":
       st.subheader("Eventos por Plataforma Logística")
       grafico_plataforma_logistica(data)
else:
   st.warning("Por favor, sube un archivo CSV para visualizar los gráficos.")
