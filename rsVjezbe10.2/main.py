from fastapi import FastAPI
from models import RestaurantOrder

app = FastAPI()

@app.post("/narudzbe")
def kreiraj_narudzbu(narudzba: RestaurantOrder):
    return{"poruka": "Narudžba uspješno kreirana", "podaci": narudzba}