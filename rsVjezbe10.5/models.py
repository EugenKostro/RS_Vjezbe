from pydantic import BaseModel, Field

class BaseCar(BaseModel):
    marka: str
    model: str
    godina_proizvodnje: int
    boja: str

class NewCar(BaseCar):
    cijena: float

class CarWithIDAndPDV(BaseCar):
    automobil_id: int
    cijena: float
    cijena_pdv: float = Field(default=0.0, description="Cijena s uključenim PDV-om")