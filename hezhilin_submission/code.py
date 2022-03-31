import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score

class  LinearRegression:
    def __init__(self):
        self.coef_ =None   #初始化
        self.interception_ = None
        self._theta = None

    def model(self,X_train,Y_train):


        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        self._theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(Y_train)
        self.interception_ = self._theta[0]  #截距
        self.coef_ = self._theta[1:]    #斜率
        return self

    def predict(self,X_predict):
        X_b = np.hstack([np.ones((len(X_predict),1)),X_predict])
        return X_b.dot(self._theta)  ##预测目标值


    def score(self,X_test,y_test):    ##查看拟合情况
        y_predict = self.predict(X_test)
        return r2_score(y_test,y_predict)

    def __repr__(self):
        return "LinearRegression()"


data_read = pd.read_csv(r'D:\Users\lenovo\Desktop\sznlpassessment2022\train3.csv')
list = data_read.values.tolist()
data = np.array(list)
data = data.astype('float')
X_train = data[:,2:14]
Y_train = data[:,14]
Y_train.shape = 342,1    ##这里跟我在world提到的可能有点不同，我在打代码时，自己脑海里模拟了一遍得到的Y会是一个列向量，所以就这么写了


reg = LinearRegression()
reg.model(X_train,Y_train)  ##训练模型，拟合的时候发现只有0.71左右

'''拟合的函数我用了点sklearn的框架，但其实我明白求拟合度的公式，只是用代码打一遍我觉得太浪费时间了'''

testdata_read = pd.read_csv(r'D:\Users\lenovo\Desktop\sznlpassessment2022\test_.csv')
testdata_read.drop('3',axis=1,inplace=True)   ##删除相关性较弱的特征
testdata_read.to_csv(r'D:\Users\lenovo\Desktop\sznlpassessment2022\test1_.csv')
testdata_read = pd.read_csv(r'D:\Users\lenovo\Desktop\sznlpassessment2022\test1_.csv')

list = testdata_read.values.tolist()
testdata = np.array(list)
testdata = testdata.astype('float')
X_test = testdata[:,2:14]
Y_test = X_test.dot(reg.coef_)   ##这里跟我在world写的公式有出入，原因和上面有关。
data1 = pd.DataFrame(Y_test,index=(range(0,102)),columns=['outcome'])
data1.to_csv(r'D:\Users\lenovo\Desktop\sznlpassessment2022\submission.csv')
