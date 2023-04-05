import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

# declare 2x2 matrix graph with index from 1 to 4
plt.subplot(2, 2, 1)
plt.title("SALES")
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 2, 2)
plt.title("INCOME")
plt.plot(x,y)



x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 2, 3)
plt.title("ANOTHER SALES")
plt.plot(x,y)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 2, 4)
plt.title("ANOTHER INCOME")
plt.plot(x,y)

plt.suptitle("MY SHOP")

# set space between subplots
plt.subplots_adjust(hspace=0.5)
plt.show()