#coding=utf-8
import numpy as np
import sys
'''
矩阵的基本运算。向量作为特殊的矩阵（行矩阵，列矩阵）
'''
'''
#1.数据表示
#标量数据
scalar=20
#元组列表数据
vector_1=[1,2,3,4]
vector_2=(1,2,3,4)
vector_3=np.array((1,2,3,4))
#2.二维与多维数据
matrix_1=[
    [1,2,3],
    [4,5,6],
    [7,8,9]]
matrix_2=(
    (1,2,3),
    (4,5,6),
    (7,8,9))
matrix_3=(
    (1,2,3),
    (4,5,6),
    [7,8,9])
matrix_4=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])
#2.列表数据运算

print(matrix_4.T)
#print(matrix_1.T)

#3.元组与列表数据运算
truple_1=( 1, 2, 3, 4)  #整数
truple_2=(.1,.2,.3,.4)  #负数

list_1=[ 1, 2, 3, 4]
list_2=[.1,.2,.3,.4]

#元组、列表与标量的运算
#print(5-truple_1)      #不支持+-
#print(list_1+5)        #不支持+-

print(5*truple_1)       #5倍克隆
print(list_1*5)         #5倍克隆

#print(5/truple_1)       #不支持/ //  %   **
#print(list_1**5)        #不支持/ //  %   **

#元组、列表间的运算
print(truple_1+truple_2)#(1, 2, 3, 4, 0.1, 0.2, 0.3, 0.4)
#print(truple_1-truple_2)#不支持
print(truple_1*truple_2)  #不支持
'''

'''
#ndarray类型构造器使用
v=np.ndarray(shape=(3,3),                           #数组的维数大小，矩阵、向量的形状
             dtype=np.int,                        #数组的元素类型
             buffer=np.array((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)),  #数组数据的存放缓冲（字节码格式）
             offset=0,                              #数组数据缓冲的有效开始位置
             strides=(32,24),                        #数组数据缓冲的数据获取步长
             order='F')                             #数组的显示格式，C风格与Fortran风格

print(v)
print()
print(np.int_().itemsize)       #8
print(np.byte().itemsize)       #1
print(np.int8().itemsize)       #1
print(np.int16().itemsize)      #2。
print(np.int32().itemsize)      #4
print(np.int64().itemsize)      #8

m1=np.ndarray(shape=(2,4),
             dtype=np.int,
             buffer=np.array((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)),
             order='F')

print(m1)

m2=np.ndarray(shape=(2,4),
             dtype=np.int,
             buffer=np.array((1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)),
             order='C')
print(m2)


#ndarray对象的构造工具
print("没有初始化的空数组")
m1=np.empty((3,3),np.int_)      #不初始化
print(m1)

print("初始化为0的数组")
m2=np.zeros((3,3),np.int_)      #初始化为0
print(m2)

print("对角矩阵，第三个参数，表示对角开始位置，默认为0")
m3=np.eye(3,4,1,np.int_)        #对角矩阵
print(m3)
'''
'''
m_1_3=np.array((1,2,3))
m_3_4=np.array([
    [1,2,3,4],
    [4,5,6,7],
    [7,8,9,10]
])


#加减
print("加减：")
print(2+m_1_3)
print(2-m_3_4)
#乘法
print("乘法：")
print(2*m_1_3)
print(2*m_3_4)
#除法
print("除法：")
print(2/m_1_3)
print(m_3_4/2)
#整除
print("整除：")
print(2//m_1_3)
print(m_3_4//2)
#幂
print("幂：")
print(2*m_1_3)
print(m_3_4*2)
#求余
print("求余：")
print(2%m_1_3)
print(m_3_4%2)


v1=np.array((1,2,3))            #长度为3的向量
v2=np.array((1,2,3,4,5))        #长度为5的向量

m1=np.array([                   #形状为3*3的矩阵
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
m2=np.array([                   #形状为3*4的矩阵
    [1,2,3,4],
    [4,5,6,7],
    [7,8,9,0]
])


#向量与向量，矩阵与矩阵
print(v1+v1)    #结果[2,4,6]
#print(v1+v2)    #报错：ValueError: operands could not be broadcast together with shapes (3,) (5,)
print("加法：")
print(m1+m1)    #结果[[ 2  4  6]，[ 8 10 12]，[14 16 18]]
#print(m1+m2)    #报错：ValueError: operands could not be broadcast together with shapes (3,3) (3,4)

print("乘法：")
print(m1*m1)
print("除法：")
print(m1/m1)
print("整除：")
print(m1//m1)
print("求余：")
print(m1%m1)
print("幂：")
print(m1**m1)


#内积的定义
A=np.random.uniform(0,1,(3,4))      #构造一个值在[0,1)之间的,形状为3*4的随机矩阵
B=np.random.normal(loc=5,scale=5,size=(4,5))       #构造一个均值为5，值得范围在(-1,1)之间的正态分布随机矩阵
#loc=5概率分布的均值，对应着整个分布的中心center
#scale=5概率分布的标准差，对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高
#size=(4,5)随机矩阵的形状
print("随机矩阵：")
print(A)
print(B)
print("矩阵内积：")
print(np.dot(A,B))
print(A@B)
print(np.matmul(A,B))
'''

#Kronecker积
A=np.array([       #2*3矩阵
    [1,2,3],
    [4,5,6]
])

B=np.array([       #3*2矩阵
    [1,2],
    [3,4],
    [5,6]
])

print(np.kron(A,B))
print(np.kron(B,A))

print(np.outer(A,B))