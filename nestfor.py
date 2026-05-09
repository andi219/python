a = int(input())
for i in range(a + 1):
    for j in range(i):
        print(" ", end="")
    for k in range(a):
        print("*", end="")
    print("")


for i in range(a + 1):
    for k in range(i):
        print("*", end="")
    print("")

for i in range(a + 1):
    for j in range(i):
        print(" ", end="")
    for k in range(i):
        print("*", end="")
    print("")


for i in range(a + 1):
    for j in range(a-i):
        print(" ", end="")
    for k in range(i*2-1):
        print("*", end="")
    print("")
