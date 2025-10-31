text = "ahoj"
text2 = 'ahooj'
print(text)



a = "abc"
b = "def"

print(a+b)
print(a*3)

c = "a"
for i in range(5):
    c = c + "a"
print(c)


koule = "Ahoj Karle, jak se máš?"
print(koule[6])

for i in range(len(koule)):
    print(koule[i])
print(koule[5:10:2])
print(koule[12:])
print(koule[:12])
ha = "Jelenovi Pivo Nelej"

for i in range(len(ha)):
    print(ha[i])

print(koule.index(","))