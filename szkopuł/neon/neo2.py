coMax = ""
ileMax = 0

funkcja, co = input().strip().split(" ")
terazCo = funkcja
terazIle = 1
for i in range(1999):
    funkcja, co = input().strip().split(" ")
    if funkcja == terazCo:
        terazIle+=1
    else:
        if ileMax < terazIle:
            ileMax = terazIle
            coMax = terazCo
        terazIle = 1
        terazCo = funkcja
if ileMax < terazIle:
    ileMax = terazIle
    coMax = terazCo
print(coMax, ileMax)