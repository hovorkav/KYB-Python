vstup = input('Zadej číslo: ')
try:
    cislo = int(vstup)
except:
    cislo = 0
print("vstup = " + vstup)

if  cislo > 5:
    if cislo > 10:
        print("nevim, neco")
    else:
        print("jo je to větší")

elif cislo < 5:
    print("ne je to menší")
elif cislo == 5:
    print("máš to stejný restarte")
else:
    print("a jak se ti tohle povedlo?")

a = int(input("Zadej A: "))
b = int(input("Zadej B: "))
c = int(input("Zadej C: "))

d = b**2 - 4*a*c
if d == 0:
    print("jedno reseni v R")
elif d < 0:
    print("nula reseni v R")
elif d > 0:
    print("dve reseni v R")