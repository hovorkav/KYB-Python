import matplotlib.pyplot as plt
import numpy as np
x = []
y = []
for i in range(0,100):
    x.append(i)
    y.append(float(np.sin(i)))
print(x,y)
plt.plot(x,y)
plt.show()