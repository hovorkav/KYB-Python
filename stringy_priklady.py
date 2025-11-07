a = "Ahoj Karle, jak se máš?"
x = len(a)

for i in range(x):
    print(a[i])

for i in range(x):
    print(a[-i-1])

for i in range(x):
    print(a[:i+1:1])


for i in range(x-1):
    print(a[i:i+2])

for i in range(x-2):
    print(a[i:i+3])

for i in range(int(x/2)+1):
    print(a[i],a[-i-1])


for i in range(x):
    print(a[i])
print(a.zfill(1000000))
