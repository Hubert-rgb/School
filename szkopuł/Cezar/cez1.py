ile = int(input().rstrip())
k = 107
k = k % 26
for i in range(ile):
    a = input().rstrip()
    o = ""
    for x in a:
        ia = ord(x)
        #print(ia + k)
        if ia + k <= 90:
            ib = ia + k
        else:
            ib = 65 + (-90 + ia + k - 1)
        b = chr(ib)
        #print("ib", ib)
        o += b
    print(o)