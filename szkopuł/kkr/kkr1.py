start = "11011010"
stop = "11010110"
dic = {}
for i in range(10):
    cyfra, kod = input().rstrip().split(" ")
    cyfra = int(cyfra)
    dic[cyfra] = kod
for i in range (500):
    smartCode = ""
    a = input().rstrip()
    intA = int(a)
    par = 0
    npar = 0
    while intA > 0:
        npar += intA%10
        intA = intA // 10
        par += intA%10
        intA = intA // 10
    kontrolna = (10 - ((npar * 3 + par) % 10)) % 10

    smartCode += start
    for x in a:
        smartCode += dic[int(x)]
    smartCode+=dic[kontrolna]
    smartCode+=stop
    print(smartCode)