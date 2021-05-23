import sys
import tushare as ts
import pandas as pd
import pandas_datareader
import psycopg2

import fix_yahoo_finance as yf

yf.pdr_override() 
try:
    # 打开数据库连接
    conn=psycopg2.connect(database="trade",user="jiedong",password="ljd_yz2019",host="49.234.17.178",port="5432")
except:
    print('Error when Connecting to DB.')   
    sys.exit()
cursor = conn.cursor()

# 从网站爬取数据，并插入到对应的数据表中
def insertStockData(code,startDate,endDate):
    try:
        stock = pandas_datareader.get_data_yahoo(code+'.ss',startDate,endDate)
        if(len(stock)<1):
            stock= pandas_datareader.get_data_yahoo(code+'.sz',startDate,endDate)
        # 删除最后一行，因为get_data_yahoo会多取一天的股票交易数据
        print('Current handle:' + code)
        print(stock)
    except Exception as e:
        print('Error when inserting the data of:' + code)
        print(repr(e))
        conn.rollback()


startDate='2018-08-01'
endDate='2021-05-31'
insertStockData('002127',startDate,endDate)  