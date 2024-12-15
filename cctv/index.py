from cctv import CCTV_frame
import random
import asyncio

kamera = CCTV_frame(frame_id = 1, location_x = 10, location_y = 20, frame_rate = 30, camera_status = "active", zoom_level= "1x", ip_adress = "192.1.1.1")

print(kamera.info())


async def main():
    print("Pokretanje simulacije...")

    test_positions = await simulate_movement(2, kamera.frame_rate)
    print("Rezultat: ")
    print(test_positions)

    durations = [1,2,3,4,5]
    list = await asyncio.gather(*[simulate_movement(duration, kamera.frame_rate) for duration in durations])

    positions = [i for sublist in list for i in sublist]
    print(f"Broj pozicija: {len(positions)}")

    positions50 = positions[:50]
    await asyncio.gather(*[update_camera_location(kamera, x, y) for x,y in positions50])

async def simulate_movement(seconds, frame_rate):
    total_frames = frame_rate * seconds
    positions = []

    for _ in range(total_frames):
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        positions.append((x,y))
        await asyncio.sleep(1/frame_rate)
    
    return positions

async def update_camera_location(instance, x, y):
    instance.update_location(x,y)
    instance.info()

if __name__ == "__main__":
    asyncio.run(main())