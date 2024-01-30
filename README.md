# <h1 align="center">**`Challenge`**</h1>

## Construido con

- Python
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit-learn
- Docker
- Fast Api

## Empezar

Para poder ejecutar los jupter nootbooks, puedes seguir los siguientes pasos.

### Prerrequisitos

  ```sh
  pip install requirements.txt
  ```

## **Objetivo**
Explore el conjunto de datos sobre vinos proporcionado para descubrir patrones, perfiles o correlaciones interesantes entre los diferentes componentes químicos de los vinos. El desafío es abierto y fomenta el análisis creativo y exploratorio.

## **Trabajo realizado**

Cada parte esta separada en jupyter notbooks.

### [`EDA` (Exploratory Data Analysis)](https://github.com/DamianAlbarino/Challenge-Wine/blob/main/EDA.ipynb)

### [`Clustering Analysis`](https://github.com/DamianAlbarino/Challenge-Wine/blob/main/Clustering-Analysis.ipynb)

### [`Creative Insights and Storytelling`](https://github.com/DamianAlbarino/Challenge-Wine/blob/main/Creative_Insights_and_Storytelling.ipynb)

## Tareas opcionales

### `Containerization and Data Retrieval`

#### Docker
En la carpeta [docker](https://github.com/DamianAlbarino/Challenge-Wine/tree/main/docker) se puede observar el Dockerfile y el script que se ejecuta en el contenedor. En el Dockerfile se incluyó todo el análisis de clustering, donde se cargan los datos solicitados a la API y se muestra la cantidad óptima de clusters para el dataframe ingresado, el dataframe con los tipos de vino definidos (0, 1, 2) y la cantidad de cada tipo.

##### Paso a paso para ejecutar el contenedor
1. Asegurate de tener docker instalado.
2. Posicionate en la carpeta docker
  ```sh
  cd docker/
  ```
3. Contruye la imagen docker:
  ```sh
  docker build -t wineimage .
  ```
4. Ejecuta el contenedor:
  ```sh
  docker run -it wineimage
  ```
  Esto iniciará tu aplicación dentro del contenedor.

#### API
Se generó con FastAPI una API que devuelve el JSON del CSV. El código se encuentra en la carpeta [`api`](https://github.com/DamianAlbarino/Challenge-Wine/tree/main/api) junto con los requisitos para su funcionamiento. Estos están separados ya que requieren menos librerías y para optimizar un poco la carga en Render, donde se realizó el deploy.

En la API, podemos observar que hay un endpoint GET:
* `/dataframe/`: Devuelve la información del dataframe proporcionado a partir del URL, el cual es utilizado en el script del contenedor.

Deploy: [Link](https://challenge-wine.onrender.com/docs)

## Contacto
- Correo Electrónico: [damianalbarino@hotmail.com](mailto:damianalbarino@hotmail.com)
- LinkedIn: [Damián Nicolas Albariño](https://www.linkedin.com/in/dami%C3%A1n-nicol%C3%A1s-albari%C3%B1o-b03b9a1ab/)