import pandas as pd

#UnicodeDecodeErrorは文字コードを変換する。この変換をエンコーディングという sep='\t'
#csvの読み込み
df = pd.read_csv('an.csv', encoding="shift-jis")
# print(df)
print(df.info())