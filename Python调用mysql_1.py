# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:12:16 2017
@author: xhs
#Python连接mysql数据库的简单使用
"""

#!/bin/env Python  
# -*- coding:utf-8 -*-  
import pymysql  

conn = pymysql.connect(  
    user="root",  
    password="",  
    port=3306,  
    host="localhost",   #本地数据库  等同于localhost  
    db="mysqldb",  
    charset="utf8"  
)
cur=conn.cursor() #获取对应的操作游标  
#information=a[id,name,sex,age,high,salary,vocation]
temp=[]
#temp=[3456,'xhs','女',26,160,10000,'计算机']
#在数据库中插入一条数据
sql="insert into woman(id,name,sex,age,high,salary,vocation)values(10006,'xcx','男',26,180,10000,'计算机')"
cur.execute(sql)
##在数据库中插入多条数据
sqls="insert into woman values(%s,%s,%s,%s,%s,%s,%s)"
cur.executemany(sqls,[
        (100010,'xcx','男',26,180,10000,'计算机')
        ,(100011,'马明明','女',26,159,10000,'计算机')
        ,(100012,'陈欣','男',26,178,10000,'计算机')
        ])
#输出查询的元组个数
sql2='select * from woman'
print(cur.execute(sql2))
#删除和插入一条记录
cur.execute("delete from woman where id=100010")
cur.execute("update woman set name='曹伟华' where id=10007")
#关闭游标
cur.close()
#conn.commit()方法在提交事物，在向数据库插入一条数据时必须要有这个方法，否则数据不会被真正的插入。
conn.commit()
#关闭数据库连接
conn.close()