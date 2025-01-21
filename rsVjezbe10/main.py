from fastapi import FastAPI
from models import Knjiga, Izdavac

app = FastAPI()

@app.post("/knjige")
def kreiraj_knjigu(knjiga: Knjiga):
    return{"poruka": "Knjiga uspješno dodana", "podaci": knjiga}