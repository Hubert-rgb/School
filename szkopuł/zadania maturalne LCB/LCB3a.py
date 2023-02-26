t = []
ile = 200
k = 0
for i in range(ile):
    a = int(input().rstrip())
    t.append(a)
for i in range(ile):
    for j in range(i, ile):
        for h in range(j, ile):
            x = t[i]
            y = t[j]
            z = t[h]
            arr = [x, y, z]
            if x != y != z and ((z % y == 0 and y % x == 0)
                                or (x % y == 0 and y % z == 0)
                                or (y % z == 0 and z % x == 0)
                                or (y % x == 0 and x % z == 0)
                                or (z % x == 0 and x % y == 0)
                                or (x % z == 0 and z % y == 0)):
                k += 1
                i += 1

print(k)