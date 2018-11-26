#coding=utf-8
import numpy as np
import tensorflow as tf

#1.scalar数据
rd1=tf.Variable(tf.random_uniform([],-1.0,1.0))
tf.summary.scalar("rd1",rd1)
rd2=tf.Variable(tf.random_uniform([],-1.0,1.0))
tf.summary.scalar("rd2",rd2)

#2.数据合并
me=tf.summary.merge_all()

#2.图执行
session=tf.Session()
#创建一个图数据IO写入器
writer=tf.summary.FileWriter("./scalar",graph=session.graph)
init_op= tf.global_variables_initializer()
session.run(init_op)

#写100个随机变量
for i in range(100):
    #3.计算合并数据
    data= session.run(me)
    #4.合并数据用IO写入文件
    writer.add_summary(data,i)

#关闭图写入器
writer.close()
