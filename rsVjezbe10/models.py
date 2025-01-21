from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Izdavac(BaseModel):
    naziv: str
    adresa: str

class Knjiga(BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    godina_izdavanja: int = Field(default_factory=lambda: datetime.now().year)
    broj_stranica: int
    izdavac: Izdavac