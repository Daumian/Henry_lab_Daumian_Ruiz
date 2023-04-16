import pandas as pd

from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI,Body,Query


#creacion de la app
app:FastAPI = FastAPI();

amazon_df = pd.read_csv('df_limpios\DF_Amazon.csv')
disney_df = pd.read_csv('df_limpios\DF_Disney.csv')
hulu_df = pd.read_csv('df_limpios\DF_Hulu.csv')
netflix_df = pd.read_csv('df_limpios\DF_Netflix.csv')

def contar_datos(dataframe):
   if dataframe == "1" or dataframe == "amazon":
      return amazon_df.shape[0]
   elif dataframe == "2" or dataframe == "netflix":
      return netflix_df.shape[0]
   elif dataframe == "3" or dataframe == "disney":
      return disney_df.shape[0]
   elif dataframe == "4" or dataframe == "hulu":
      return hulu_df.shape[0]
   else:
      return "error:plataforma incorrecta"


#appdef
@app.get("/")
async def home():
   return {"Hola": "Mundo"}

#Cuantas Peliculas hay en esta plataforma
@app.get("/get_count_platform/{plataforma}")
async def plataforma(plataforma:str):

   cantidad=contar_datos(plataforma)

   return {"la plataforma":{plataforma},
            "tiene un total de peliculas": cantidad}


# @app.get("/get_max_duration")
# def boton1():
#     return {"message": "Has presionado el botón 1"}

# @app.get("/get_score_count")
# def boton2():
#     return {"message": "Has presionado el botón 2"}


#Cuantas Peliculas hay en esta plataforma

# @app.get("/get_count_platform/{plataforma}")

# async def plataforma(plataforma:str):
#    cantidad_peliculas=sin_jupiter.variable3
#    return {"plataforma":cantidad_peliculas}

# @app.get("/prod_per_county")
# def boton2():
#     return {"message": "Has presionado el botón 2"}

# @app.get("/get_contents")
# def boton2():
#     return {"contenido"}


#get_max_duration(year, platform, duration_type)
#get_score_count(platform, scored, year)
#get_count_platform(platform)
#prod_per_county(tipo,pais,anio)
#get_contents(rating)



