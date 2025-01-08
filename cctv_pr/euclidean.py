from aiohttp import web
import math


async def calculate_distance(request):
    data = await request.join()
    coordinates = data.get("coordinates", [])

    if len(coordinates) != 2:
        return web.json_response({"error": "Invalid input format"}, status=400)
    
    (x1, y1), (x2, y2) = coordinates
    distance = round(math.sqrt((x2-x1)**2+(y2-y1)**2),2)
    return web.json_response({"distance": distance}, status=200)

def main():
    app = web.Application()
    app.router.add_post("/euclidean", calculate_distance)
    print("Euclidean pokrenut na portu 8091")
    web.run_app(app, port=8091)

if __name__ == "__main__":
    main()