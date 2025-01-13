from fastapi import FastAPI

from models import CreateFilm, Film

app = FastAPI()

filmovi = [
    {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
    {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
    {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
    {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

@app.get("/filmovi", response_model=list[Film])
def get_filmovi():
    return filmovi

@app.get("/filmovi/{film_id}", response_model=Film)
def get_film_id(film_id: int):
    for film in filmovi:
        if film["id"] == film_id:
            return film
    return {"id": 0, "naziv": "", "genre": "", "godina": 0}

@app.post("/filmovi", response_model=Film)
def dodaj_film(film: CreateFilm):
    new_id = len(filmovi) + 1
    film_sa_id = {"id": new_id, **film.dict()}
    filmovi.append(film_sa_id)
    return film_sa_id