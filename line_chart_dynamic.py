import matplotlib.pyplot as plt

x = list(map(int,input("Enter the value of x: ").split()))
y = list(map(int,input("Enter the value of y: ").split()))

plt.plot(x,y)
plt.xlabel("x-axis")
plt.ylabel("y-label")
plt.title("Line Chart")
plt.show()