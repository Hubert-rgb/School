max = "02"
min = "100000002"
for i in range(999):
    inp = input().rstrip()
    last = inp[-1:]
    par = inp[:-1]

    dec = int(par, int(last))
    lastMax = int(max[-1:])
    decMax = int(max[:-1], lastMax)
    if dec > decMax:
        max = inp
    if dec < int(min[:-1], int(min[-1:])):
        min = inp
print(min)
print(max)
print(int(min[:-1], int(min[-1:])))
print(int(max[:-1], int(min[-1:])))