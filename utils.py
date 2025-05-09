
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

def cargar_datos(ruta_csv):
    data = pd.read_csv(ruta_csv, encoding='ISO-8859-1', delimiter=';')
    return data

def grafico_eventos_provincia_poblacion(data):
    plt.figure(figsize=(12, 6))
    eventos_por_provincia = data['Provincia'].value_counts().head(10)
    sns.barplot(x=eventos_por_provincia.index, y=eventos_por_provincia.values, palette='Set3')
    plt.title('Top 10 Provincias con más Eventos')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def grafico_volumen_eventos(data):
    plt.figure(figsize=(12, 6))
    top_eventos = data[['Nombre Evento', 'Volumen estimado (litros) Evento']].nlargest(10, 'Volumen estimado (litros) Evento')
    sns.barplot(x=top_eventos['Volumen estimado (litros) Evento'], y=top_eventos['Nombre Evento'], palette='Blues_r')
    plt.title('Top 10 Eventos por Volumen Estimado')
    plt.tight_layout()
    plt.show()

def grafico_cantidad_equipos(data):
    plt.figure(figsize=(12, 6))
    data['Total Equipos'] = (
        data['Cantidad Total de Botelleros'] +
        data['Cantidad Total de Mostradores'] +
        data['Cantidad Total de Vitrinas'] +
        data['Cantidad Total de Instalaciones Barril']
    )
    top_equipos = data[['Nombre Evento', 'Total Equipos']].nlargest(10, 'Total Equipos')
    sns.barplot(x=top_equipos['Total Equipos'], y=top_equipos['Nombre Evento'], palette='Greens_r')
    plt.title('Top 10 Eventos por Cantidad de Equipos')
    plt.tight_layout()
    plt.show()

def grafico_evolucion_entregas_retiradas(data):
    plt.figure(figsize=(12, 6))
    data['Fecha Entrega Evento'] = pd.to_datetime(data['Fecha Entrega Evento'], errors='coerce')
    data['Fecha Retirada Evento'] = pd.to_datetime(data['Fecha Retirada Evento'], errors='coerce')
    entregas = data['Fecha Entrega Evento'].dt.to_period('M').value_counts().sort_index()
    retiradas = data['Fecha Retirada Evento'].dt.to_period('M').value_counts().sort_index()
    plt.plot(entregas.index.astype(str), entregas.values, label='Entregas', marker='o')
    plt.plot(retiradas.index.astype(str), retiradas.values, label='Retiradas', marker='o')
    plt.title('Evolución de Entregas y Retiradas')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def grafico_plataforma_logistica(data):
    plt.figure(figsize=(10, 5))
    plataforma_counts = data['Plataforma Logística'].value_counts()
    sns.barplot(x=plataforma_counts.index, y=plataforma_counts.values, palette='Set2')
    plt.title('Eventos por Plataforma Logística')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
