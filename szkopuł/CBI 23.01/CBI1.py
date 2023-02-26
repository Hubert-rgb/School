ile = input().rstrip()
ile = int(ile)

k = 0
max = ''
maxLen = 0
for i in range(ile):
    x = input().rstrip()
    l = int(len(x) / 2)
    if x[:l] == x[l:]:
        k += 1
        if len(x) > maxLen:
            maxLen = len(x)
            max = x
print(k)
print(max)
print(maxLen)