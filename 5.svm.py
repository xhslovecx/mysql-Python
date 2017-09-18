# -*- coding:cp936 -*-
###################################
#�ֶ���bad.txt �� good.txt�������ں���һ���ˡ�
#
#fit(x_test,y_test),����fit(x,y).fit(x,y)�ǰ�ȫ����������ѵ���ˡ�
#�����Ȼ��fit(x_test,y_test)��̫�ࡣ
#
#######################################################
import time
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.cross_validation import train_test_split
#import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, fbeta_score
#1.׼������
data = np.loadtxt('bad_good.txt', dtype=np.float, delimiter=',')
x, y = np.split(data, (-1, ), axis=1)


#############################################################################
#2.ѵ��������������ݷֿ�
#############################################################################
#****************5�ֲ�ͬ��ѵ�����ı��ʣ��������Ρ�*************************
##############################################################################
'''
test_sizes = [0.5,0.4,0.3,0.2,0.1]
for i in test_sizes:
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = i)
	clf = svm.SVC().fit(x_train, y_train)
	y_hat = clf.predict(x_test)
	print '----------------------------------------'
	print u'��ȷ�ʣ�\t', accuracy_score(y_test, y_hat)
	print u' ���� ��\t', precision_score(y_test, y_hat)
	print u'�ٻ��ʣ�\t', recall_score(y_test, y_hat)
	print u'F1Score��\t', f1_score(y_test, y_hat)
	print '----------------------------------------'

#print u'ʱ�䣺\t',time1-time0,u'��'
########################################################################


############################################################################
#3.���ڷ���ĸ��ֺ˺���
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
	print u'��ȷ�ʣ�\t', accuracy_score(y_test, y_hat)
	print u' ���� ��\t', precision_score(y_test, y_hat)
	print u'�ٻ��ʣ�\t', recall_score(y_test, y_hat)
	print u'F1Score��\t', f1_score(y_test, y_hat)	
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
		print u'��ȷ�ʣ�\t', accuracy_score(y_test, y_hat)
		print u' ���� ��\t', precision_score(y_test, y_hat)
		print u'�ٻ��ʣ�\t', recall_score(y_test, y_hat)
		print u'F1Score��\t', f1_score(y_test, y_hat)
		print '----------------------------------------'
#*************************************************************************************************************
#*************************************************************************************************************
#*************************************************************************************************************

#clf = svm.SVC().fit(x_train, y_train)
#clf = svm.SVC(kernel='sigmoid').fit(x, y)
#clf  = svm.SVC(kernel='poly', degree=3).fit(x, y)
#clf = svm.SVC(kernel='linear').fit(x, y)
#clf= svm.SVC(C=1, kernel='rbf', gamma=0.001,class_weight={-1: 1, 1: 1}).fit(x,y)