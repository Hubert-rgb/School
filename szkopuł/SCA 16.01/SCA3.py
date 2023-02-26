t1 = []
t2 = []
to = []

for x in range(1000):
    a = input().rstrip().split(" ")
    t1.append(a)
for x in range(1000):
    a = input().rstrip().split(" ")
    t2.append(a)

k = 0
for x in range(1000):
    dic1 = {}
    dic2 = {}

    for y in range(10):
        try:
            dic1[t1[x][y]] += 1
        except:
            dic1[t1[x][y]] = 1
    for y in range(10):
        try:
            dic2[t2[x][y]] += 1
        except:
            dic2[t2[x][y]] = 1
    kc = 0
    for y in range(10):
        try:
            a = dic1[t2[x][y]]
        except:
            kc+=1
    if kc == 0:
        k += 1
        to.append(x + 1)
print(k)
for x in to:
    print(x)