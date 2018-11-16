#coding=utf-8
import matplotlib.pyplot as plt
import matplotlib
'''
matplotlib.rcParams
'''
print(matplotlib.rcParams.keys())
print(matplotlib.rcParams['figure.figsize'])
print(matplotlib.rcParams['figure.dpi'])
matplotlib.rcParams['figure.figsize']=[12,8]
fig=plt.figure()
ax = fig.subplots()
ax.plot([1, 2, 3])
plt.show()

