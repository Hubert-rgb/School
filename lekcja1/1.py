t = []
for i in range(3):
    firstName = input()
    lastName = input()
    height = input()
    pesel = input()
    t.append([firstName, lastName, height, pesel])
for i in range(3):
    print(t[i][0], t[i][1])