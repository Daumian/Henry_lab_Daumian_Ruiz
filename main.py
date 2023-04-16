from typing import Dict
from fastapi import FastAPI;

#  Instancia de la clase.
mi_app:FastAPI = FastAPI();

#  Path Operator Decoration.
@mi_app.get("/")
def home() -> Dict:
   #  Return JSON.
   return {"Hello": "World"};