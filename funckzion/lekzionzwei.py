def secti(a, b):
    globalni_promenna = 20
    return [a+b+globalni_promenna, globalni_promenna]

def secti_tuple(a, b):
    globalni_promenna = 20
    return a+b+globalni_promenna, globalni_promenna
    
globalni_promenna = 10
y = secti(5, 3)





print(y)
print(type(y))
print(secti_tuple(5,3))
print(type(secti_tuple(5,3)))