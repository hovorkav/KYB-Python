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


