import matplotlib.pyplot as plt

data = list(map(int, input("Enter the data: ").split()))
labels = input("Enter the labels: ").spilt()

plt.pie(data, labels=labels)
plt.title("Activities")
plt.show()