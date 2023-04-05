import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]
# ms (marker size): kích thước của marker.
# mec (marker edge color): màu sắc của viền marker.
# mew (marker edge width): độ rộng của viền marker.
# mfc (marker face color): màu sắc của phần bên trong marker.
plt.plot(x, y, marker = 'o', linestyle = 'dashed', color = 'r', ms = 20, mec = 'g', mew = 5, mfc = 'b')

plt.show()