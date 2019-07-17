# ２つのモジュールをインポート
import requests
from bs4 import BeautifulSoup

print('検索したい本の文字列を入力してください')
str = input() # ユーザーからの入力
sach = {}
sach['search'] = str # パラメータを作成
url = 'https://www.shoeisha.co.jp/search'
# params = sach パラメータを設定
# timeout = 1 タイムアウトを1秒に設定
req = requests.get(url, params = sach, timeout = 1) # webページの情報を取得して、解析する
soup = BeautifulSoup(req.text, 'html.parser')

print('検索結果')
for book in soup.findAll('div', {'class':'textWrapper'}):
    print(book.find('a').get_text().strip().replace('    ',''))