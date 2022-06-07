# FILL WITH ZERO ALL REMAINING FREE SPACE ON DISK
from datetime import datetime

today = datetime.now()
f = open(today.strftime("%d%m%Y%H%M%S"), "wb")

try:
    while(True):
        f.write(int(0).to_bytes(1, 'big'))
finally: 
    f.close()
    print("Done")