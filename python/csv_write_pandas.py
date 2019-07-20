#csvの読み書きするのに必要
import pandas as pd

# listに文字列を追加
calendar = [['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], ['a', 'b', 'c', 'd', 'e', 'f', 'g']]

# listをdataframe形式に変換(dataframeでないと書き込みできない)
df1 = pd.DataFrame(calendar)

# 画面に出力
print(df1)

 # csvファイルに出力
 # ヘッダー（列名）、インデックス（行名）のありなしは引数header, indexにTrue or Falseで指定する。
df1.to_csv('output/csv_write_pandas_out.csv', header=False, index=False)