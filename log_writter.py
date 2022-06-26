#Example
#[11:57:45] JOE: Has approached sector 1
from datetime import datetime

execute = True
while(execute):
    txt = input("> ")

    if (txt.upper() == "END"):
        execute = False
    else:
        with open(datetime.now().strftime("%Y_%m_%d") + '.log', 'a') as f:
            f.write(datetime.now().strftime("[%H:%M:%S]") + " " + txt.upper() + "\n")
    
