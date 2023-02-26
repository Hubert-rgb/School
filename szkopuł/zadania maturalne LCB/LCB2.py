def jakieLitery(t):
    dic = [t[0]]
    for x in t:
        k = 0
        for y in dic:
            if x == y:
                k += 1
        if k == 0:
            dic.append(x)
    return dic

maxLen = 0
maxLenNum = 0
maxDifLen = 0
maxDifNum = 0
for i in range(200):
    a = input().rstrip()
    a = int(a)
    b = a
    t = []
    d = 2
    while a > 1:
        if a % d == 0:
            t.append(d)
            a//=d
        else:
            d += 1
    if len(t) > maxLen:
        maxLen = len(t)
        maxLenNum = b
    elif len(t) == maxLen and b < maxLenNum:
        maxLen = len(t)
        maxLenNum = b
    arr = jakieLitery(t)
    if len(arr) > maxDifLen:
        maxDifLen = len(arr)
        maxDifNum = b
    elif len(arr) == maxDifLen and b < maxDifNum:
        maxDifLen = len(arr)
        maxDifNum = b
    #print(t, arr)
print(maxLenNum, maxLen)
print(maxDifNum, maxDifLen)