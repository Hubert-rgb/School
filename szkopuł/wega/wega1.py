t = []
for i in range(1000):
    a = input().rstrip()
    t.append(a)
out = ""
for i in range(39, 1000, 40):
    out += t[i][9]
print(out)