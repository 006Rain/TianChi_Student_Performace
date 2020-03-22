import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#读取数据
df = pd.read_csv( './StudentPerformance.csv' )

#查看数据前5行
print( df.head() )

#查看数据形状
print( df.shape )

#查看数据是否存在确实值
print( df.isnull().sum() )

#查看每个特征的数据类型
print( df.dtypes )

#查看每个特征的数据统计值
print( df.describe( include='all' ) )

#查看每个特征的数据的整体信息
print( df.info() )

#举例查看某特征的分类
print( 'Relation: ', df['Relation'].unique() )

#查看结果标签的类别
print( 'Class: ', df['Class'].unique() )

#查看数据集结果是否平衡
plt_fig = plt.figure()
plt.subplots_adjust( hspace = 0.6 )#调整子图间距

plt_fig.add_subplot( 2, 3, 1 )
plt.title( 'y_label Distribution' )
sns.countplot( x='Class', order=['L', 'M', 'H'], data=df )

#数据可视化
#了解性别的分布情况
plt_fig.add_subplot( 2, 3, 2 )
plt.title( 'sex Distribution' )
sns.countplot( x='gender', data=df )

#了解学科的分布情况
sub_plt = plt_fig.add_subplot( 2, 3, 3 )
sns.countplot( x='Topic', data=df )
plt.title( 'Topic Distribution' )
sub_plt.set_xticklabels( df['Topic'].unique(), rotation=90 )

#了解课程和成绩的相关性
sub_plt = plt_fig.add_subplot( 2, 3, 4 )
sns.countplot( x='Topic', hue='Class', hue_order=['L', 'M', 'H'], data=df )
plt.title( 'Topic-Class Correlation' )
sub_plt.set_xticklabels( df['Topic'].unique(), rotation=90 )

#了解性别和成绩的关系
plt_fig.add_subplot( 2, 3, 5 )
plt.title( 'Gender-Class Correlation' )
sns.countplot( x='gender', order=['M', 'F'], hue='Class', hue_order=['L', 'M', 'H'], data=df )

#了解性别和学科的关系
sub_plt = plt_fig.add_subplot( 2, 3, 6 )
sns.countplot( x='Topic', hue='gender', data=df )
sub_plt.set_xticklabels( df['Topic'].unique(), rotation=90 )
plt.title( 'Sex-Topic Correlation' )

#弹窗显示绘制的图
plt.show()