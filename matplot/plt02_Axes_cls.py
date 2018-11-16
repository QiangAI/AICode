#coding=utf-8
import matplotlib.pyplot as plt
fig=plt.figure('技术趋势图')
ax1=plt.Axes(
    fig,
    [0.1,0.1,0.8,0.8],
    title="趋势图",
    xlabel='x坐标',ylabel='y坐标',
    xticks=[1,2,3,4,5,6],yticks=[1,2,3],
    xticklabels=['a','b','c'],
    #yticklabels=['A','B','C','D','E','F'],
    ymargin=-0.2
)
fig.add_axes(ax1)
fig.show(warn=False)
plt.show()