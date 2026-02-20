import matplotlib.pyplot as plt
import numpy as py

x = list(map(int, input("Enter the values for plot1: ").split()))
plt.subplot(1,2,1)
plt.title("Plot1")

y = list(map(int, input("Enter the values for plot2: ").split()))
plt.subplot(1,2,2)
plt.title("Plot2")

plt.tight_layout()
plt.show()