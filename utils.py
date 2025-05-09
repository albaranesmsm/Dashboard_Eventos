import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# ==========================
# Función para cargar datos
# ==========================
def cargar_datos(archivo_csv):
   """
   Carga un archivo CSV en un DataFrame de pandas.
   """
   try:
       data = pd.read_csv(archivo_csv)
       data.columns = data.columns.str.strip()  # Eliminar espacios en los nombres de columnas
       return data
   except Exception as e:
       st.error(f"Error al cargar el archivo CSV: {e}")
       return None
# ==========================================
# Gráfico: Eventos por provincia y población
# ==========================================
def grafico_eventos_provincia_poblacion(data):
   """
   Genera un gráfico de barras mostrando los eventos por provincia y población.
   """
   plt.figure(figsize=(12, 6))
   eventos_provincia = data.groupby(['Provincia', 'Poblacion']).size().reset_index(name='Cantidad')
   sns.barplot(x='Provincia', y='Cantidad', hue='Poblacion', data=eventos_provincia, palette='Set2')
   plt.title('Eventos por Provincia y Población')
   plt.xticks(rotation=45)
   plt.tight_layout()
   st.pyplot(plt)
   plt.clf()
# ===============================
# Gráfico: Volumen estimado
# ===============================
def grafico_volumen_estimado(data):
   """
   Genera un gráfico de barras del volumen estimado por evento.
   """
   if 'Volumen Estimado' not in data.columns or 'Evento' not in data.columns:
       st.error("Las columnas 'Volumen Estimado' y/o 'Evento' no existen en el archivo.")
       return
   plt.figure(figsize=(12, 6))
   sns.barplot(x='Evento', y='Volumen Estimado', data=data, palette='Blues_r')
   plt.title('Volumen Estimado por Evento')
   plt.xticks(rotation=45)
   plt.tight_layout()
   st.pyplot(plt)
   plt.clf()
# ============================================
# Gráfico: Cantidad de equipos desplegados
# ============================================
def grafico_equipos_desplegados(data):
   """
   Genera un gráfico de barras mostrando la cantidad de equipos desplegados por evento.
   """
   if 'Evento' not in data.columns or 'Equipos Desplegados' not in data.columns:
       st.error("Las columnas 'Evento' y/o 'Equipos Desplegados' no existen en el archivo.")
       return
   plt.figure(figsize=(12, 6))
   sns.barplot(x='Evento', y='Equipos Desplegados', data=data, palette='Greens_r')
   plt.title('Cantidad de Equipos Desplegados por Evento')
   plt.xticks(rotation=45)
   plt.tight_layout()
   st.pyplot(plt)
   plt.clf()
# ===============================================
# Gráfico: Evolución de entregas y retiradas
# ===============================================
def grafico_evolucion_entregas_retiradas(data):
   """
   Genera un gráfico de línea mostrando la evolución de entregas y retiradas a lo largo del tiempo.
   """
   if 'Fecha' not in data.columns or 'Entregas' not in data.columns or 'Retiradas' not in data.columns:
       st.error("Las columnas 'Fecha', 'Entregas' y/o 'Retiradas' no existen en el archivo.")
       return
   data['Fecha'] = pd.to_datetime(data['Fecha'], errors='coerce')
   data = data.sort_values('Fecha')
   plt.figure(figsize=(12, 6))
   plt.plot(data['Fecha'], data['Entregas'], label='Entregas', marker='o')
   plt.plot(data['Fecha'], data['Retiradas'], label='Retiradas', marker='o')
   plt.title('Evolución de Entregas y Retiradas en el Tiempo')
   plt.xlabel('Fecha')
   plt.ylabel('Cantidad')
   plt.legend()
   plt.tight_layout()
   st.pyplot(plt)
   plt.clf()
# ========================================
# Gráfico: Eventos por plataforma logística
# ========================================
def grafico_eventos_por_plataforma(data):
   """
   Genera un gráfico de barras mostrando los eventos por plataforma logística.
   """
   if 'Plataforma Logística' not in data.columns:
       st.error("La columna 'Plataforma Logística' no existe en el archivo.")
       return
   plt.figure(figsize=(12, 6))
   eventos_plataforma = data['Plataforma Logística'].value_counts().reset_index()
   eventos_plataforma.columns = ['Plataforma Logística', 'Cantidad']
   sns.barplot(x='Plataforma Logística', y='Cantidad', data=eventos_plataforma, palette='Oranges_r')
   plt.title('Eventos por Plataforma Logística')
   plt.xticks(rotation=45)
   plt.tight_layout()
   st.pyplot(plt)
   plt.clf()
