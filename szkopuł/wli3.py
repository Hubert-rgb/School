def jakieLitery(t):
    dic = {}
    for x in t:
       dic[x] = 1
    return dic
k = 0
t = []
powt = 5000
for j in range (powt):
    inp = input().rstrip()
    jakie = jakieLitery(inp)
    #print(jakie)
    t.append(jakie)
#print(sorted(t))
for i in range(powt):
    for j in range(i + 1, powt):
        if t[i] == t[j]:
            ##print(t[i].keys(), t[j].keys())
            k+=1

print(k)