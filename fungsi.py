

def volume (r,t):
    v = (r*2)*t*3.14
    k = 2*3.14*r*t
    print("total volume ",v)
    print("total luas", k)
def volumed (r,t):
    v = r*t*3.14
    k = 2*3.14*r*t
    print("total volume ",v)
    print("total luas", k)

def vlimas(l,t):
    p = 1/3*l*t
    print("total volume limas", p)
   

print("input jari jari dan tinggi volume tabung")
i = int(input())
p = int(input())
volume(i,p)
print("input diamater dan tinggi volume tabung")
i = int(input())
p = int(input())
volumed(i,p)

print("volume limas masukan luas dan tinggi")
k = int(input())
o= int(input())
vlimas(k,o)