# <h1 align="center">**`Challenge`**</h1>

## Construido con

- Python
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit-learn
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
En la carpeta [docker](https://github.com/DamianAlbarino/Challenge-Wine/tree/main/docker) se puede observar el dockerfile y el script que se ejecuta en el contenedor.
En el dockerfile se acopló todo el clustering analysis, donde se cargan los datos pedidos a la API, y se muestra la cantidad optima de clusters para el dataframe ingresado, el dataframe con los tipos de vino definidos (0,1,2) y la cantidad de cada tipo.

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
Se genero con Fast Api, una api que devuelve el json del csv. El codigo se encuentra en la carpeta [`api`](https://github.com/DamianAlbarino/Challenge-Wine/tree/main/api) junto con los requirements para su funcionamiento, estos estan separados ya que requieren menos librerias y para optimizar un poco la carga en Render, donde se hizo el deploy.

En la API podemos ver que hay un GET:
* `/dataframe/`: Devuelve la informacion del dataframe dado, desde su url, este es utilizado en el script del contenedor.

Deploy: [Link](https://challenge-wine.onrender.com/docs)

## Contacto
- Correo Electrónico: [damianalbarino@hotmail.com](mailto:damianalbarino@hotmail.com)
- LinkedIn: [Damián Nicolas Albariño](https://www.linkedin.com/in/dami%C3%A1n-nicol%C3%A1s-albari%C3%B1o-b03b9a1ab/)