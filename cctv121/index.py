import asyncio
import aiohttp
import random
from cctv import CCTV_frame
'''
kamera1 = CCTV_frame(
    frame_id = 1,
    location_x = 10,
    location_y = 20,
    frame_rate = 30,
    camera_status = 'Active',
    zoom_level = 1,
    ip_address = "192.168.1.10"
)

kamera1.info()
'''

async def simulate_movement(seconds, frame_rate):
    total_frames = frame_rate * seconds
    positions = []

    for _ in range(total_frames):
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        positions.append((x, y))
        await asyncio.sleep(1 / frame_rate)
    
    return positions

async def send_request(session, url, x, y):
    payload = {
        "cctv_details": {
            "location_x": x,
            "location_y": y,
            "frame_rate": 30,
            "camera_status": "Active",
            "zoom_level": "1x",
            "ip_address": "192.168.5.11"
        }
    }

    async with session.post(url, json=payload) as response:
        result = await response.json()
        print(result)

async def update_camera_location(instance, x, y):
    instance.update_location(x, y)
    instance.info()

async def send_distance_request(session, url, pos1, pos2):
    payload = {"coordinates": [pos1, pos2]}

    async with session.post(url, json=payload) as response:
        if response.status == 200:
            result = await response.json()
            print(f"Udaljenost između {pos1} i {pos2}: {result['distance']}")
        else:
            print(f"Greška: {response.status}, {await response.text()}")

async def main():
    '''
    frame_rate = 30

    print("Testiranje korutine simulate_movement za 1 sekundu: ")
    test_result = await simulate_movement(1, frame_rate)
    print(f"Generirano {len(test_result)} pozicija za 1 sekundu.\n")

    print("Konkurentno pokretanje simulacije za 1, 2, 3, 4, 5 sekundi...")
    durations = [1, 2, 3, 4 ,5]
    tasks = [simulate_movement(seconds, frame_rate) for seconds in durations]
    positions = await asyncio.gather(*tasks)

    total_positions = sum(len(position) for position in positions)
    print(f"Ukupan broj generiranih pozicija: {total_positions}")
    print(f"Očekivani broj pozicija: 450")
    '''
    cctv = CCTV_frame(0, 0, 30, "Active", 1, "192.168.1.10")

    frame_rate = 30
    durations = [1, 2, 3, 4, 5]
    tasks = [simulate_movement(seconds, frame_rate) for seconds in durations]
    results = await asyncio.gather(*tasks)

    positions = [pos for sublist in results for pos in sublist]
    print(f"Ukupno generiranih pozicija: {len(positions)}")

    first_50_positions = positions[:50]

    euclidean_url = "http://localhost:8091/euclidean"
    async with aiohttp.ClientSession() as session:
        tasks = [send_distance_request(session, euclidean_url, first_50_positions[i], first_50_positions[i+1]) for i in range(0, len(first_50_positions)-1)]
        await asyncio.gather(*tasks)
        
if __name__ == "__main__":
    asyncio.run(main())