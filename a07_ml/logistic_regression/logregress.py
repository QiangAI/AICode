from sklearn.linear_model import *
import numpy as np

cls1_data = np.random.uniform(low=10000, high=100000, size=50)
cls1_result = np.ones(shape=(50,),dtype=np.int32)

cls2_data = np.random.uniform(low=0, high=30000, size=50)
cls2_result = np.zeros(shape=(50,), dtype=np.int32)

x=np.hstack((cls1_data,cls2_data))
y=np.hstack((cls1_result,cls2_result))
x=x.reshape(-1, 1)

# 逻辑回归
logreg = LogisticRegression(C=10e5,max_iter=10000)
logreg.fit(x, y)
print(logreg.coef_)
print(logreg.classes_)
print(logreg.intercept_)
re=logreg.predict_proba(x)

re=logreg.score(x,y)


