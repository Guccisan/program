# ファナックの株価を取得する
# 必ず２つのモジュールをインポートすること
import requests
from bs4 import BeautifulSoup

# FANUCの株価のURL
url = 'https://www.nikkei.com/nkd/company/?scode=6954' 

# webページの情報を取得して、解析する
req = requests.get(url) 
soup = BeautifulSoup(req.text, 'html.parser')

#会社名を取得
company = soup.find('h1', {'class':'m-headlineLarge_text'})

# <dd class="m-stockPriceElm_value now"> ...<span class="m-stockPriceElm_value_unit">...</span></dd> を抽出
# 株価を取得
book = soup.find('dd', {'class':'m-stockPriceElm_value now'})

# 不要な部分<span class="m-stockPriceElm_value_unit">...</span>を削除
for rt in book.findAll("span", {'class':'m-stockPriceElm_value_unit'}):
    rt.extract()

# タグを削除して出力
print("Company" + ":" + "Stockprice")
print(company.text + ':' + book.text)
