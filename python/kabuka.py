#日経平均平均株価
nikkei_heikin = ""

#①インポートします。
import requests
from bs4 import BeautifulSoup

#②HTMLを取得します。
#url = 'https://www.nikkei.com/'
url = 'https://stocks.finance.yahoo.co.jp/stocks/detail/?code=6506.T'
html = requests.get(url)

#③HTMLパース用のオブジェクトを作成します。
soup = BeautifulSoup(html.text,"html.parser")

#④「td」要素全て抽出します。
td = soup.find_all("td")

#⑤「td」要素をループします。
for tag in td:
    try:
        #⑥「td」要素から「class」をpopしていきます。
        string_ = tag.get("class").pop(0)
        #⑦摘出したclassの文字列にm-miH01C_rateが設定されているかチェックします。
        if string_ in "stoksPrice":
            #⑧tagの文字列(日経平均株価)を取得します。
            # nikkei_heikin = tag.string
            td_tag = tag.select_one('table[class="stocksTable"] > tbody > tr > td[class="stoksPrice"]')
            nikkei_heikin = td_tag.string
            #⑨ループ処理を中断します。
            break
    except:
        #⑥'「span」要素から「class」をpopできなかった場合何もしません。
        pass

#⓾取得した日経平均株価を出力します。
print(nikkei_heikin)