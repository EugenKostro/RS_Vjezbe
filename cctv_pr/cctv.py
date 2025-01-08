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
        return f"Frame ID: {self.frame_id}, Location: ({self.location_x}, {self.location_y}), Frame Rate: {self.frame_rate}, Camera Status: {self.camera_status}, Zoom Level: {self.zoom_level}, IP address: {self.ip_address}"
    
async def create_cctv(request):
    data = await request.json()
    details = data.get("cctv_details")
    cctv = CCTV_frame(*+details)
    return web.json_response({"message": cctv.info()}, status=201)

def main():
    app = web.Application()
    app.router.add_post("/cctv", create_cctv)
    print("CCTV pokrenut na portu 8090...")
    web.run_app(app, port=8090)

if __name__ == "__main__":
    main()