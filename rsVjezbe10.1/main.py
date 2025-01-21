from fastapi import FastAPI
from models import Admin

app = FastAPI()

@app.post("/admini")
def kreiraj_admina(admin: Admin):
    return{"poruka": "Admin uspješno kreiran", "podaci": admin}