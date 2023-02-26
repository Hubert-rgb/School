k = 0
fi = ""
for i in range(200):
    inp = input().rstrip()
    #print(inp[-1])
    if inp[0] == inp[-1]:
        if fi == "":
            fi = inp
        k += 1
print(k)
print(fi)