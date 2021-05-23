# !/usr/bin/env python
# coding=utf-8
import pymysql
import sys
import tushare as ts
try:
    # 打开数据库连接
    db = pymysql.connect("localhost","root","123456","pythonStock" )
except:
    print('Error when Connecting to DB.')   
    sys.exit()
cursor = db.cursor()     
'''
stockList=['600895','603982','300097','603505','600759']
for code in stockList:
    try:
        createSql= 'CREATE TABLE stock_' +code+' (  date varchar(255) ,open float,close float ,high float , low float,vol int(11))'        
        cursor.execute(createSql)
    except:
        print('Error when Creating table for:' + code)
'''            
stockList=ts.get_stock_basics()  # 通过tushare接口获取股票代码
for code in stockList.index:
    try:
        createSql= 'CREATE TABLE stock_' +code+' (  date varchar(255) ,open float,close float ,high float , low float,vol int(11))'
        print(createSql)
        cursor.execute(createSql)
    except:
        print('Error when Creating table for:' + code)                
db.commit()
cursor.close()
db.close()