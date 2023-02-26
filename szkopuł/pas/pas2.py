k  = 0
for i in range(200):
    k1=0
    a, b = input().rstrip().split(" ")
    #print(a[0:len(b)])
    lenB = len(b)
    for j in range(len(a) - lenB + 1):
        #print(a[j:j+lenB ])
        if a[j:j+lenB] == b:

            k1+=1
    if k1 > 0:
        k+=1
print(k)