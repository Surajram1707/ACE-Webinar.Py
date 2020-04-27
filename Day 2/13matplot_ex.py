import matplotlib.pyplot as plt

a = [1,3,6,7]
b = [2,4,5,6]

plt.plot(a,b,"bd") # b - color o - points
plt.title("Line Graph")
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
plt.savefig("graph.png")
plt.show()

plt.bar(a,b,color="red",width=[0.5]) #barh - horizontal
plt.show()

plt.hist(a, bins = 20)
plt.show()