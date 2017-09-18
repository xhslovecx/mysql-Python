# -*- coding:cp936 -*-
###################################
#手动把bad.txt 和 good.txt的内容融合在一起了。
#
#fit(x_test,y_test),不是fit(x,y).fit(x,y)是把全集都拿来做训练了。
#结果当然比fit(x_test,y_test)好太多。
#
#######################################################
import time
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.cross_validation import train_test_split
#import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, fbeta_score
#1.准备数据
data = np.loadtxt('bad_good.txt', dtype=np.float, delimiter=',')
x, y = np.split(data, (-1, ), axis=1)


#############################################################################
#2.训练数据与测试数据分开
#############################################################################
#****************5种不同的训练集的比率，看结果如何。*************************
##############################################################################
'''
test_sizes = [0.5,0.4,0.3,0.2,0.1]
for i in test_sizes:
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = i)
	clf = svm.SVC().fit(x_train, y_train)
	y_hat = clf.predict(x_test)
	print '----------------------------------------'
	print u'正确率：\t', accuracy_score(y_test, y_hat)
	print u' 精度 ：\t', precision_score(y_test, y_hat)
	print u'召回率：\t', recall_score(y_test, y_hat)
	print u'F1Score：\t', f1_score(y_test, y_hat)
	print '----------------------------------------'

#print u'时间：\t',time1-time0,u'秒'
########################################################################


############################################################################
#3.用于分类的各种核函数
############################################################################
'''
'''
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
clf_rbf     = svm.SVC()
clf_linear  = svm.SVC(kernel='linear')
#clf_linear  = svm.LinearSVC()
clf_poly    = svm.SVC(kernel='poly', degree=3)
clf_sigmoid = svm.SVC(kernel='sigmoid')
model = [clf_rbf,clf_linear,clf_poly,clf_sigmoid]
for i in model:
	clf = i.fit(x_train,y_train)
	y_hat=clf.predict(x_test)
	print '----------------------------------------'
	print u'正确率：\t', accuracy_score(y_test, y_hat)
	print u' 精度 ：\t', precision_score(y_test, y_hat)
	print u'召回率：\t', recall_score(y_test, y_hat)
	print u'F1Score：\t', f1_score(y_test, y_hat)	
	print '----------------------------------------'	

#############################################################################
#############################################################################
#############################################################################



#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************
'''
#default setup:
#######################################
C_values = range(1,10,1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)
#gamma_values = np.arange(0.001,0.1,0.001)
for i in C_values:
	#for j in gamma_values:
		clf = svm.SVC(C=i,gamma=0.05,class_weight={-1: 1.5, 1: 1}).fit(x_train,y_train)
		y_hat = clf.predict(x_test)
		print '----------------------------------------'
		print u'正确率：\t', accuracy_score(y_test, y_hat)
		print u' 精度 ：\t', precision_score(y_test, y_hat)
		print u'召回率：\t', recall_score(y_test, y_hat)
		print u'F1Score：\t', f1_score(y_test, y_hat)
		print '----------------------------------------'
#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************

#clf = svm.SVC().fit(x_train, y_train)
#clf = svm.SVC(kernel='sigmoid').fit(x, y)
#clf  = svm.SVC(kernel='poly', degree=3).fit(x, y)
#clf = svm.SVC(kernel='linear').fit(x, y)
#clf= svm.SVC(C=1, kernel='rbf', gamma=0.001,class_weight={-1: 1, 1: 1}).fit(x,y)