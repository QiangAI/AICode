#coding=utf-8

'''
import matplotlib.pyplot as plt
#建议不要使用Figure构造器创建Figure对象
fig=plt.figure()
fig.show()
'''

##############################

'''
import matplotlib.pyplot as plt
#建议不要使用Figure构造器创建Figure对象
fig=plt.figure(
    num='岗位分析趋势图',
    figsize=(5.5,3.5),
    dpi=100,
    facecolor=(0,1,0),
    edgecolor=(1,0,0),
    frameon=True,
    linewidth=3
)
plt.plot(1,1)
fig.show(warn=False)
plt.show()
'''
############################
'''
#coding=utf-8
import matplotlib
import matplotlib.pyplot as plt

for key in matplotlib.rcParams.keys():
    if 'figure' in key:
        print(key,':',matplotlib.rcParams[key])

for key in matplotlib.rcParams.keys():
    if 'linewidth' in key:
        print(key,":",matplotlib.rcParams[key])
'''
import matplotlib.pyplot as plt
import matplotlib as mpl
#建议不要使用Figure构造器创建Figure对象
mpl.rcParams['figure.figsize']=(5.5,3.5)
mpl.rcParams['figure.dpi']=100
mpl.rcParams['figure.facecolor']=(1,1,0,1)
mpl.rcParams['figure.edgecolor']=(1,0,1,1)
mpl.rcParams['figure.frameon']=True
fig=plt.figure(num='岗位分析趋势图',linewidth=3)
plt.plot(1,1)
fig.show(warn=False)
plt.show()