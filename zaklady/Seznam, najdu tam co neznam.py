a = [1, 2, 3, 4, 5]

print(a)

haha = ["mozna", 0.55, True, [90, 60, 90]]
print(haha)

print(haha[2:len(haha)])
print(type(haha[2:len(haha)]))

x = [1, 2, 8, 4, 6, 11, 7, 4]

for i in range(len(x)):
    if (i)%2 == 0:
        print(x[i])