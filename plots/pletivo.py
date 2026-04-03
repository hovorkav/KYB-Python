import numpy as np
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9]
y = [99,86,87,88,11,86,103,87]

x1 = [1,2,3]
y1 = [2,3,4]

x2 = [1,2,3]
y2 = [5,1,2]

x3 = [1,3,5]
y3 = [1,7,5]

plt.scatter(x1,y1,color = 'red', marker="o",s = 10, label="data1")
plt.scatter(x2,y2,color = 'blue', marker="s", label="data2")
plt.scatter(x1,y1,color = 'purple', marker="^", label="data3")
plt.grid(True)
plt.show()