# pythonの絵本p181参照
# 必ず2つのモジュールをインポートする
import requests
from bs4 import BeautifulSoup

print('検索したい本の文字列を入力してください')
str = input() #入力
sach = {}
sach['search'] = str #パラメータを作成
url = 'http://www.shoeisha.co.jp/search'
# params = sach パラメータの設定
# timeout = 1 タイムアウトを1秒に設定
# webページの情報を取得して解析する
req = requests.get(url, params = sach, timeout = 1)
soup = BeautifulSoup(req.text, 'html.parser')

print('\n検索結果：\n')
# classがtextWrapperのdivの内容をすべて取得する
for book in soup.findAll('div', {'class':'textWrapper'}):
    # aの内容を不要なスペース文字を削除したあと出力する
    print(book.find('a').get_text().strip().replace('   ', ''))