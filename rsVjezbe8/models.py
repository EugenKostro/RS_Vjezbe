from pydantic import BaseModel

class CreateFilm(BaseModel):
    naziv: str
    ganre: str
    godina: int

class Film(CreateFilm):
    id: int