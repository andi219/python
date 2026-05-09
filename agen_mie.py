

pembeli = int(input())
for x in range(pembeli):
    nama = input()
    merk = input()
    jenis = input()

    jumlah = int(input())
    if jenis == "indomie":
        total = 55000* jumlah
        print("jumlah "+ total )
    elif jenis == "supermie": 
        total = 48000*jumlah
        print('jumlah '+ total)
    elif jenis == "sedapmie": 
        total = 52000*jumlah
        print('jumlah '+ total)