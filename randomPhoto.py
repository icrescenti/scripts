import os
import random
import time
import datetime

_max = 5 
hours = [0,0,0,0,0]
minutes = [0,0,0,0,0]

for i in range(_max):
    randHour = random.randint(8, 16)
    
    #exclude 14:00
    if (randHour == 14):
        randHour += 1

    hours[i] = randHour
    minutes[i] = random.randint(0, 59)

hours.sort()

while True:
    now = datetime.datetime.now()
    for i in range(_max):
        if (hours[i] == now.hour and minutes[i] == now.minute):
            os.system('fswebcam -r 1280x720 --no-timestamp --no-underlay --no-banner ./' + str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "-" + str(now.hour) + "_" + str(now.minute) + '_00.jpg')
    time.sleep(30)
