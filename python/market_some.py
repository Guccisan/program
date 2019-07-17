# ファナックの株価を取得する
# 必ず２つのモジュールをインポートすること
import requests
from bs4 import BeautifulSoup
# csvの読み書きするのに必要
import pandas as pd
# 文字列の正規表現
import re
# sleep
import time

# リストの初期化
l = []
l.append(["Company", "Stock price"])
stock_num = [6954, 6506, 6141, 7751, 8035, 9022]

#リストの個数を取得
num = len(stock_num)

# FANUCの株価のURL
url = 'https://www.nikkei.com/nkd/company/?scode=6954' 

print("Company" + ":" + "Stock price")


for i in range(num):
    # 10秒待機
    time.sleep(5)

    # 数字を削除して文字を追加
    # re.sub(正規表現パターン, 置換後文字列, 置換したい文字列)
    # \d : 10進数の任意の数字。
    url = re.sub(r"\d", "", url)
    url = url + str(stock_num[i])
    # print("URL:" + url)

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
    print(company.text + ':' + book.text)

    # listに会社名と業種と株価を追加
    l.append([company.text, book.text])


# listをdataframe形式に変換(dataframeでないと書き込みできない)
df = pd.DataFrame(l)

# csvファイルに出力
# ヘッダー（列名）、インデックス（行名）のありなしは引数header, indexにTrue or Falseで指定する。
# encodingで文字コードを指定
df.to_csv('output/csv_market_some.csv', header=False, index=False, encoding="shift_jis")
