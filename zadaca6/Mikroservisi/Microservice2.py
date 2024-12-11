import asyncio
from aiohttp import web

async def pozdrav2(request):
    await asyncio.sleep(4)  
    return web.json_response({"message": "Pozdrav nakon 4 sekunde"})

app = web.Application()

app.router.add_get('/pozdrav', pozdrav2)

if __name__ == '__main__':
    web.run_app(app, port=8082)