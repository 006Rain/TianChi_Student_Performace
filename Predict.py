import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

#读取数据
df = pd.read_csv( './StudentPerformance.csv' )

#Feature Enginnering 特征工程
X = df.drop( 'Class', axis=1 )
X = pd.get_dummies( X ) #将分类型特征转换成哑变量
Y = df['Class']

#划分训练和数据集
x_train, x_test, y_train, y_test = train_test_split( X, Y, test_size=0.2, random_state=10 )

#训练模型并检测模型准确率
logit = LogisticRegression()
logit.fit( x_train, y_train )
predict = logit.predict( x_test )
print( 'predict.head: ', predict[:5] )
score = logit.score( x_test, y_test )
print( 'score: ', score )

#print打印输出：
#predict.head:  ['H' 'M' 'M' 'L' 'H']
#score:  0.6666666666666666
