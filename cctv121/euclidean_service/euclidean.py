import math
import json
from aiohttp import web 

async def calculate_distance(request):
    try:
        data = await request.json()
        coordinates = data.get("coordinates", [])

        if len(coordinates) != 2:
            return web.json_response({"error": "Invalid input format"}, status=400)
        
        (x1, y1), (x2, y2) = coordinates

        distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
        distance_rounded = round(distance, 2)

        return web.json_response({"distance": distance_rounded}, status=200)
    
    except (KeyError, ValueError, json.JSONDecodeError):
        return web.json_response({"error": "Invalid JSOn format"}, status=400)

def main():
    app = web.Application()
    app.router.add_post("/euclidean", calculate_distance)
    print("Euclidean mikroservis pokrenut na portu 8091")
    web.run_app(app, port=8091)

if __name__ == "__main__":
    main()