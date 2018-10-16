#coding=utf-8
import tensorflow as tf

x = tf.placeholder(tf.float32, [])  #标量
y = tf.placeholder(tf.float32, [])  #标量

r=1/2 *(x- y)       #随机均方误差损失计算

session=tf.Session()
init_op=tf.global_variables_initializer()
session.run(init_op)

#参数传递
re=session.run(r,feed_dict={x:10,y:20})
print(re)

