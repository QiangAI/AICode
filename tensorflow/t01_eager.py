#coding=utf-8

import sys
import numpy as np
import tensorflow as tf

#1.开启eager执行方式
tf.enable_eager_execution()

#2.判定当前是否是eager执行方式
if tf.executing_eagerly():
    print("Eager执行方式")
else:
    print("Graphs执行方式")
    sys.exit(-1)


#实现eager执行方式
m1=np.random.uniform(0,1,(4,3))
m2=np.random.uniform(0,1,(3,2))

r=tf.matmul(m1,m2)

print(r)



