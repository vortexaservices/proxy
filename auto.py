from time import sleep
import os
id = 0
while True:
    file = open("proxy.txt", "r")
    file = file.readlines()
    id += 1
    for line in file:
        os.system(line)
        if line == "":
            file.close()
    sleep(10)
    print(f"Successfully screened! ID: {id}")