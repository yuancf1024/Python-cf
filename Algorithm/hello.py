# print("Hello world!")

# s = input("输入一个数字:")

# print(s)
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,10)

y = np.sin(x)

plt.plot(x,y)

num=input("请输入你的名字：")
plt.show()

print(num)