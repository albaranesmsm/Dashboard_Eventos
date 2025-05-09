import streamlit as st
import pandas as pd
import sys
import os
# Agregamos el directorio actual al PATH
sys.path.append(os.path.dirname(__file__))
# Importar funciones de utils.py
try:
   from utils import (
       cargar_datos,
       grafico_eventos_provincia_poblacion,
       grafico_volumen_estimado,
       grafico_equipos_desplegados,
       grafico_evolucion_entregas_retiradas,
       grafico_eventos_por_plataforma
   )
except ImportError as e:
   st.error(f"No se pudo importar utils.py: {e}")
# =======================
# Configuración de página
# =======================
st.set_page_config(page_title="Dashboard de Eventos", layout="wide")
st.title("Dashboard de Eventos")
st.write("Sube un archivo CSV para visualizar los datos:")
# =======================
# Carga del archivo CSV
# =======================
archivo = st.file_uploader("Subir CSV", type=["csv"])
if archivo:
   # Intentar cargar los datos
   try:
       data = cargar_datos(archivo)
       if data is None or data.empty:
           st.error("El archivo CSV no se ha cargado correctamente o está vacío.")
       else:
           # Mostrar vista previa
           st.subheader("Vista Previa de los Datos")
           st.write(data.head())
           st.write("Columnas encontradas:", list(data.columns))
           # =======================
           # Renderización de gráficos
           # =======================
           st.subheader("Eventos por Provincia y Población")
           try:
               grafico_eventos_provincia_poblacion(data)
           except Exception as e:
               st.error(f"Error en gráfico 'Eventos por provincia y población': {e}")
           st.subheader("Volumen Estimado por Evento")
           try:
               grafico_volumen_estimado(data)
           except Exception as e:
               st.error(f"Error en gráfico 'Volumen estimado por evento': {e}")
           st.subheader("Cantidad de Equipos Desplegados por Evento")
           try:
               grafico_equipos_desplegados(data)
           except Exception as e:
               st.error(f"Error en gráfico 'Equipos desplegados por evento': {e}")
           st.subheader("Evolución de Entregas y Retiradas a lo Largo del Tiempo")
           try:
               grafico_evolucion_entregas_retiradas(data)
           except Exception as e:
               st.error(f"Error en gráfico 'Evolución de entregas y retiradas': {e}")
           st.subheader("Eventos por Plataforma Logística")
           try:
               grafico_eventos_por_plataforma(data)
           except Exception as e:
               st.error(f"Error en gráfico 'Eventos por plataforma logística': {e}")
   except Exception as e:
       st.error(f"No se pudo cargar el archivo CSV: {e}")
else:
   st.info("Esperando un archivo CSV...")
