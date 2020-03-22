# 天池--学生成绩预测


## 文件
Predict.py: 代码

StudentPerformance.csv: 数据

## 数据集简介: 
该数据集包含了305个男生和175个女生的基本情况和课堂课外表现的量化数据，最终目的是通过这些特征来预测学生的最终学术评测成绩。

## 特征(Features)介绍：
Gender: 性别

Nationality: 国籍

PlaceofBirth：出生地

StageID：学校级别（小学，中学，高中）

GradeID：年级 (G01 - G12)

SectionID: 班级

Topic：学科科目

Semester: 学期 （春学期，秋学期）

Relation: 孩子家庭教育负责人（父亲，母亲）

RaisedHands: 学生该学期上课举手的次数

VisitedResources: 学生浏览在线课件的次数

AnnoucementsView: 学生浏览学校公告的次数

Discussion: 学生参与课堂讨论的次数

ParentAnsweringSurvey: 家长是否填写了关于学校的问卷调查 （是，否）

ParentSchoolSatisfaction: 家长对于学校的满意度 （好，不好）

StudentAbsenceDays: 学生缺勤天数 （大于7天，低于7天）


## 结果(Response Variable)介绍：
Class: 根据学生最后的学术评测分数，学生会被分为3个等级 

Low-Level: 分数区间在0-60 

Middle-Level:分数区间在70-89 

High-Level:分数区间在90-100
