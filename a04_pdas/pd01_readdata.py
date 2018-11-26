#!/usr/bin/python
# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
'''
pandas从文件读取数据：
1.CSV文本文件
    |-read_csv	
        |-usecols 指定读取的哪些列（ 数据类型：list（索引构成的列表） ）
        |-nrows 指定读取的行数（整数类型）
    |-to_csv
2.JSON文本文件	
    |-read_json	
    |-to_json
3. HTML文本文件	
    |-read_html	
    |-to_html
4.本地粘贴板文本数据
    |-read_clipboard	
    |-to_clipboard
5.Office应用的Excel文件	
    |-read_excel	
    |-to_excel
6.HDF5数据	
    |-read_hdf	
    |-to_hdf
7.其他数据格式
    二进制特征数据格式
        |-read_feather	
        |-to_feather
    Parquet格式	
        |-read_parquet	
        |-to_parquet
    Msgpack格式
        |-read_msgpack	
        |-to_msgpack
    Stata格式
        |-read_stata	
        |-to_stata
    SAS格式
        |-read_sas	 
    Python Pickle格式	
        |-read_pickle	
        |-to_pickle
    SQL数据库格式	
        |-read_sql	
        |-to_sql
    SQL	Google Big Query	
        |-read_gbq	
        |-to_gbq
'''
# usecols 读取的列
data = pd.read_csv('jobs.csv')
data.dropna()
salary = data['薪水']
print(len(salary))
data1 = data.drop(['薪水'], axis=1)
low = [float(v.replace('k', '000').split('-')[0]) for v in salary]
upper = [float(v.replace('k', '000').split('-')[1]) for v in salary]
data1['最高'] = upper
data1['最低'] = low

dd=data1[['工作年限', '城市', '最高', '最低']].groupby(['工作年限','城市'])
df=dd.mean()
df.plot()
plt.show()