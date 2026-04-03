import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,30,35]

plt.subplot(1,2,1)
plt.xlim(0,10)
plt.ylim(0,60)
plt.plot(x,y)
plt.title("plot 1")

plt.subplot(1,2,2)
plt.bar(x,y)
plt.title("plot 2")
plt.show()