import random
print("batu = 1 gunting = 2 kertas = 3")
print("masukan input batu gunting kertas")
print("masukan nilai 0 untuk break")
while True:
    komputer = random.randint(1, 3)
    nilai = int(input())
    if nilai==1 and komputer==1:
        print("seri")
    elif nilai==1 and komputer==2:
        print("player menang")
    elif nilai==1 and komputer==3:
        print("komputer menang")
    elif nilai==0:
        break
    elif nilai==2 and komputer==2:
        print("seri")
    elif nilai==2 and komputer==1:
        print("komputer menang")
    elif nilai==2 and komputer== 3:
        print("player menang ")
    elif nilai==3 and komputer==3:
        print("seri ")
    elif nilai==3 and komputer==1:
        print("player menang")
    elif nilai==3 and komputer==2:
        print("komputer menang")
    else:
        print("nilai salah")