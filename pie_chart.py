import matplotlib.pyplot as plt

data = [10,40,20,5]
labels = "Reading Books", "Video Games", "Coding", "Travelling"

plt.pie(data, labels=labels)
plt.title("Activities")
plt.show()