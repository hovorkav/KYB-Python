#rekurze

def fakt(a):
    if a != 0:
        return a*fakt(a-1)
    else:
        return 1
    
print(fakt(5))
