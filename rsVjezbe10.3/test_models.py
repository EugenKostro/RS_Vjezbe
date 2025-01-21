from models import CCTVFrame
from datetime import datetime

frame1 = CCTVFrame(
    id = 1,
    vrijeme_snimanja = datetime.now(),
    koordinate = (45.1321, 23.2948)
)

frame2 = CCTVFrame(
    id = 2,
    vrijeme_snimanja = datetime.now()
)

print(frame1)
print(frame2)