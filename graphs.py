import numpy as np
import matplotlib.pyplot as plt
size = 5
a = np.random.random(size)
b = np.random.random(size)
c = np.random.random(size)
x = np.arange(size)
# 有多少个类型，只需更改n即可
total_width, n = 0.8, 3
width = total_width / n
# 重新拟定x的坐标
x = x - (total_width - width) / 2
# 这里使用的是偏移
plt.bar(x, a, width=width, label='a')
plt.bar(x + width, b, width=width, label='b')
plt.bar(x + 2 * width, c, width=width, label='c')
plt.legend()
# plt.show()

x1 = np.linspace(0, 2, 100)
plt.plot(x1, x1, label='linear')
plt.plot(x1, x1**2, label='quadratic')
plt.plot(x1, x1**3, label='cubic')
plt.xlabel('x1 label')
plt.ylabel('y1 label')
plt.title("Simple Plot")
plt.legend()
plt.show()

