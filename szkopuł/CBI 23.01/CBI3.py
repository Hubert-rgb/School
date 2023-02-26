ile = input().rstrip()
ile = int(ile)

max = 0
maxBin = ""
for i in range(ile):
    x = input().rstrip()
    l = int(x, 2)
    if l <= 65535:
        if l > max:
            max = l
            maxBin = x
print(maxBin)
print(max)