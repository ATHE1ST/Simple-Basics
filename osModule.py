import os

liste = os.listdir()

for i in liste:
    if i.endswith(".py"):
        print(i)
        print("********************************************************************************")
    else:
        pass