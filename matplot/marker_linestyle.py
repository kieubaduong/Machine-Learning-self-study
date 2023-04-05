import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]
# marker: định dạng của marker (điểm đánh dấu) trên đường vẽ. Ví dụ: 'o' (tròn), '^' (tam giác), '*' (sao)...
# ls (linestyle): định dạng của đường vẽ. Ví dụ: 'dashed' (đứt), 'dotted' (chấm), 'solid' (liền)...
# c (color): màu sắc của đường vẽ.
# ms (marker size): kích thước của marker.
# mec (marker edge color): màu sắc của viền marker.
# mew (marker edge width): độ rộng của viền marker.
# mfc (marker face color): màu sắc của phần bên trong marker.
# lw (line width): độ rộng của đường vẽ.
plt.plot(x, y, marker = 'o', ls = 'dashed', c = 'r', ms = 20, mec = 'g', mew = 5, mfc = 'b', lw = 10)

plt.clf() # clear the previous plot

# draw multi lines by plot multiple times
plt.plot(x)
plt.plot(y)

plt.show()

