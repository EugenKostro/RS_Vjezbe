from fastapi import FastAPI, HTTPException, Query
from models import Automobil

app = FastAPI()

automobili = [
    Automobil(automobil_id=1, marka="BMW", model="M3", godina_proizvodnje=2010, cijena=13000, boja="Plava"),
    Automobil(automobil_id=2, marka="RAM", model="1500", godina_proizvodnje=2020, cijena=10000, boja="Crvena"),
    Automobil(automobil_id=3, marka="Mercedes", model="Eclass", godina_proizvodnje=2000, cijena=9000, boja="Bijela"),
]

@app.get("/automobili")
def filtriraj_automobile(
    min_cijena: float = Query(default=0, ge=0, description="Minimalna cijena mora biti veća od 0"),
    max_cijena: float = Query(default=float("inf"), description="Maksimalna cijena automobila"),
    min_godina: int = Query(default=1960, ge=1960, description="Minimalna godina mora biti veća od 1960"),
    max_godina: int = Query(default=9999, description="Maksimalna godina proizvodnje")
):
    if min_cijena > max_cijena:
        raise HTTPException(status_code=404, detail="Minimalna cijena ne smije biti veća od maksimalne cijene")
    
    if min_godina > max_godina:
        raise HTTPException(status_code=404, detail="Minimalna cijena ne smije biti veća od maksimalne")
    
    filtrirani_automobili = [automobil for automobil in automobili if min_cijena <= automobil.cijena <= max_cijena and min_godina <= automobil.godina_proizvodnje <= max_godina]

    if not filtrirani_automobili:
        raise HTTPException(status_code=404, detail="Nijedan automobil nije pronađen")
    
    return filtrirani_automobili


@app.get("/automobili/{automobili_id}")
def dohvati_automobil(automobil_id: int):
    for automobil in automobili:
        if automobil.automobil_id == automobil_id:
            return automobil
    raise HTTPException(status_code=404, detail="Automobil nije pronađen")