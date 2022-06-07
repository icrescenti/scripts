import os
import platform
import datetime

osName = platform.system()

f = open('execution.log', 'w')
f.write("")
f.close()
f = open('execution.log', 'a')

scripts = [input("First script/program -> "), input("Second script/program -> ")]

bestTimes = []
for script in scripts:
    times = []

    print("-------------------" + script + "-------------------" )
    for _ in range(50):
        begin_time = datetime.datetime.now()

        if (osName == "Linux"):
            os.system(script + " | tee /proc/sys/vm/drop_caches >/dev/null 2>&1")
        elif (osName == "Windows"):
            pass
        
        print(script + " (" + str(_) + "/50): " + str(datetime.datetime.now() - begin_time))
        times.append(datetime.datetime.now() - begin_time)
    
    times.sort()
    bestTimes.append(times[0])
    f.write(script + ": " + str(times[0]) + "\n")

print("--------------------------------------" )
for _, script, in enumerate(scripts):
    print("[BEST RESULT] " + script + ": " + str(bestTimes[_]))

f.close()