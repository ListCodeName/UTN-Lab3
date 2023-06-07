from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Hola Mundo"}

@app.get("/valor/{var}")
def valor(var: int):
    return {"valor": var}

@app.get("/sum")
def sumar(sum1: int, sum2: int):
    return {"sum": sum1+sum2}

@app.get("/sumo")
def sumar(sum1: Union[int, None]=0, sum2: Union[int,None]=0):
    return {"sum": sum1+sum2}

class Item(BaseModel):
    nombre: str
    descripcion: Union[str, None] = None
    fecha: Union[str, None] = None

@app.post("/items/")
async def create_item(item: Item):
    return item