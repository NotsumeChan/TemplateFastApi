from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from contextlib import asynccontextmanager

from dotenv import dotenv_values as dv
from uvicorn import run
import multiprocessing

import configs


#Coneccion con db
configs.init()


#Inicializar FastAPI
app = FastAPI()


#Controllers
from Controllers.ExampleController import example


#CORS
origins = eval(configs.config["Allowed"]) #esto es un riesgo de seguridad, solo se uso para pruebas, no se recomienda en produccion
#lo ideal es crear un funccion que lea el string, lo separa por comas y lo devuelve como una lista
#allowed = [origin[1:-1] for origin in configs.config["Allowed"].split(",")] algo asi

app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])



#Agregar rutas a FastAPI
app.include_router(example, prefix="/api/Expample", tags=["ExampleController"])


#at run
port : int = 8000

host_normal : str = "0.0.0.0"

#workers : int = 2 if multiprocessing.cpu_count() > 4 else multiprocessing.cpu_count() -2

run(app, host=host_normal, port=port)