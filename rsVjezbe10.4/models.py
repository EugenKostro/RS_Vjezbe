from pydantic import BaseModel

class Automobil(BaseModel):
    automobil_id: int
    marka: str
    model: str
    godina_proizvodnje: int
    cijena: float
    boja: str