def szyfruj(a, k):
    o = ""
    for x in a:
        ia = ord(x)
        if ia + k <= 90:
            ib = ia + k
        else:
            ib = 65 + (-90 + ia + k - 1)
        b = chr(ib)
        o += b
    return o

ile = int(input().rstrip())
for i in range(ile):
    a, c = input().rstrip().split(" ")
    cou = 0
    k = 1
    while k < 27:
        #print(o, c)
        if szyfruj(a, k) == c:
            cou += 1
            k = 28
        k += 1
    if cou > 1:
        print("błąd")
    elif cou == 0:
        print(a)