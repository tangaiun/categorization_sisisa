import pandas as pd
import MeCab
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# CSVファイルの読み込み
df = pd.read_csv('an.csv', encoding="shift-jis")  # ファイル名は適宜変更してください

# 形態素解析器の初期化
m = MeCab.Tagger()  # MeCabの辞書パスは適宜変更してください

# 名詞の抽出
def extract_nouns(text):
    nouns = []
    node = m.parse(text)
    lines = node.split('\n')
    for line in lines:
        if '\t' not in line:
            continue
        surface, features = line.split('\t')
        if '名詞' in features:
            nouns.append(surface)
    return ' '.join(nouns)

# 名詞の抽出
df['nouns'] = df.apply(extract_nouns)

# ワードクラウドの作成
wordcloud_text = ' '.join(df['nouns'])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(wordcloud_text)

# ワードクラウドの表示
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
