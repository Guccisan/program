#csvの読み書きするのに必要
import pandas as pd

# df = pd.read_csv('input/input.csv', index_col=0)
# df.to_csv('to_csv_out.csv')
# print(df)

# listに文字列を追加
calendar = [['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], ['a', 'b', 'c', 'd', 'e', 'f', 'g']]

# listをdataframe形式に変換(dataframeでないと書き込みできない)
df1 = pd.DataFrame(calendar)

# 画面に出力
print(df1)

 # csvファイルに出力
 # ヘッダー（列名）、インデックス（行名）のありなしは引数header, indexにTrue or Falseで指定する。
df1.to_csv('to_csv_out1.csv', header=False, index=False)