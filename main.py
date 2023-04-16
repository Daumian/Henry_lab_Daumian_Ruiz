from typing import Optional
from pydantic import BaseModel

from fastapi import FastAPI,Body

#creacion de la app
app:FastAPI = FastAPI();

#Modelo
class Person(BaseModel):              
   first_name: str 
   last_name: str
   age: int
   hair_color: Optional[str] = None
   is_married: Optional[bool] = None


#appdef
@app.get("/")
async def home():
    return {"Hola": "Mundo"}

#crearPersona
@app.post("person/new")
def create_person(person: Person = Body(...)):
   return person


@app.get("/get_max_duration")
async def boton1():
    return {"message": "Has presionado el botón 1"}

@app.get("/get_score_count")
async def boton2():
    return {"message": "Has presionado el botón 2"}

@app.get("/get_count_platform")
async def boton2():
    return {"message": "Has presionado el botón 2"}

@app.get("/prod_per_county")
async def boton2():
    return {"message": "Has presionado el botón 2"}

@app.get("/get_contents")
async def boton2():
    return {"message": "Has presionado el botón 2"}


    #get_max_duration(year, platform, duration_type)
#get_score_count(platform, scored, year)
#get_count_platform(platform)
#prod_per_county(tipo,pais,anio)
#get_contents(rating)