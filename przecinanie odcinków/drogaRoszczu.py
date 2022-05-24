ile = input().rstrip()
ile = int(ile)
d = []
d.append(ile)
for i in range(ile* (ile + 1) * 2):
    line = input().rstrip()
    lineArr = line.split(" ")
    d.append(line)
N=int(d[0])
dane=[[[0,0] for i in range(N+1)]for j in range(N+1)]
poprzednicy=[[[0,0] for i in range(N+1)]for j in range(N+1)]
koszt=[[0 for i in range(N+1)]for j in range(N+1)]
#index 0 prawo, index1 - dół
for i in range(1,len(d)):
    a=d[i].split(" ")
    for i in range(len(a)):
        a[i] = int(a[i])
    if a.count("")>0:
        a.remove("")
    for j in range(ile - 1):
        a[j]=int(a[j])
    if a[0]==a[2]:
        dane[a[1]][a[0]][1]=a[4]
    else:
        dane[a[1]][a[0]][0]=a[4]

#uwaga - współrzędne wiersz/kolumna - czyli y następnie x
poprzednicy[0][0]=[-1,-1]
for w in range(1,N+1):
    poprzednicy[w][0][0]=w-1
    poprzednicy[w][0][1]=0
    koszt[w][0]=koszt[w-1][0]+dane[w-1][0][1]
for k in range(1,N+1):
    poprzednicy[0][k][0]=0
    poprzednicy[0][k][1]=k-1
    koszt[0][k]=koszt[0][k-1]+dane[0][k-1][0]

print(koszt, poprzednicy)
for w in range(1,N+1):
    for k in range(1,N+1):
        if koszt[w-1][k]+dane[w-1][k][1]<koszt[w][k-1]+dane[w][k-1][0]:
            koszt[w][k]=koszt[w-1][k]+dane[w-1][k][1]
            poprzednicy[w][k][0]=w-1
            poprzednicy[w][k][1]=k
        else:
            koszt[w][k]=koszt[w][k-1]+dane[w][k-1][0]
            poprzednicy[w][k][0]=w
            poprzednicy[w][k][1]=k-1

'''
for i in range(N+1):
    print(poprzednicy[i])
for i in range(N+1):
    print(koszt[i])
'''
x_end=int(input("Podaj x końcowe "))
y_end=int(input("Podaj y końcowe "))
x=x_end
y=y_end
print("Koszt dojścia ",koszt[y][x])
r=[[x,y]]
while x!=0 or y!=0:
    x_n=poprzednicy[y][x][1]
    y_n=poprzednicy[y][x][0]
    x=x_n
    y=y_n
    r.append([x,y])
for i in range(len(r)-1,-1,-1):
    print(r[i][1],",",r[i][0],end="")
    if i!=0:
        print(" -> ",end="")