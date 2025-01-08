import json
import uuid
from aiohttp import web

class CCTV_frame:
    def __init__(self, location_x, location_y, frame_rate, camera_status, zoom_level, ip_address):
        self.frame_id = str(uuid.uuid4())
        self.location_x = location_x
        self.location_y = location_y
        self.frame_rate = frame_rate
        self.camera_status = camera_status
        self.zoom_level = zoom_level
        self.ip_address = ip_address
    
    def info(self):
        return (f"Frame ID: {self.frame_id}, Location: ({self.location_x}, {self.location_y}), Frame rate: {self.frame_rate}, Camera_status: {self.camera_status}, Zoom level: {self.zoom_level}, IP address: {self.ip_address}")


    def update_location(self, x, y):
        self.location_x = x
        self.location_y = y

cctv_instances = []

async def create_cctv(request):
    try:
        data = await request.json()
        cctv_details = data.get("cctv_details", {})

        new_cctv = CCTV_frame(
            location_x = cctv_details["location_x"],
            location_y = cctv_details["location_y"],
            frame_rate = cctv_details["frame_rate"],
            camera_status = cctv_details["camera_status"],
            zoom_level = cctv_details["zoom_level"],
            ip_address = cctv_details["ip_address"]
        )

        cctv_instances.append(new_cctv)

        response_message = {"message": new_cctv.info()}
        return web.json_response(response_message, status=201)
    
    except KeyError as e:
        error_message = {"error": f"Missing key: {e}"}
        return web.json_response(error_message, status=400)
    except json.JSONDecodeError:
        return web.json_response({"error": "Invalid JSON format"}, status=400)

def main():
    app = web.Application()
    app.router.add_post("/cctv", create_cctv)
    print("Pokrećem CCTV na portu 8090")
    web.run_app(app, port=8090)

if __name__ == "__main__":
    main()