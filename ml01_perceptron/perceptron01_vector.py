#coding=utf-8
import  numpy as np             #构造权重数组与数学计算
import random                   #随机数
from sklearn import datasets    #获取鸢尾花数据样本

class Perceptron_Scalar:
    '''
    感知器的前置条件：
    1.特征数据，特征数据在训练中需要改变，通过函数参数赋值；
    2.特征数据的大小，决定这权重的个数；还要额外设置一个偏置项
    3.激活函数

    注意：这里默认采用随机均方误差损失函数。
    '''
    def __init__(self,input_size,activation_function,activation_derivative,learn_rate):
        '''
        初始化感知器需要的前置条件：
        :param input_size:              输出特征数据的维数大小
        :param activation_function:     激活函数，我们这里使用恒等激活函数f(x)=x
        :param activation_derivative:   激活函数的导数
        :param learn_rate:              学习率
        '''
        #1.初始化权重向量,大小为输入特征数据大小
        self.weights=np.random.uniform(-0.1,0.1,input_size)
        self.bias=random.uniform(-0.1,0.1)
        #2.激活函数与导数
        self.activation_function=activation_function
        self.activation_derivative=activation_derivative
        #3.学习率
        self.learn_rate=learn_rate

    def forward(self,input_data):
        '''
        根据已知输入特征数据，进行加权求和与激活函数运算，得到输出。
        :param input_data:              输入的特征数据，必须与构造器指定维数大小一直
        :return:                        返回特征数据计算输出。
        '''
        #1.加权求和运算
        self.input_data=input_data      #后面计算更新梯度要使用
        self.sum=np.dot(self.input_data,self.weights)      #加权求和后面要使用
        self.sum+=self.bias             #偏置项
        #2.激活函数运算
        y=self.activation_function(self.sum)
        self.y=y                        #后面计算更新梯度要使用
        #print("输出:%f"%self.y)
        return  self.y                  #返回计算输出

    def backward(self,expect_output):
        '''
        :param expect_output:           输入特征数据的期望输出值。
        :return:                        无返回值
        '''
        #1.计算每个权重更新相同的部分(delta在这儿是标量)。
        delta=(self.y-expect_output)
        delta=delta*self.activation_derivative(self.sum)
        delta=self.learn_rate * delta   #学习率

        #2.计算每个权重对应的更新梯度（包含偏置项）。
        self.w_delta=np.zeros(self.weights.shape,np.float32)    #向量
        self.b_delta=0

        #偏置项的更新梯度
        self.b_delta=delta      #标量
        #权重的更新梯度
        self.w_delta=delta*self.input_data  #向量（哈马达积）

        #3.更新权重
        self.bias-=self.b_delta
        self.weights-=self.w_delta      #形状相同的向量与矩阵的减法


class Perceptron_Scalar_App:
    '''
    对感知进行训练，需要训练策略参数：
    1.一个需要被训练的感知器
    '''
    def __init__(self,times,input_size,activation_function,activation_derivative,learn_rate):
        '''
        训练策略参数
        :param times:                   训练迭代次数
        下面参数都是传递给感知器对象的
        :param input_size:
        :param activation_function:
        :param activation_derivative:
        :param learn_rate:
        '''
        self.times=times                #训练次数
        #
        self.perceptron=Perceptron_Scalar(input_size,activation_function,activation_derivative,learn_rate)

    def train(self,train_data,train_label):
        '''
        训练过程
        :param train_data:              训练的样本数据
        :param train_label:             训练样本的预期输出
        :return:                        无返回值
        '''
        for t in range(self.times):             #循环训练
            print("第%04d轮训练"%(t+1))
            for idx in range(len(train_data)):  #对每个样本数据训练
                #1.使用感知器对象向前计算结果
                self.perceptron.forward(train_data[idx])
                #2.使用感知器向后更新权重
                self.perceptron.backward(train_label[idx])


    def predict(self,input_data):
        '''
        对输入数据进行分类：
        :param input_data:              需要分类的特征数据
        :return:                        返回计算结果，结果用于分类
        '''
        return self.perceptron.forward(input_data)      #返回训练后的计算结果

import time
start = time.clock()

#1.加载鸢尾花数据
data,target=datasets.load_iris(return_X_y=True)     #第一个返回值是样本数据，第二个返回值是样本的期望标签
#取前面100个眼本测试（这100个是线性可分的）
train_data=data[:100]
label_data=target[:100]     #第一类是0，第二类是1

#2.构建感知器应用对象
#激活函数
activation_function=lambda x:x
#激活函数导数
activation_derivative=lambda x:1
#感知器应用对象
app=Perceptron_Scalar_App(100000,4,activation_function,activation_derivative,0.0000001)

#3.训练感知器
app.train(train_data,label_data)

#4.测试感知器(使用训练样本测试)
correct_counter=0
#前50个期望标签都是0（近似0.5以下都算正确）
for item in train_data[:50]:
    y=app.predict(item)
    if y<0.5:
        correct_counter+=1
#后50个期望标签都是1（近似0.5以上都算正确）
for item in train_data[50:]:
    y=app.predict(item)
    if y>=0.5:
        correct_counter+=1

#打印正确率：
print("正确率：%8.2f"%((correct_counter/100.0)*100))

end=time.clock()
print("CPU运行时间：",end-start)