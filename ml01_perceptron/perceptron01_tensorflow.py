#coding=utf-8
from sklearn import datasets    #获取鸢尾花数据样本
import tensorflow  as tf        #tensoflow模块
import time

start = time.clock()

#########################################
LEARNING_RATE=0.0001        #学习率
TIMES=10                    #训练轮数

DATA_SIZE=4                 #特征个数，也就是训练样本的数组长度

#一、感知器计算图描述
#1.描述输入数据：训练样本sample，训练样本的期望标签label
sample=tf.placeholder(dtype=tf.float32,shape=[None,DATA_SIZE])  #第一个是训练样本个数（不确定设置为None），第二个特征个数
label=tf.placeholder(dtype=tf.float32,shape=[None])                 #训练样本的期望标签是标量，其值为0或者1

#2.描述权重与偏置值（初始值随机）
w_init=tf.random_uniform(shape=[DATA_SIZE,1],minval=-0.1,maxval=0.1,dtype=tf.float32)
weights=tf.Variable(w_init)   #传统方式

b_init=tf.random_uniform(shape=[],minval=-0.1,maxval=0.1,dtype=tf.float32)
bias=tf.Variable(b_init)

#3.描述加权求和操作节点
amount=tf.matmul(sample,weights)+bias

#4.描述损失函数操作节点
loss=tf.reduce_mean(tf.square(amount-label))

#5.描述梯度优化操作节点
trainer=tf.train.GradientDescentOptimizer(LEARNING_RATE).minimize(loss) #使用学习率，最小化误差损失

#二、感知器计算图运行
#加载鸢尾花数据
data,target=datasets.load_iris(return_X_y=True)     #第一个返回值是样本数据，第二个返回值是样本的期望标签
#取前面100个眼本测试（这100个是线性可分的）
train_data=data[:100]
label_data=target[:100]     #第一类是0，第二类是1

#1.构建运行会话
session=tf.Session()
#2.初始化环境
init_op=tf.global_variables_initializer()
session.run(init_op)
#---------------------------
graph_writer=tf.summary.FileWriter("./graph",graph=session.graph)
#---------------------------
#3.开始训练
print("开始训练！")
for n in range(TIMES):
    print("第%4d轮训练"%(n+1))
    for i in range(len(train_data)):
        session.run(trainer,feed_dict={sample:train_data[i:i+1],label:label_data[i:i+1]})
    #session.run(trainer, feed_dict={sample: train_data, label:label_data})
print("训练完毕！")

#4.测试训练
correct_counter=0
#前50个期望标签都是0（近似0.5以下都算正确）
for item in train_data[:50]:
    result=session.run(amount,feed_dict={sample:[item]})
    print(result)
    if result<0.5:
        correct_counter+=1
print("===============")
#后50个期望标签都是1（近似0.5以上都算正确）
for item in train_data[50:]:
    result = session.run(amount, feed_dict={sample: [item]})
    print(result)
    if result>=0.5:
        correct_counter+=1

#打印正确率：
print("正确率：%8.2f"%((correct_counter/100.0)*100))

#########################################
end=time.clock()
print("CPU运行时间：",end-start)

#-----------------------
graph_writer.close()
#-----------------------
