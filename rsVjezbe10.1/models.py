from pydantic import BaseModel
from typing import List, Literal

class Admin(BaseModel):
    ime: str
    prezime: str
    korisnicko_ime: str
    email: str
    ovlasti: List[Literal["dodavanje", "brisanje", "ažuriranje", "čitanje"]] = []