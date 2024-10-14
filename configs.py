from sqlmodel import Session, create_engine, SQLModel
from dotenv import dotenv_values as dv

from sqlalchemy.exc import OperationalError as sqlOperationalError
from pyodbc import OperationalError as pyOperationalError

context = None
config = None
def init():
    global context
    global config
    config = dv(".env")

    #conectar con la base de datos
    motor = None
    try:
        motor = create_engine(f"mssql+pyodbc://{config["User"]}:{config["Password"]}@{config["Server"]}/{config["Database"]}?driver=ODBC+Driver+17+for+SQL+Server", echo=True)
    except Exception as e:
        print("Error al conectar con la base de datos")
        if isinstance(e, KeyError):
            print("Verifique que exista el archivo .env y que sus keys sean correctas")
        elif isinstance(e, sqlOperationalError) or isinstance(e, pyOperationalError): 
            print("Verifique que los datos de conexion en el archivo .env sean correctos")
        return
    #crear la metaata de la base de datos
    SQLModel.metadata.create_all(motor)

    #crear el contexto de la base de datos
  
    context = Session(motor)
    return context