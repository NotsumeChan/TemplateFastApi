import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__name__))))
from sqlmodel import select
from fastapi import APIRouter

from configs import context

from Models.ExampleModel import Example

example = APIRouter()


@example.get("/ExampleRoute")
async def example():
    with context as ctx:
        statement = select(Example)
        data = list(ctx.exec(statement).all()) #aca podemos transformalo en una lista, aunque ya lo retorna como un iterable
    return data