'''
Created on 2020年1月30日

@author: JM
'''
import pandas as pd
import tushare as ts
from sqlalchemy import create_engine 

engine_ts = create_engine('postgresql://jiedong:ljd_yz2019@49.234.17.178:5432/trade')

def read_data():
    sql = """SELECT * FROM stock_basic LIMIT 20"""
    df = pd.read_sql_query(sql, engine_ts)
    return df


def write_data(df):
    res = df.to_sql('stock_basic', engine_ts, index=False, if_exists='append', chunksize=5000)
    print(res)


def get_data():
    pro = ts.pro_api()
    df = pro.stock_basic()
    return df


if __name__ == '__main__':
#     df = read_data()
    ts.set_token('b63beb8e2d4786e82ad2d2fab50a23809dd58e35d6f562a3a386245c')
    df = get_data()
    write_data(df)
    print(df)