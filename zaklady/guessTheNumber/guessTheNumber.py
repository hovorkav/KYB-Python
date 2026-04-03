import time as clk
import numpy as np
import random
skore = 0
x = 10
y = 0
d = 0
hra = True
while hra == True:
    y = 0
    cislo = np.random.randint(1, 21)
    for i in range(x):
        try: pokus = int(input("Hadej: "))
        except ValueError:
            while d<1000:
                print("CISLO RESTARTE!")
                clk.sleep(0.005)
                d += 1
            exit()
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
            print("Hledane cislo bylo "+str(cislo))
            print("Finalni skore: "+str(skore))
            exit()




