coMax = ""
ileMax = 0

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = {}
for x in alfabet:
    t[x] = 0

for i in range(2000):
     funkcja, co = input().strip().split(" ")
     if funkcja == "DOPISZ":
         t[co] += 1
ts = sorted(t.items(), key=lambda x:x[1], reverse=True)
value = ts.pop(0)
print(value[0], value[1])