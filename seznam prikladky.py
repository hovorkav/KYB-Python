pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]

x = pole[0]
y = 0

for i in range(len(pole)):
    if x < pole[i]:
        x = pole[i]
        y = i
print(x)
print(y)

print("*****************************************************************")

x = pole[0]
y = 0

for i in range(1, len(pole)):
    if x > pole[i]:
        x = pole[i]
        y = i
print(x)
print(y)


print("*****************************************************************")


y = 0

for i in range(len(pole)):
    y += pole[i]

print("prumer seznamu: ", y/len(pole) )


print("*****************************************************************")
x = 0
y = 5
for i in range(len(pole)):
    if pole[i] > y:
        x += 1

print(x)

print("*****************************************************************")
x = 0
y = 5

for i in range(len(pole)):
    if pole[i] < y:
        x += 1
print(x)

print("*****************************************************************")
x = 0

for i in range(len(pole)):
    x += pole[i]


print(x)
print("*****************************************************************")
x = []
for i in range(len(pole)-1, -1, -1):
    x.append(pole[i])
print(x)

print("*****************************************************************")
pole1 = [5, 2, 9, 1, 7, 3, 10, 6, 4]
pole2 = [3, 5, 4, 7, 5, 3, 4, 5, 10]
pole_vysledne = []
x = 0

for i in range(len(pole1)):
    x = pole1[i] + pole2[i]
    pole_vysledne.append(x)
print(pole_vysledne)

print("*****************************************************************")
pole1 = [5, 2, 9, 1, 7, 3, 10, 6, 4]
pole2 = [3, 5, 4, 7, 5, 3, 4, 5, 10]
pole_vysledne = []
x = 0

for i in range(len(pole1)):
    x = pole1[i] + pole2[-i-1]
    pole_vysledne.append(x)
print(pole_vysledne)

print("*****************************************************************")
pole = [5, 2, 9, 1, 7, 3, 10, 6, 4]
haha = []
x = pole[0]
for i in range(len(pole)):
    if pole[i] > x:
        x = pole[i]
        haha.append(x)
#    elif pole[i] >
print(haha)
print(haha[-2])
print("*****************************************************************")

pole = [1, 2, 3, 4, 4, 5, 8, 19]


for i in range(len(pole)-1):
    print(x)
    if pole[i] > pole[i+1]:
        o = False
        break
if x == len(pole):
    print("Pole je serazene")

print("*****************************************************************")
pole1 = [5, 2, 9, 1, 7, 3, 10, 6, 4]
x = 0
y = 0
for i in range(len(pole)):
    if pole[i] % 2 == 0:
        x += 1
    else:
        y += 1


print("Pocet sudych cisel je:" ,x," a pocet lichych cisel je: ",y )


