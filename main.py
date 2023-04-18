import pandas as pd

from typing import Optional
from typing import Dict
from pydantic import BaseModel
from fastapi import FastAPI,Body,Query


#creacion de la app
app:FastAPI = FastAPI();


ruta_amazon = r"df_limpios/DF_Amazon.csv"
amazon_df = pd.read_csv(ruta_amazon)
ruta_disney = r"df_limpios/DF_Disney.csv"
disney_df = pd.read_csv(ruta_disney)
ruta_netflix = r"df_limpios/DF_Netflix.csv"
netflix_df = pd.read_csv(ruta_netflix)
ruta_hulu = r"df_limpios/DF_Hulu.csv"
hulu_df = pd.read_csv(ruta_hulu)

ruta_score = r"ratings\GroupBy_Year_MovieId_MeanforRating.csv"
score_movies_df = pd.read_csv(ruta_score)

ruta_archivo1 = r"catalogo/total_movie_for_rating.csv"
only_content_and_score = pd.read_csv(ruta_archivo1)

ruta_archivo1 = r"catalogo/total_movie_for_rating.csv"
only_content_and_score = pd.read_csv(ruta_archivo1)

def contar_peliculas(dataframe):
   #este def contara solo las "movie" de cada plataforma, y las devolvera
   if dataframe == "1" or dataframe == "amazon":
      cant_peliculas =amazon_df[amazon_df["type"] == "movie"]
      return cant_peliculas.shape[0]
   elif dataframe == "2" or dataframe == "netflix":
      cant_peliculas =netflix_df[netflix_df["type"] == "movie"]
      return cant_peliculas.shape[0]
   elif dataframe == "3" or dataframe == "disney":
      cant_peliculas =disney_df[disney_df["type"] == "movie"]
      return cant_peliculas.shape[0]
   elif dataframe == "4" or dataframe == "hulu":
      cant_peliculas =hulu_df[hulu_df["type"] == "movie"]
      return cant_peliculas.shape[0]
   else:
      return "error:plataforma incorrecta"

def contar_peliculas(dataframe):
   #este def contara el numero de contenidos
   count_peliculas = only_content_and_score.loc[(only_content_and_score['rating'] >= dataframe)]
   contenidos = count_peliculas.shape[0]
   return contenidos

def saberid(dataframe, anio):
    # este def solo el id de una pelicula especifica
   if dataframe == "1" or dataframe == "amazon":
      estas_peliculas = amazon_df.loc[(amazon_df['type'] == "movie") & (amazon_df['release_year'] == int(anio))]
      id_max = estas_peliculas['duration_int'].idxmax()
      show_title = estas_peliculas.loc[id_max,'title']
      show_duration = estas_peliculas.loc[id_max,'duration_int']
      return show_title,show_duration
   elif dataframe == "2" or dataframe == "netflix":
      estas_peliculas = netflix_df.loc[(netflix_df['type'] == "movie") & (netflix_df['release_year'] == int(anio))]
      id_max = estas_peliculas['duration_int'].idxmax()
      show_title = estas_peliculas.loc[id_max,'title']
      show_duration = estas_peliculas.loc[id_max,'duration_int']
      return show_title,show_duration
   elif dataframe == "3" or dataframe == "disney":
      estas_peliculas = disney_df.loc[(disney_df['type'] == "movie") & (disney_df['release_year'] == int(anio))]
      id_max = estas_peliculas['duration_int'].idxmax()
      show_title = estas_peliculas.loc[id_max,'title']
      show_duration = estas_peliculas.loc[id_max,'duration_int']
      return show_title,show_duration
   elif dataframe == "4" or dataframe == "hulu":
      estas_peliculas = hulu_df.loc[(hulu_df['type'] == "movie") & (hulu_df['release_year'] == int(anio))]
      id_max = estas_peliculas['duration_int'].idxmax()
      show_title = estas_peliculas.loc[id_max,'title']
      show_duration = estas_peliculas.loc[id_max,'duration_int']
      return show_title,show_duration
   else: 
      return "error: dato no valido"

def score_count(dataframe, scored, year):
#muestra la cantidad de peliculas con un score especifico
   compania = None

   if dataframe == "1" or dataframe == "amazon":
      compania = "amazon"
   elif dataframe == "2" or dataframe == "netflix":
      compania = "netflix"
   elif dataframe == "3" or dataframe == "disney":
      compania = "disney"
   elif dataframe == "4" or dataframe == "hulu":
      compania = "hulu"
   else:
      return "error"

   count_peliculas = score_movies_df.loc[(score_movies_df['compania'] == compania) & (score_movies_df['year'] == int(year)) & (score_movies_df['rating'] >= scored)] 
   cantidad = count_peliculas.shape[0]
   return cantidad


#appdef
@app.get("/")
async def home():
   lineas = [
      "BIENVENIDO",
      "",
      "estos son los path que existen:",
      "",
      "Cuantas Peliculas hay en esta plataforma",
      "@app.get(\"/get_count_platform/{plataforma}\")",
      "","",
      "Pelicula mas larga en determinado año y plataforma",
      "@app.get(\"/get_max_duration/{year}/{plataforma}\")",
      "","",
      "Cantidad de peliculas con un score superior al dado",
      "@app.get(\"/get_score_count/{platform}/{scored}/{year}\")",
      "","",
      "Cantidad de contenido total con un score superior",
      "@app.get(\"/get_contents/{rating}\")",   
   ]
   return "\n".join(lineas) 


#Cuantas Peliculas hay en esta plataforma
@app.get("/get_count_platform/{plataforma}")
async def plataforma(plataforma:str):
   cantidad=contar_peliculas(str(plataforma))
   return cantidad

#Pelicula mas larga
@app.get("/get_max_duration/{year}/{plataforma}")
async def get_max_duration(year: int, plataforma: str):
   titleMovie,durationMovie = saberid(plataforma, year)
   return (f'Movie{titleMovie} || Duration:{durationMovie}')

#cantidad de peliculas con un score superior
@app.get("/get_score_count/{platform}/{scored}/{year}")
async def get_score_count(platform:str, scored: int, year: str):
   cantidad=score_count(str(platform), int(scored),year)
   return cantidad

#cantidad de peliculas con un score superior
@app.get("/get_contents/{rating}")
async def get_contents(rating: float):
   cantidad=contar_peliculas(float(rating))
   return cantidad
