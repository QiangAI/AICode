#coding=utf-8
import matplotlib.pyplot as plt
import matplotlib.patches as patch
import numpy as np
def yourfunc(p1):
    print(p1)
fig=plt.figure()
ax=fig.add_subplot(111)
line=plt.Line2D([0.1,0.3,0.5,0.9],[0.5,0.5,0.5,0.5])
line.set_linewidth(3)
line.set_marker(11)
line.set_markeredgecolor((1,0,0,1))
line.set_markerfacecolor((0,0,1,1))
line.set_markersize(20)
line.set_pickradius(1)
line.set_markevery(2)
line.set_picker(True)

ax.add_artist(line)

fig.canvas.mpl_connect('pick_event', yourfunc)

plt.show()