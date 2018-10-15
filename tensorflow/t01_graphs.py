#coding=utf-8
import numpy as np
import tensorflow as tf

#1.描述图：数据节点，运行节点
#数据节点
m1=np.random.uniform(0,1,(4,3))
#数据节点
m2=np.random.uniform(0,1,(3,2))
#运算节点（r也算数据节点，通过matmul建立与m1、m2的数据与运算流 ）
r=tf.matmul(m1,m2)


#2.构建会话执行环境，并执行图。
#构建会话对象
session=tf.Session()
#使用会话初始化变量环境
init_op= tf.global_variables_initializer()  #构建一个初始化器
session.run(init_op)                        #执行初始化器，并完成全局变量初始化

#执行运算
re=session.run(r)                           #返回结果
print(re)



