t = ""

for i in range(2000):
    funkcja, co = input().strip().split(" ")
    if funkcja == "DOPISZ":
        t = t + co
    elif funkcja == "ZMIEN":
        t = t[:-1]
        t += co
    elif funkcja == "USUN":
        t = t[:-1]
    elif funkcja == "PRZESUN":
        x = 0
        while x < len(t):
            if t[x] == co:
                if co == "Z":
                    t2 = t[x + 1:]
                    t3 = t[:x]
                    t = t3 + "A" + t2
                else:
                    char = chr(ord(t[x]) + 1)
                    t2 = t[x + 1:]
                    t3 = t[:x]
                    t = t3 + char + t2
                x = len(t) + 1
            x += 1
   #print(t)
print(t)