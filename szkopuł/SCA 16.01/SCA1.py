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
    if t1[x][9] == t2[x][9]:
        k += 1
print(k)