# !/usr/bin/env python
# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
# 折线图
x = np.array([1,2,3,4,5])
y = np.array([20,15,18,16,12])
plt.plot(x,y,color="green",linewidth=10)
# 柱状图
x = np.array([1,2,3,4,5])
y = np.array([14,16,18,12,21])
plt.bar(x,y,alpha=1,color='#ffff00',width=0.2)
plt.show()

