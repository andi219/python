import random
import os
from inputimeout import inputimeout,TimeoutOccurred

with open("words.txt", "r") as f:
    kata = f.read().splitlines()

def bersih():
    os.system('cls')

nyawa = 5
point = 0 
while nyawa >0:
    try:
        print("nyawa : ",nyawa,"--------")
        print("-------------------")
        print("--------",point,"--------")
        print("-------------------")
        target = random.choice(kata)
        print(": ",target)
        h = inputimeout(":", timeout=10)
        if h == "x":
           break
        if h == target:
          point +=1
        else: 
           nyawa -= 1
        bersih()
    except TimeoutOccurred:
        print("waktu habis")
        nyawa -=1
        bersih()
    bersih()

print("Game Over ", "Total point :", point)