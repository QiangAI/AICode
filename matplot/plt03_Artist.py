#coding=utf-8
import matplotlib.pyplot as plt
import matplotlib.patches as patch
#创建一个Figure对象
fig=plt.figure()
#坐标系
ax=fig.add_subplot(111)
line=plt.Line2D([0.5,0.5],[0.503,0.5],linewidth=3,color=(1,0,0,1))
rect=patch.Rectangle((0.1,0.1),0.4,0.4)
ax.add_artist(line)
ax.add_artist(rect)
r=plt.Rectangle((0.6,0.6),0.2,0.2,angle=0.1,fill=False)
ax.add_artist(r)
plt.show()

