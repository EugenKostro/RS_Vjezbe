from pydantic import BaseModel
from typing import List, TypedDict

class StolInfo(BaseModel):
    broj: int
    lokacija: str

class Dish(BaseModel):
    id: int
    naziv: str
    cijena: float

class RestaurantOrder(BaseModel):
    id: int
    ime_kupca: str
    stol_info: StolInfo
    jela: List[Dish]
    ukupna_cijena: float