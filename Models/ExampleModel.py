from sqlmodel import SQLModel
from sqlmodel import Field
from dataclasses import dataclass

@dataclass
class Example(SQLModel, table=True):
    id: int = Field(primary_key=True, default=None)
    atribute_str : str = None
    atribute_int : int = None
    atribute_float : float = None
    atribute_nullable : str | None = None