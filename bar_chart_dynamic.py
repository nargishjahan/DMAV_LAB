import matplotlib.pyplot as plt

x = list(map(int, input("Enter the values for x-axis: ").split()))
y = list(map(int, input("Enter the values for y-axis: ").split()))

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Bar Chart")
plt.bar(x,y)
plt.show()