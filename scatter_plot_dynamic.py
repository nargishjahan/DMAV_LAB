import matplotlib.pyplot as plt

data = list(map(int, input("Enter data: ").split()))
labels = input("Enter the labels: ").split()

plt.scatter(data, labels)
plt.title("Activities")
plt.show()
