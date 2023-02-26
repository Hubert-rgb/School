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
longest = ""
longestLen = 0
for i in range(1000):
    a = input().rstrip()
    dic = jakieLitery(a)
    if len(dic) > longestLen:
        longestLen = len(dic)
        longest = a
print(longest, end=" ")
print(longestLen)