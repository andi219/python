import time
with open("lirik.txt","r") as f:
    txt = f.read().splitlines()

j = 0
for i in txt:
    k = txt[j]
    for x in range(len(txt[j])):
        print(k[x],end="",flush=True)
        time.sleep(0.1)
    j +=1
    print("")
    
#time sleep itu buat men delay kecepatan loop (1) itu satu loopp perdetik
