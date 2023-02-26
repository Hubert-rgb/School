def czyPierwsza(a):
    k = 0
    if a == 2:
        return True
    elif a==1:
        return False
    for i in range(2, int(a ** 0.5 + 1)):
        if a % i == 0:
            k +=1
    if k == 0:
        return True
    else:
        return False
t = []
for i in range(300):
    a = int(input().rstrip())
    if a >= 100 and a <= 5000:
        if czyPierwsza(a):
            t.append(a)
for i in t:
    print(i)