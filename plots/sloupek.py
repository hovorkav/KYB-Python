import matplotlib.pyplot as plt

labels = ["prvaci", "druhaci", "tretaci", "ctvrtaci"]
values = [100,80,60,40]
y = [80,75,60,45]
plt.bar(labels,values)
plt.plot(labels,y,label = "cara", color = "red",linestyle = ":")
plt.legend()
plt.grid(True, axis="y", which="major")
plt.title("Pocet vyhozenych studentu")
plt.show()