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
ile = int(input().rstrip())
for i in range(ile):
    a = int(input().rstrip())
    if czyPierwsza(a) and czyPierwsza(int(str(a)[::-1])):
        t.append(a)
for i in t:
    print(i)