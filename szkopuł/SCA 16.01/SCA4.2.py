t1 = []
t2 = []

for x in range(1000):
    a = input().rstrip().split(" ")
    tc = []
    for y in a:
        tc.append(int(y))
    tc.sort()
    t1.append(tc)
for x in range(1000):
    a = input().rstrip().split(" ")
    tc = []
    for y in a:
        tc.append(int(y))
    tc.sort()
    t2.append(tc)

k = 0
tO = []
for x in range(1000):
    to = []
    for y in t1:
        to.append(y)
    for y in t2:
        to.append(y)
    to.sort()
    tO.append(to)

for x in tO:
    for y in x:
        print(y, end=" ")
    print()
