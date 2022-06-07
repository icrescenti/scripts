task = input("code: ")

print("-----------")
if (task[0:2] == "if"):
    task = task.replace("if ", "").split(' ')
    condition = ""

    for _ in range(int(len(task)/3)):
        cond = task[1+(_*3)]
        c2 = task[2+(_*3)]

        cond = cond.replace("ne", "!=").replace("e", "==").replace("h", ">").replace("l", "<")

        if(c2 == "n"):
            c2 = "null"
        elif(c2 == "u"):
            c2 = "undefined"
        
        if(_ > 0):
            condition += " and "
        
        condition += task[0+(_*3)] + " " + cond + " " + c2

    print(f"""
        if ({condition}) {{
            
        }}
    """)

elif (task[0:2] == "log"):
    task = task.split(' ')

    if (len(task) > 0):
        tag = task[1]

    print(f"""
        console.log("{tag}", value)
    """)

else:
    print("var " + task + " = null")