ile = int(input().rstrip())
for i in range(ile):
    a, k = input().rstrip().split(" ")
    k = int(k)
    k = k % 26
    o = ""
    for x in a:
        ia = ord(x)
        #print(ia - k)
        if ia - k >= 65:
            ib = ia - k
        else:
            ib = 91 - (65 - (ia - k))
        b = chr(ib)
        #print("ib", ib)
        o += b
    print(o)