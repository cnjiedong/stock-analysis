# coding=utf-8
import urllib.request   # 导入库
stockCode = '600895'    # 待爬取的股票“张江高科”所对应的股票代码
url = 'http://quotes.money.163.com/service/chddata.html?code=0'+stockCode+'&start=20170103&end=20190110&fields=TCLOSE;HIGH;LOW;TOPEN;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER'
print(url)              # 打印出要爬取的url
# 调用urlopen方法爬取数据
response = urllib.request.urlopen(url)
# 由于返回结果中有中文，因此要用gbk解码
print(response.read().decode("gbk"))
response.close();       # 关闭对象s