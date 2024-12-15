from aiohttp import web
import json

class CCTV_frame:
    def __init__(self, frame_id, location_x, location_y, frame_rate, camera_status, zoom_level, ip_adress):
        self.frame_id = frame_id
        self.location_x = location_x
        self.location_y = location_y
        self.frame_rate = frame_rate
        self.camera_status = camera_status
        self.zoom_level = zoom_level
        self.ip_adress = ip_adress
    
    def info(self):
        print(f"Informacije o kameri, frame_id: {self.frame_id}, location_x: {self.location_x}, location_y: {self.location_y}, frame_rate: {self.frame_rate}, camera_status: {self.camera_status}, zoom_level: {self.zoom_level}, ip_adress: {self.ip_adress}")
    
    def update_location(self, x, y):
        self.location_x = x
        self.location_y = y

cctv_instances = []

async def create_cctv(request):
    try:
        data = await request.json()
        cctv_details = data.get("cctv_details", {})
        required_keys = ["frame_id", "location_x", "location_y", "frame_rate", "camera_status", "zoom_level", "ip_adress"]
        if not all(key in cctv_details for key in required_keys):
            return web.json_response({"error: "}, status=400)
        
        new_cctv = CCTV_frame(
            frame_id = cctv_details["frame_id"],
            frame_id = cctv_details["location_x"],
            frame_id = cctv_details["location_y"],
            frame_id = cctv_details["frame_rate"],
            frame_id = cctv_details["camera_status"],
            frame_id = cctv_details["zoom_level"],
            frame_id = cctv_details["ip_adress"]
        )

        cctv_instances.append(new_cctv)

        return web.json_response({"message": new_cctv.info()}, status=201)

    except json.JSONDecodeError:
        return web.json_response({"error: "}, status=400)
    except Exception as e:
        return web.json_response({"error": str(e)}, status=500)

app = web.Application()
app.router.add_post('/cctv', create_cctv)

if __name__ == "__main__":
    web.run_app(app, port=8090)