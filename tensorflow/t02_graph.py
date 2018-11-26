#coding=utf-8
import numpy as np
import tensorflow as tf

#1.描述图
m1=np.random.uniform(0,1,(4,3))
m2=np.random.uniform(0,1,(3,2))
r=tf.matmul(m1,m2)

#2.图执行
session=tf.Session()

#创建一个图数据IO写入器
writer=tf.summary.FileWriter("./graph",graph=session.graph)

init_op= tf.global_variables_initializer()
session.run(init_op)
re=session.run(r)
print(re)

#关闭图写入器
writer.close()
