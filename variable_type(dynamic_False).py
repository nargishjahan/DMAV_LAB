import matplotlib.pyplot as plt

x = list(map(int, input("Enter the values for x-axis: ").split()))
y = list(map(int, input("Enter the values for y-axis: ").split()))

plt.plot(x,y,marker='o')

plt.xlabel("X Values (Independent variable)")
plt.ylabel("Y Values (Dependent variable)")

plt.title("X-Y axiz data plot")

plt.grid(False)

plt.show()

                                                 