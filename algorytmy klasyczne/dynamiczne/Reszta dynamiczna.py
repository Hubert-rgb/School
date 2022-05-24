kwota=int(input("Podaj kwotę do wydania ").rstrip())
inputValues=input("Podaj wartości monet, w jednym wierszu oddzielone spacją ").rstrip()
inputValues=inputValues.split(" ")
inputValues=[int(c) for c in inputValues]
inputValues.sort(reverse=True)
ile=[999999]*(kwota + 1)
uzyte_monety=[0]*(kwota + 1)
ile[0]=0
for moneta in inputValues:
    uzyte_monety[0]=moneta
    counter=moneta
    while counter<=kwota:
        if ile[counter]>ile[counter - moneta]+1:
            ile[counter]= ile[counter - moneta] + 1
            uzyte_monety[counter]=moneta
        counter+=moneta
while kwota>0:
    print(uzyte_monety[kwota])
    kwota-=uzyte_monety[kwota]