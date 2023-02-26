def czyNależy(a, b):
    k1 = 0
    for j in range(len(a) - len(b) + 1):
        if a[j:j+len(b)] == b:
            k1+=1
    if k1 > 0:
        return True
    return False
def łączenie(a, b):
    out = ""
    for j in range(len(b)):
        #print("b", a[0:len(b) - j], b[j:])
        #print("a", a[len(a) + j - len(b):], b[:len(b) - j])

        if a[len(a) + j - len(b):] == b[:len(b) - j]:
            out += a
            #print("a", out)
            out += b[len(b) - j:]
            return out
        elif a[0:len(b) - j] == b[j:]:
            out += b
            #print("b", out)
            out += a[len(b) - j:]
            return out
    return out
k = 0
for i in range(200):
    a, b = input().rstrip().split(" ")
    lacz = łączenie(a, b)
    if czyNależy(a, b):
        print(a)
        pass
    elif lacz != "":
        print(łączenie(a, b))
        pass
    else:
        print(a + b)
        k += 1
#print(k)
