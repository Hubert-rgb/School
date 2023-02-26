ile = input().rstrip()
ile = int(ile)

k = 0
min = ''
minLen = 45
for i in range(ile):
    x = input().rstrip()
    l = int(len(x) / 4)
    kc = 0
    for y in range(l):
        licz = x[y*4:y*4+4]
        if int(licz, 2) > 9:
            kc += 1
    if kc != 0:
        k += 1
        if len(x) < minLen:
            minLen = len(x)
            min = x
print(k)
print(minLen)