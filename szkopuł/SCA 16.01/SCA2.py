t1 = []
t2 = []

for x in range(1000):
    a = input().rstrip().split(" ")
    t1.append(a)
for x in range(1000):
    a = input().rstrip().split(" ")
    t2.append(a)

k = 0
for x in range(1000):
    par1 = 0
    npar1 = 0

    par2 = 0
    npar2 = 0
    for y in range(10):
        if int(t1[x][y]) % 2 == 0:
            par1 += 1
        else:
            npar1 += 1
        if int(t2[x][y]) % 2 == 0:
            par2 += 1
        else:
            npar2 += 1
    if par1 == par2 == 5:
        k += 1
print(k)