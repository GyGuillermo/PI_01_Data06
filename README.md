# PI_01_Data06 - PROYECTO INDIVIDUAL Nº1

![image](https://user-images.githubusercontent.com/43472426/213601305-9b7e29de-4454-46cf-97b4-85fe8d0a207b.png)

# Proyecto de Data Engineering

Este proyecto tiene como objetivo automatizar las transformaciones necesarias y disponibilizar los datos mediante una API, para optimizar las actividades del área de análisis de datos de una empresa.

## Transformaciones

* Generación de un campo id único para cada plataforma, compuesto por la primera letra del nombre de la plataforma y el show_id ya presente en los datasets.Reemplazo de valores nulos en el campo rating por el string "G" (corresponde al maturity rating: "general for all audiences").

* Conversión de las fechas a formato AAAA-mm-dd.

* Conversión de los campos de texto a minúsculas.

* División del campo duration en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

## API

Para disponibilizar los datos, se ha desarrollado una API utilizando el framework FastAPI. 
Esta API permite realizar consultas como:

* Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

* Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
 
* La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

* Película que más duró según año, plataforma y tipo de duración

* Cantidad de series y películas por rating

## Deployment

Para llevar a cabo el deploy de la aplicación, se ha utilizado Deta. Sin embargo, también exite la posibilidad de usar Railway y Render, estas ultimas requieren de un proceso de dockerización.

## Requerimientos

Para ejecutar este proyecto, es necesario tener instalado:

* Python 3.6 o superior
* Las librerías especificadas en el archivo requirements.txt

## Instrucciones de ejecución

* Clonar este repositorio en su máquina local

* Instalar las dependencias necesarias ejecutando pip install -r requirements.txt en la carpeta del proyecto

* Ejecutar el archivo main.py para iniciar la API

* Acceder a la URL especificada en la consola para utilizar la API





