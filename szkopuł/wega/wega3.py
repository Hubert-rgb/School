def odlegloscWAlfabecie(a, b):
    alfabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    aId = -1
    bId = -1
    for i in range(len(alfabet)):
        if alfabet[i] == a:
            aId = i
        if alfabet[i] == b:
            bId = i
    return abs(aId - bId)
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

t = []
for i in range(1000):
    a = input().rstrip()
    k = 0
    dic = jakieLitery(a)
    sortedDic = sorted(dic)
    c = 0
    for i in range(len(sortedDic) - 1):
        c += odlegloscWAlfabecie(sortedDic[i], sortedDic[i + 1])
    if c <= 10:
        t.append(a)
for x in t:
    print(x)