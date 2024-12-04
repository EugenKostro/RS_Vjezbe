#1
'''
from aiohttp import web

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

async def proizvodi_handler(request):
    return web.json_response(proizvodi)

async def proizvod_id(request):
    proizvodId = int(request.match_info['id'])
    proizvod = next((p for p in proizvodi if p['id'] == proizvodId), None)

    if proizvod is None:
        return web.json_response({'error'}, status = 404)
    
    return web.json_response(proizvod)

app = web.Application()

app.router.add_get('/proizvodi', proizvodi_handler)
app.router.add_get('/proizvodi/{id}', proizvod_id)

if __name__ == '__main__':
    web.run_app(app, port=8081)
'''

#2

from aiohttp import web
import json

proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

narudzbe = []

async def proizvodi_handler(request):
    return web.json_response(proizvodi)

async def proizvod_id(request):
    proizvodId = int(request.match_info['id'])
    proizvod = next((p for p in proizvodi if p['id'] == proizvodId), None)

    if proizvod is None:
        return web.json_response({'error'}, status = 404)
    
    return web.json_response(proizvod)

async def narudzbe_handler(request):
    try:
        data = await request.json()
        proizvodId = data['proizvodId']
        kolicina = data['kolicina']

        proizvod = next((p for p in proizvodi if p['id'] == proizvodId), None)
        if proizvod is None:
            return web.json_response({'error'}, status = 404)
        
        nova_narudzba = {'proizvodId': proizvodId, 'naziv': proizvod['naziv'], 'kolicina': kolicina}
        narudzbe.append(nova_narudzba)

        return web.json_response(narudzbe, status=201)
    except (KeyError, ValueError) as e:
        return web.json_response({'error'}, status = 400)
    
app = web.Application()

app.router.add_get('/proizvodi', proizvodi_handler)
app.router.add_get('/proizvodi/{id}', proizvod_id)
app.router.add_post('/narudzbe', narudzbe_handler)

if __name__ == '__main__':
    web.run_app(app, port=8081)