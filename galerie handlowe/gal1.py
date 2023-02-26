mMax = ""
ileMax = 0

mMin = ""
ileMin = 10000
for i in range(50):
    inT = input().strip()
    inT = inT.split(" ")
    kod = inT[0]
    inT = inT[1:]
    miasto = inT[0]
    inT = inT[1:]

    dicP = {}
    for j in range(0, len(inT), 2):
        inT[j] = int(inT[j])
        inT[j + 1] = int(inT[j + 1])
        if inT[j] != 0:
            p = inT[j] * inT[j + 1]
            dicP[p] = 1
    ile = len(dicP)

    if ile > ileMax:
        ileMax = ile
        mMax = miasto
    if ile < ileMin:
        ileMin = ile
        mMin = miasto
    #print(dicP)
print(mMax, ileMax)
print(mMin, ileMin)
