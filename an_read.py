import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

#UnicodeDecodeErrorは文字コードを変換する。この変換をエンコーディングという sep='\t'
#csvの読み込み
df = pd.read_csv('sample/an_clean.csv', encoding="shift-jis")
print(df)
# print(df.info())

# # ライブラリのインポート
# import re

# def text_preprocessing(text):
#    # 「]の削除
#    text = text.replace('「','')
#    text = text.replace('」','')

#    # URLの削除
#    text = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', '', text)

#    # pic.twitter.comXXXの削除
#    text = re.sub(r'pic.twitter.com/[\w/:%#\$&\?\(\)~\.=\+\-]+', '', text)

#    # 小文字の変更
#    text = text.lower()

#    return text 