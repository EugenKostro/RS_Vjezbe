import asyncio
import random
from cctv import CCTV_frame

'''
kamera = CCTV_frame(location_x=10, location_y=20, frame_rate=30, camera_status="Active", zoom_level="1x", ip_address="192.168.1.10")

print(kamera.info())
'''

async def simulate_movement(seconds, frame_rate):
    total_frames = seconds*frame_rate
    positions = []

    for _ in range(total_frames):
        x = random.uniform(-100, 100)
        y = random.uniform(-100, 100)
        positions.append((x,y))
        await asyncio.sleep(1/frame_rate)
    return positions

async def main():
    frame_rate=30

    print("Simulacija za 1 sekundu...")
    positions = await simulate_movement(1, frame_rate)
    print(f"Generirano {len(positions)}, pozicija: {positions}")

    durations = [1, 2, 3 ,4 , 5]
    tasks = [simulate_movement(seconds, frame_rate) for seconds in durations]
    all_positions = await asyncio.gather(*tasks)

    total_positions = sum(len(pos) for pos in all_positions)
    print(f"Ukupan broj generiranih pozicija: {total_positions}")

if __name__ == "__main__":
    asyncio.run(main())