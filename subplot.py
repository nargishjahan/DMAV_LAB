import matplotlib.pyplot as plt
import numpy as py

plt.subplot(1,2,1)
plt.plot([2,1,3],[1,2,4])
plt.title("Plot1")

plt.subplot(1,2,2)
plt.plot([1,2,9],[2,1,4])
plt.title("Plot2")

plt.tight_layout()
plt.show()



