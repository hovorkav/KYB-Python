''''''''''''''''
heslo = input("Zadej heslo: ")
skutecne_heslo = "42"
if heslo == skutecne_heslo:print("Access granted")
else:print("Access denied")





while True:
    cislo_text = input("zadej cislo: ")
    try:
        cislo = int(cislo_text)
        break
    except:
        print("Cislo retarde")


print(str(cislo) + " + 10 = " + str(cislo+10))
'''''''''''''''''
import numpy as np
skore = 0
x = 10
y = 0
hra = True
while hra == True:
    y = 0
    cislo = np.random.randint(1, 21)
    for i in range(x):
        pokus = int(input("Hadej: "))
        if pokus == cislo:
            print("uhodls, +1 skore")
            print("skore: "+str(skore+1) + "; pocet pokusu:"+ str(y) )
            skore += 1
            break
        elif pokus < cislo:
            print("nene cislo je VETSI")
            y += 1
            print("zbyva "+ str(10-y)+" pokusu")
        elif pokus > cislo:
            print("nene, cislo je MENSI")
            y += 1
            print("zbyva " + str(10 - y) + " pokusu")
        if y == x:
            hra = False
            print("Finalni vysledek: "+str(skore))




