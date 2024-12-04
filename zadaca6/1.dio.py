#1

from aiohttp import web
import json
'''
proizvodi = [
    {"naziv": "Mlijeko", "cijena": 2, "kolicina": 10},
    {"naziv": "Jaja", "cijena": 3, "kolicina": 20},
]

async def proizvodi_handler(request):
    return web.json_response(proizvodi)

app = web.Application()
app.router.add_get('/proizvodi', proizvodi_handler)

if __name__ == '__main__':
    web.run_app(app, port=8081)
'''

#2
'''
proizvodi = [
    {"naziv": "Mlijeko", "cijena": 2, "kolicina": 10},
    {"naziv": "Jaja", "cijena": 3, "kolicina": 20},
]

async def proizvodi_handler(request):
    return web.json_response(proizvodi)

async def dodaj_proizvod_handler(request):
    try:
        novi_proizvod = await request.json()
        print("Primljeni podaci o proizvodu...")
        proizvodi.append(novi_proizvod)
        return web.json_response(proizvodi, status = 201)
    except Exception as e:
        return web.json_response({"error": str(e)}, status = 400)

app = web.Application()

app.router.add_get('/proizvodi', proizvodi_handler)
app.router.add_post('/proizvodi', dodaj_proizvod_handler)

if __name__ == '__main__':
    web.run_app(app, port=8081)
'''

#3
'''
korisnici = [
    {'ime': 'Ivo', 'godine': 25},
    {'ime': 'Ana', 'godine': 17},
    {'ime': 'Marko', 'godine': 19},
    {'ime': 'Maja', 'godine': 16},
    {'ime': 'Iva', 'godine': 22}
]

async def punoljetni(request):
    punoljetni_korisnici = [korisnik for korisnik in korisnici if korisnik['godine'] > 18]
    return web.json_response(punoljetni_korisnici)

app = web.Application()

app.router.add_get('/punoljetni', punoljetni)

if __name__ == '__main__':
    web.run_app(app, port=8082)
'''