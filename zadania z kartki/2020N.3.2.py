n = 45778
w = 0
while n != 0:
    w = w + (n % 10)
    n = n // 10
print(w)