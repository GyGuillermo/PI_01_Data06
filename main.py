from fastapi import FastAPI, Query, HTTPException
import pandas as pd
import os
import traceback
import polars as pl

app = FastAPI()

# 1 - Definimos una ruta
@app.get("/search")
# 1 - Funcion para obtener la Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
def search_by_keyword(plataforma: str, keyword: str):
    data = pd.read_csv('data_concatenada.csv')
    
    # Se filtra el dataframe para obtener los registros que comienzan con el primer caracter del parametro plataforma
    result = data[data['id'].str.startswith(plataforma[0])]
    #filtrar el dataframe según la keyword
    filtered_df = result[result['title'].str.contains(keyword)]

    #obtener la cantidad de veces que aparece la keyword en el título
    count = len(filtered_df)
    return {"plataforma ": plataforma, "keyword": keyword, "count": count}

# 2 - Definimos una ruta
@app.get("/movies/{plataforma}/{puntaje}/{year}")
# 2 - Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
def movie_for_platform(plataforma: str, puntaje: int, year: int):
    data = pd.read_csv('data_concatenada.csv')
    
    # Se filtra el dataframe para obtener los registros que comienzan con el primer caracter del parametro plataforma
    result = data[(data['id'].str[0] == plataforma[0])] 
    #filtrar el dataframe por mayor puntaje
    puntaje_df = result[(result['score'] > puntaje)] 
    # Filtarr por el año
    anio_df = puntaje_df[(puntaje_df['release_year'] == year)]
    cant = len(anio_df)
    return {"plataforma ": plataforma,"Cantidad de peliculas  ": cant}


# 3 - Definimos una ruta
@app.get('/movie/{plataforma}')

# 3 - Función para obtener la segunda película con el mayor score de una plataforma
def get_second_highest_movie_by_platform(plataforma: str):
    data_p = pl.read_csv('data_concatenada.csv', has_header=True)
    caract = plataforma[0]
    # Se filtra el DataFrame para obtener solo las filas con el año, plataforma y tipo de duración específicos
    filtered_df = data_p.filter(pl.col("id").str.contains(caract))
    sorted_df = filtered_df.sort("score", reverse=True)
    salida = sorted_df.row(1)
    title = salida[3]
    duration = salida[15]
    return {"plataforma ": plataforma,"título": title, "duración": duration}  
    
# 4 - Definimos una ruta
@app.get("/longest_movie/{plataforma}/{duration_type}/{year}")
# 4 - Función para determinar Película que más duró según año, plataforma y tipo de duración
def longest_movie(plataforma : str, duration_type: str, year: int):
    data_p = pl.read_csv('data_concatenada.csv', has_header=True)
    caract = plataforma[0]
    # Se filtra el DataFrame para obtener solo las filas con el año, plataforma y tipo de duración específicos
    filtered_df = data_p.filter(pl.col("id").str.contains(caract) & (pl.col("release_year") == year) & (pl.col("duration_type") == duration_type))
    sorted_df = filtered_df.sort("duration_int", reverse=True)
    salida = sorted_df.row(0)
    title = salida[3]
    duration = salida[15]
    return {"plataforma ": plataforma,"título": title, "duración": duration}
    
# 5 - Definimos una ruta
@app.get("/count_shows_movies_by_classification/{classification}")
# 5 - Cantidad de series y películas por rating
def count_shows_movies_by_classification(classification: str):
    data = pd.read_csv('data_concatenada.csv')
    # Se filtra el DataFrame para obtener solo las filas con la clasificación específica
   # Contar los registros de la columna 'col1' con el valor 2
    count = data.loc[data['rating'] == classification].shape[0]

    return {"Clasificación  " :classification, "Cantidad ":count}

    
    