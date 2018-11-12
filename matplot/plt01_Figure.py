#coding=utf-8
import matplotlib.pyplot as plt
'''
Figure的创建方式
'''
#创建一个Figure对象
#manager=plt.get_current_fig_manager()
#fig=plt.figure()
#fig=manager.canvas.figure
fig=plt.gcf()
#print(manager)
#创建一个子图Axes对象
axes1=plt.axes((0,0,1,1))
#创建一个Artist对象
line=plt.Line2D([0,1],[0,1])

#添加Artist对象到子图Axes
l=axes1.add_artist(line)
#添加子图Axes对象到Figure对象
fig.add_axes(axes1)
#显示Figure对象
fig.show(warn=False)
#显示当前所有Figure对象（与fig.show()可以选择使用一个）
