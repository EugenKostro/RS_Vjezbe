from fastapi import FastAPI, HTTPException
from models import BaseCar, NewCar, CarWithIDAndPDV

app = FastAPI()

automobili = []

def generiraj_id():
    return len(automobili)+1

def izracunaj_pdv(cijena: float, pdv_stopa: float = 0.25):
    return cijena*pdv_stopa

@app.post("/automobili")
def dodaj_automobil(novi_automobil: NewCar):
    for automobil in automobili:
        if automobil.marka == novi_automobil.marka and automobil.model == novi_automobil.model:
            raise HTTPException(status_code=400, detail="Automobil već postoji")
    
    automobil_id = generiraj_id()
    cijena_pdv = izracunaj_pdv(novi_automobil.cijena)

    novi_automobil_pdv = CarWithIDAndPDV(
        automobil_id = automobil_id,
        marka = novi_automobil.marka,
        model = novi_automobil.model,
        godina_proizvodnje = novi_automobil.godina_proizvodnje,
        boja = novi_automobil.boja,
        cijena = novi_automobil.cijena,
        cijena_pdv = cijena_pdv
    )

    automobili.append(novi_automobil_pdv)
    return {"poruka": "Automobil uspješno dodan", "podaci": novi_automobil_pdv}