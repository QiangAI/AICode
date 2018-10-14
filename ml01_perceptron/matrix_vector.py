#coding=utf-8
import  numpy as np
#矩阵与向量的内积
weights=np.random.uniform(-0.1,0.1,size=4)
input_data=np.array([4.7,3.2,1.3,0.2])  #来自iris数据集
sum=0

#标量计算方式
for idx in range(len(input_data)):
    sum += weights[idx] * input_data[idx]

print(sum)
#矩阵与向量的内积计算方式
sum=np.dot(weights,input_data)
print(sum)

sum=np.dot(input_data,weights)
print(sum)
print()

#1维向量的内积与矩阵在数据格式上有差别
v=np.array([1,2,3,4])
m=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,8,7,6],
    [5,4,3,2]
])

print(np.dot(v,m))  #v作为行向量使用
print(np.dot(m,v))  #v作为列向量使用

