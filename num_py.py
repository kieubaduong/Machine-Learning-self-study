import numpy as np

a = np.array([1, 2, 3, 4, 5])

print(a) # [1 2 3 4 5]

# number of dimensions array a
print(a.ndim) # 1

# index 2 to 4
print(a[2:4]) # [3 4]

b = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])

# number of dimensions array b
print(b.shape) # (2, 3)
print(b.ndim) # 2

# length of array b
print(len(b[0])) # 3

b=np.array([5,3 ,2, 1, 4])

print(a-b) # [-4 -1  1  3  1]
print(a*b) # [ 5  6  9 16 25]
print(a/b) # [0.2        0.66666667 1.5        4.         1.25      ]