import MeCab
import pandas as pd

# ================================================
# 言語処理
# ================================================

# テキスト
df = pd.read_csv('csv/output2.csv')
# Mecab 形態素解析
tagger = MeCab.Tagger()

print(df)
# 品詞分解
# print(tagger.parse(df))