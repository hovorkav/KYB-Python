def funkc(a,b,c=10,d=10):
    return a+b+c+d

print(funkc(1,2,3,4))
print(funkc(1,2,3))
print(funkc(1,2,3,4))

def jedembomby(*args):
    print(args)
    souc = 0
    for i in range(len(args)):
        souc += args[i]    
    return souc

print(jedembomby(1,2,5,6,7,2,45,662))