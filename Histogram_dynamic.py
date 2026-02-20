import matplotlib.pyplot as plt

data = list(map(int,input("Enter data: ").split(1)))

plt.hist(data,bins=20)
plt.show()