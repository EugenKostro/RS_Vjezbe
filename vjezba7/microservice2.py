import aiohttp
import asyncio

from aiohttp import web
async def handle_service2(request):
    return web.json_response({"message": "Pozdrav nakon 4 sekunde"})

app = web.Application()
app.router.add_get('/', handle_service2)

if __name__ == "__main__":
    web.run_app(app, port=8082)