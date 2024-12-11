import asyncio
from aiohttp import web

async def pozdrav1(request):
    await asyncio.sleep(3)
    return web.json_response({"message": "Pozdrav nakon 3 sekunde"})

app = web.Application()

app.router.add_get('/pozdrav', pozdrav1)

if __name__ == '__main__':
    web.run_app(app, port=8081)