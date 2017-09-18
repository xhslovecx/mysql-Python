# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 19:32:55 2017

@author: xhs
"""
import urllib
import pymysql
import pandas as pd
from bs4 import BeautifulSoup as bs
import re
from sqlalchemy import create_engine

def getsoup(url):
    headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    data = opener.open(url).read()
    soup=bs(data,'html.parser')
    return soup

#使用python连接数据库
conn = pymysql.connect(
        user = 'root',#一般默认用户名
        passwd = '',#本地数据库登录密码（这里用你自己的密码！！！）
        db = 'mysqldb',#数据库名称（这里用你自己的数据库名称！！！）
        port = 3306,#安装mysql默认的端口号
        host='localhost',#本地地址
        charset = 'utf8'#设置数据库统一编码
)
sql = 'SELECT * FROM `table_id`;'
#将数据库中的数据读入到pandas的二维数组里面
pds = pd.read_sql(sql,conn)
series=pds.id
#解析正则的汉字和数字
com_num=re.compile(r'[0-9]+')
com_chinese=re.compile(r'[\u4e00-\u9fa5]+')
info_DtFrame=pd.DataFrame(columns=['id','sex','age','high','address'])
for j in range(len(series)):   
    temp_str=series.get_value(j)
    temp=[temp_str]
    url='http://love.163.com/'+temp_str
    soup=getsoup(url)
    info=soup.find_all('div',class_='profile-basic-info-left')
    info_str=str(info).split('\n')
    temp=temp+(re.findall(com_chinese,info_str[1]))
    temp=temp+(re.findall(com_num,info_str[2]))
    temp=temp+(re.findall(com_num,info_str[3]))
    temp=temp+(re.findall(com_chinese,info_str[4]))
    info_DtFrame.loc[j]=temp
#因为通过to_sql创建的表字段都是text格式，插入中文时容易造成编码不同而插入失败
#因此，最好采用先建表，并将中文字符的编码统统修改为utf8编码。否则会出错。
#mysql的代理管理软件Navicat软件，设计表里面可以很容易更改编码
#另外，在创建engine时，也要将编码设定为utf8
engine = create_engine("mysql+pymysql://root:@localhost:3306/mysqldb?charset=utf8",encoding='utf-8')
info_DtFrame.to_sql('love_people',engine,if_exists='append',index=False)#,chunksize=1000)    
