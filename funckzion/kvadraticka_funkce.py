def kvadraticka(a, b ,c):
    dis = (b**2) - (4*a*c)
    if dis < 0:
        return None
    elif dis == 0:
        vysledek = (-b)/(2*a)
        return vysledek
    else:
        vysledek = [(-b + dis**0.5)*0.5, (-b - dis**0.5)*0.5]
        return vysledek

#print(kvadraticka(1,2,-3))

def kvadratic_test():
    results = []
    for i in range(5):
        results.append(kvadraticka(1,i,1))
    return results

vysledky = kvadratic_test()
for ů in vysledky:
    print(ů)
