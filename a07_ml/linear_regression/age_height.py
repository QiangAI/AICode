# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

# 年龄
age = np.loadtxt('ex2x.dat')
# 身高
height = np.loadtxt('ex2y.dat')


figure = plt.figure('机器学习可视化',figsize=(5,4))
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8], label='年龄与身高')
ax.scatter(x=age, y=height)
plt.show()

