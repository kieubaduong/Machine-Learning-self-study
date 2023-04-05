import matplotlib.pyplot as plt
import numpy as np


# draw a line with x array and y array
xPoints = np.array([0,200])
yPoints = np.array([0,200])
plt.plot(xPoints,yPoints)
plt.clf() # clear the previous plot

# draw a line with two points
firstPoint = np.array([0,0])
secondPoint = np.array([200,200])
plt.plot([firstPoint[0],secondPoint[0]],[firstPoint[1],secondPoint[1]],'ro') # 'ro' means red color and circle shape marker
plt.clf() # clear the previous plot

# plot without line
plt.plot([firstPoint[0],secondPoint[0]],[firstPoint[1],secondPoint[1]],'o') 
plt.clf() # clear the previous plot

# draw multiple lines
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints,'D')
plt.clf() # clear the previous plot

# default x points are index of y points array [0,1,2,3,4,5]
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.clf() # clear the previous plot




