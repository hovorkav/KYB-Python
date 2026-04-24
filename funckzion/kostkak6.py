import random as rnd


def hod_k6() -> int:
    """
    Vrati nahodne cislo z intervalu 1 az 6.
    """
    return rnd.randint(1, 6)


hod_k6()


def pocet_pokusu_na_sestku() -> int:
    """
    Zkousi opakovane hodit 6 a vrati pocet potrebnych pokusu.
    """
    x = hod_k6()
    count = 1
    while x != 6:
        count += 1
        x = hod_k6()
    return count


print(pocet_pokusu_na_sestku())

def sim_pokusu(n):
    vys = [0]*20
    for i in range(n):
        x = pocet_pokusu_na_sestku()
        if x > 20:
            vys[19] += 1
        else:
            vys[x-1] += 1
    return vys
#rnd.seed(5)
print(sim_pokusu(1000000))
