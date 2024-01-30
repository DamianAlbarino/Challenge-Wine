import pandas as pd
import numpy as np
import requests

# Abrir csv

url = "https://challenge-wine.onrender.com/dataframe/"

response = requests.get(url)

if response.status_code == 200:
    # La solicitud fue exitosa, puedes acceder a los datos en formato JSON
    data = response.json()
    print('\nCSV Leido.\n')
else:
    print(f"Error al realizar la solicitud. Código de estado: {response.status_code}")

df = pd.DataFrame(data)

# Estandarizar los valores

from sklearn.preprocessing import MinMaxScaler

escalar = MinMaxScaler()

df_normalizado = pd.DataFrame(escalar.fit_transform(df), columns=df.columns)

df_normalizado.describe()


# Buscamos la cantidad optima de clusters con silhouette

from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans

# Creamos una lista donde iremos guardando los valores medios de silhouette
lista_sil = []

# Entrenamos un modelo para cada número de cluster que queremos testear
Cantidad_Clusters = np.arange(2,11)
for k in Cantidad_Clusters:
    # Definimos y entrenamos el modelo
    km = KMeans(n_clusters=k, max_iter=300)
    km = km.fit(df_normalizado)
    
    # Tomamos las etiquetas
    etiquetas = km.labels_
    
    # Calculamos el silhouette 
    valor_medio_sil = silhouette_score(df_normalizado, etiquetas)
    lista_sil.append(valor_medio_sil)

valor_max = max(lista_sil)
indice_max = lista_sil.index(valor_max)
print('---------------------------------------------------------\n')
print(f'La cantidad optima de cluster para este caso es: {Cantidad_Clusters[indice_max]}.\n')
print('---------------------------------------------------------\n')

# Crear modelo

modelo_kmeans = KMeans(n_clusters= Cantidad_Clusters[indice_max], max_iter=300) # Creamos el modelo

modelo_kmeans.fit(df_normalizado)                   # Entrenamos el modelo

df['Kmeans_Clusters'] = modelo_kmeans.labels_ # Clasificamos los vinos

print(df)

print(f'''
---------------------------------------------------------\n
Cantidad de tipo 0: {df[df["Kmeans_Clusters"]==0].shape[0]}.\n
---------------------------------------------------------\n
Cantidad de tipo 1: {df[df["Kmeans_Clusters"]==1].shape[0]}.\n
---------------------------------------------------------\n
Cantidad de tipo 2: {df[df["Kmeans_Clusters"]==2].shape[0]}.\n
''')