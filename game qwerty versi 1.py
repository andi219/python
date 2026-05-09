import random
import os
word = ["quit", "banana", "time", "earth", "moon", "mouse", "wall"]

def pembersih():
    os.system('cls')
point  = 0
nyawa = 3
while True:
    print("nyawa : ",nyawa,"--------")
    print("-------------------")
    print("--------",point,"--------")
    print("-------------------")
    nomor = random.randint(0, 6)
    if nyawa ==0:
        break
    print(word[int(nomor)])
    h = input()

    if h == word[int(nomor)]:
        point +=1
    else:
        nyawa -=1
    pembersih()
