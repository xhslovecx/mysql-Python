import re
import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
from sqlalchemy import create_engine

url = "http://love.163.com/home"
#加入代理服务器，使得爬虫可以像浏览器一样访问页面，使得网页对爬虫不限制
headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
#得到的页面信息，通过beautifulsoup库解析
soup=bs(data,'html.parser')
#将获取到的男女的id放在ls_id里面
ls_id=[]
list_item=soup.find_all('div',class_='login-user-item js-userItem')
compiles=re.compile(r'[0-9]+')
for item in list_item:
    a_label=item.find_all('a',class_="login-user-target")
    str_a=str(a_label)
    ls_id.append(re.findall(compiles,str_a))
df = pd.DataFrame(ls_id,columns=['id'])

engine = create_engine("mysql+pymysql://root:@localhost:3306/mysqldb")
df.to_sql('table_ID',engine,if_exists='append',index=False)
#http://love.163.com/130177803