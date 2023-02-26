def f(a):
    if a == 1:
        return 4
    else:
        return 1 / (1 - f(a - 1))
print(f(100))