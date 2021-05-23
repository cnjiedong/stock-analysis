# !/usr/bin/env python
# coding=utf-8
import pymysql
import sys
import tushare as ts
import pandas as pd
import pandas_datareader
try:
    # 打开数据库连接
    db = pymysql.connect("localhost","root","123456","pythonStock" )
except:
    print('Error when Connecting to DB.')   
    sys.exit()
cursor = db.cursor()
# 从网站爬取数据，并插入到对应的数据表中
def insertStockData(code,startDate,endDate):
    try:
        filename='D:\\stockData\ch8\\'+code+startDate+endDate+'.csv'
        stock = pandas_datareader.get_data_yahoo(code+'.ss',startDate,endDate)
        if(len(stock)<1):
            stock= pandas_datareader.get_data_yahoo(code+'.sz',startDate,endDate)
        # 删除最后一行，因为get_data_yahoo会多取一天的股票交易数据
        stock.drop(stock.index[len(stock)-1],inplace=True)        # 在本地留份csv
        print('Current handle:' + code)
        stock.to_csv(filename)
        df = pd.read_csv(filename,encoding='gbk')
        cnt=0
        while cnt<=len(df)-1:
            date=df.iloc[cnt]['Date']
            open=df.iloc[cnt]['Open']
            close=df.iloc[cnt]['Close']
            high=df.iloc[cnt]['High']
            low=df.iloc[cnt]['Low']
            vol=df.iloc[cnt]['Volume']
            tableName='stock_'+code
            values = [date,float(open),float(close),float(high),float(low),int(vol)]
            insertSql='insert into '+tableName+' (date,open,close,high,low,vol) values (%s,%s,%s,%s,%s,%s)'
            cursor.execute(insertSql, values)
            cnt=cnt+1
        db.commit()   
    except Exception as e:
        print('Error when inserting the data of:' + code)
        print(repr(e))
        db.rollback()
startDate='2018-08-01'
endDate='2019-05-31'
stockList=['600460']
for code in stockList:
    insertStockData(code,startDate,endDate)     
'''            
stockList=ts.get_stock_basics()  # 通过tushare接口获取股票代码
for code in stockList.index:
    insertStockData(code,startDate,endDate)            
'''
cursor.close()
db.close()