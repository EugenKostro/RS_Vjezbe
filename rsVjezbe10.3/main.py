from fastapi import FastAPI
from models import CCTVFrame

app = FastAPI()
cctv_frames = []

@app.post("/cctv_frame")
def kreiraj_cctv_frame(frame: CCTVFrame):
    return{"Poruka": "CCTV_Frame uspješno kreiran", "podaci": frame}

@app.get("/cctv_frames")
def dohvati():
    return{"cctv_frames": cctv_frames}