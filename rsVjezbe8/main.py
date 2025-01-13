from fastapi import FastAPI

from models import CreateFilm, Film

app = FastAPI()

filmovi = [
    {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
    {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
    {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
    {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

@app.get("/filmovi/{film_id}")
def get_filmovi(film_id: int):
    trazeni_film = next((film for film in filmovi if film["id"] == film_id), None)

    return {"film_id": trazeni_film}

@app.post("/filmovi")
def dodaj_film(film: CreateFilm):
    new_id = len(filmovi) + 1
    film_sa_id = {"id": new_id, **film.dict()}
    filmovi.append(film_sa_id)
    return film_sa_id

