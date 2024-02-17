
import numpy as np

array = np.zeros((5, 5), dtype=int)


pos1 = np.random.choice(5, 2, replace=False)
pos2 = np.random.choice(5, 2, replace=False)
while np.array_equal(pos1, pos2):
    pos2 = np.random.choice(5, 2, replace=False)
array[pos1[0], pos1[1]] = 1
array[pos2[0], pos2[1]] = 1
print (array)


x1, y1 = pos1
x2, y2 = pos2
while x1 != x2 or y1 != y2:
    if x1 < x2:
        x1 += 1
    elif x1 > x2:
        x1 -= 1
    elif y1 < y2:
        y1 += 1
    elif y1 > y2:
        y1 -= 1
    array[x1, y1] = 1


print(array)