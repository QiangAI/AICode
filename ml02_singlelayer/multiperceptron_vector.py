#coding=utf-8
import numpy as np
from sklearn import  datasets
class Layer:
    def __init__(self,input_size,output_size,activity_funtion,derivative_function,learning_rate):
        '''
        初始虎与感知器层有关的数据。
        :param input_size:          输入的特征数据的长度
        :param output_size:         输出的特征数据的长度（就是感知器个数）
        :param activity_funtion:    激活函数
        :param derivative_function: 激活函数的导数
        :param learning_rate:       学习率
        '''
        self.input_size=input_size
        self.output_size=output_size
        #初始化一个随机权重矩阵，矩阵的每行对应一个感知器的权重向量，output_size对应感知器的个数
        self.weights=np.matrix(np.random.uniform(-0.1,0.1,(self.output_size,self.input_size)))
        #加权求和的偏置项(列向量：使用矩阵表示)
        self.bias=np.matrix(np.random.uniform(-0.1,0.1,(self.output_size,1))).T
        #激活函数
        self.activity_funtion=activity_funtion
        #激活函数的导数函数
        self.derivative_function=derivative_function
        #学习率
        self.learning_rate=learning_rate

    def forward(self,input_data):
        '''
        感知器层的输出计算。
        :param input_data:          输入的特征数据
        :return:                    返回感知器的输出
        '''
        self.input_data=input_data
        #计算加权求和（矩阵内积）
        self.weights_sum=self.weights @ self.input_data.T
        #+偏置项（矩阵加法运算）
        self.weights_sum=self.weights_sum + self.bias.T
        #激活函数运算
        self.out_data=self.activity_funtion( self.weights_sum )
        #返回结果(结果是长度为self.output_size的矩阵)
        return self.out_data.T

    def backward(self,delta):
        '''
        根据误差项计算，计算梯度，并使用梯度更新权重
        :param delta:               误差项（根据训练样本的期望标签计算）
        '''
        #计算梯度：梯度=学习率 * 误差项 ● 特征数据
        self.grads = delta.T @ self.input_data
        self.grads *= self.learning_rate
        #更新权重矩阵
        self.weights -= self.grads


class ANN:
    def __init__(self,layers_param):
        '''
        初始化与感知器层有关的参数
        :param layers_param:        所有层感知器相关的参数，使用数组表示一层多个参数
        '''
        self.layers_param=layers_param
        #构造一个感知器层
        self.layer=Layer(layers_param['input_size'],
                         layers_param['output_size'],
                         layers_param['activity_funtion'],
                         layers_param['derivative_function'],
                         layers_param['learning_rate']);

    def forward(self,sample_data):
        '''
        神经网络的输出计算
        :param sample_data:         训练或者测试样本特征数据
        :return:                    返回整个神经网络的输出
        '''
        self.y=self.layer.forward(sample_data)
        return self.y

    def backward(self,label):
        '''
        反向更新权重
        :param label:               与神经网络输入训练样本对应的期望输出标签
        '''
        #根据输出与期望标签，计算误差项（这里损失函数还是采用差平方）。
        #计算输出与期望标签的差
        diff=self.y.T-label.T
        #乘以导数
        delta=diff * self.layers_param['derivative_function'](self.layer.weights_sum)
        #调用感知器层，更新感知器的权重
        self.layer.backward(delta.T)


class ANNApp:
    def __init__(self,ann_param,times):
        '''
        初始化与神经网络的有关的参数
        :param ann_param:           所有神经网络有关的参数
        :param times:               训练次数
        '''
        self.times=times
        #构造一个神经网络
        self.ann=ANN(ann_param)

    def predict(self,sample_data):
        '''
        根据样本数据，计算神经网络输出
        :param sample_data:
        :return:
        '''
        return self.ann.forward(sample_data)

    def train(self,train_dataset,label_dataset):
        #循环训练次数
        for n in range(self.times):
            print("第%d轮训练"%(n+1))
            #循环训练样本，计算输出，并跟新梯度
            for i in range(len(train_dataset)):
                sample_data=train_dataset[i]
                #计算输出
                self.ann.forward(sample_data)
                #更新权重
                label=label_dataset[i]
                self.ann.backward(label)


PERCEPTRON_SIZE=2
#1.加载数据
data,target=datasets.load_iris(return_X_y=True)
#把期望标签转换为向量
target_num=len(target[:100])
arr_labels=np.zeros((target_num,PERCEPTRON_SIZE))
for i in  range(target_num):
    idx=target[i]
    arr_labels[i][idx]=1

#把数据集转换为矩阵
label_dataset=np.matrix(arr_labels)
train_dataset=np.matrix(data[0:100])
#2.初始化训练相关的参数
times=1000
ann_param={
    'input_size':4,
    'output_size':2,
    'activity_funtion':lambda x:x,
    'derivative_function':lambda x:1,
    'learning_rate':0.0001
}
#3.创建神经网络应用对象
app=ANNApp(ann_param,times)
#4.使用训练样本进行神经网络训练
app.train(train_dataset,label_dataset)
#5.使用测试样本测试训练结果
counter=0
for i in range(target_num):
    #计算预测输出
    y=app.predict(train_dataset[i])
    print(y)
    #判定分类是否正确
    if(y.argmax()==label_dataset[i].argmax()):
        counter+=1

print("准确率：%8.2f"%(100.0*counter/100))

