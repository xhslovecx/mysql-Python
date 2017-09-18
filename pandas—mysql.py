import pymysql
import pandas as pd
from sqlalchemy import create_engine
#使用python连接数据库
conn = pymysql.connect(
        user = 'root',#一般默认用户名
        passwd = '',#本地数据库登录密码（这里用你自己的密码！！！）
        db = 'mysqldb',#数据库名称（这里用你自己的数据库名称！！！）
        port = 3306,#安装mysql默认的端口号
        host='localhost',#本地地址
        charset = 'utf8'#设置数据库统一编码
)
sql = 'SELECT * FROM `woman` where id=10003;'
#将数据库中的数据读入到pandas的二维数组里面
pds = pd.read_sql(sql,conn)
print(pds)
#将数据文件导出成csv
#pds.to_csv('E:\goods_info.csv', encoding = 'utf-8', index = False)
engine = create_engine("mysql+pymysql://root:@localhost:3306/mysqldb")
#将DataFrame类型的二维数组的数据存放入数据库里面
pds.to_sql('woman_copy',con=engine,if_exists='replace',index='False')
conn.commit()
conn.close()