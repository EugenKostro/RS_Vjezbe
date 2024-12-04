###MIKROSERVISNA ARHITEKTURA
import aiohttp
import asyncio
from aiohttp import web
'''
async def fetch_fact(session):
    print("Šaljem zahtjev...")
    rezultat = await session.get("https://catfact.ninja/fact")
    return(await rezultat.json())["fact"]

async def main():
    async with aiohttp.ClientSession() as session:
        cat_task = [asyncio.create_task]
        print(response.status)
asyncio.run(main())
'''
'''
app = web.Application()

def handler_function(request):
    
    
    data = {"ime": "Ivo", "prezime": "Ivić"}
    return web.json_response(data)

async def post_handler(request):
    data = await request.json()
    print(data)
    return web.json_response(data)
    

app.router.add_get("/", handler_function)
app.router.add_post("/", post_handler)

web.run_app(app, host='localhost', port=8080)
'''

#ZADACI
###Definirajte aiohttp poslužitelj koji radi na portu 8081 koji na putanji /proizvodi vraća listu proizvoda u
#JSON formatu. Svaki proizvod je rječnik koji sadrži ključeve naziv , cijena i količina . Pošaljite zahtjev na
#adresu http://localhost:8080/proizvodi koristeći neki od HTTP klijenata ili curl i provjerite odgovor.

'''
app = web.Application()

proizvodi = [
        {"naziv": "Mlijeko", "cijena": 3, "količina": "2L"},
        {"naziv:": "Sir", "cijena": 4, "količina": "2kg"}
    ]

def handler_function(request):
    return web.json_response(proizvodi)


app.router.add_get("/proizvodi", handler_function)


web.run_app(app, host='localhost', port=8081)
'''

