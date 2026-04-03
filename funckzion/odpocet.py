def odpocet(n):
    if n == 0:
        print("BUM!"); return
    else:
        print("Cas je T - "+str(n))
        return odpocet(n-1)
print(odpocet(5))