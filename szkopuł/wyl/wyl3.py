ile = int(input().rstrip())

def w(n):
    n1 = 0
    while n > 0:
        n1+= n%10
        n//=10
    if n1 // 10 > 0:
        return w(n1)
    else:
        return n1
k = 0
for i in range(ile):
    a= int(input().rstrip())
    if w(a) == 1:
        k += 1
print(k)