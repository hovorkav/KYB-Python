list = [5,10,63,2,120,98,45, 110, 88, 119, 20, 71]

def second(mylist):
    nej = mylist[0]
    dru = mylist[0]
    #x = list[0]
    for i in range(1, len(mylist)):
        if nej < mylist[i]:
            dru = nej
            nej = mylist[i]
        elif dru < list[i]:
            dru = list[i]

    return dru



print(second(list))

def isprime(cis):
    for i in range(2,cis):
        if cis%(i) == 0:
            return False      
    return True
print(isprime(624896709750))


print("***********************************\n")
vstup = [5, 13, 31, 55, 17, 54]

def countprimearr(pole):
    count = 0
    for j in pole:
        if isprime(j):
            count += 1
    return count   
print(countprimearr(vstup))

print("***********************************\n")
print("***********************************\n")

def adding(a,b):
    return a+b
def substract(a, b):
    return a-b
def calc(func, a ,b):
    return(func(a, b))


print(calc(adding, 5, 1))
print(calc(substract, 9, 2))