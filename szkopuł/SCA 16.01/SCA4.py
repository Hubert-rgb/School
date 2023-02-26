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
    tc1 = t1[x]
    tc2 = t2[x]

    a = tc1.pop(0)
    b = tc2.pop(0)

    tc1Len = len(tc1)
    tc2Len = len(tc2)

    while tc1Len >= 0 and tc2Len >= 0:
        if a > b:
            to.append(b)
            try:
                b = tc2.pop(0)
                tc2Len -= 1
            except:
                tc1Len = -1
                to.append(a)
                for y in tc1:
                    to.append(y)
        else:
            to.append(a)
            try:
                a = tc1.pop(0)
                tc1Len -= 1
            except:
                tc1Len = -1
                to.append(b)
                for y in tc2:
                    to.append(y)
    # if a > b:
    #     to.append(b)
    # else:
    #     to.append(a)
    # print("a", a, "b", b)
    # print("tc1",tc1)
    # print("tc2", tc2)
    # if len(tc1) == 0:
    #     for y in tc2:
    #         to.append(y)
    # else:
    #     for y in tc1:
    #         to.append(y)
    tO.append(to)

for x in tO:
    for y in x:
        print(y, end=" ")
    print()
