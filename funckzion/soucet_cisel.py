def soucet2(n):
    if n == 1:
        return 1
    else:
        return n + soucet2(n-1)

print(soucet2(10))