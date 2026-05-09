

while True:
    print("input x untuk menutup")
    print("input kode pelanggan")
    p = input()
    print("input jumlah pemakaian air")
    j = int(input())
    if p =="f" or p == "F":
        if j <=50:
            g = j*1000
            print("jumlah pembayaran ", g )
        elif j >=50 and j <=100:
            g = j*1500
            print("jumlah pembayaran ", g)
        elif j >=100:
            g = j *2500
            print("jumlah pembayaran ", g)
    elif p =="r" or p == "R":
        if j <=50:
            g = j*4000
            print("jumlah pembayaran ", g )
        elif j >=50 and j <=100:
            g = j*7000
            print("jumlah pembayaran ", g)
        elif j >=100:
            g = j *10000
            print("jumlah pembayaran ", g)
    elif p == "n" or p == "N":
        if j <=50:
            g = j*7500
            print("jumlah pembayaran ", g )
        elif j >=50 and j <=100:
            g = j*10000
            print("jumlah pembayaran ", g)
        elif j >=100:
            g = j *13500
            print("jumlah pembayaran ", g)
    elif p == "x" or j =="x":
        break
    else:
        print("gagal menerima informasi")