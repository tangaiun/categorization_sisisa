import pandas as pd
import MeCab

# CSVファイルの読み込み
csv_file = 'csv/annkert.csv'  # 適切なファイルパスに置き換えてください
data = pd.read_csv(csv_file, encoding='utf-8')

# MeCabの初期化
mecab = MeCab.Tagger("-Owakati")  # 分かち書きのみを出力する設定

# 分かち書きを実行
wakati_text = mecab.parse(data).strip()

print("分かち書き:", wakati_text)

# 品詞分解を実行
node = mecab.parseToNode(data)
while node:
    if node.feature.split(',')[0] != 'BOS/EOS':
        print("表層形:", node.surface, "\t品詞:", node.feature.split(',')[0])
    node = node.next