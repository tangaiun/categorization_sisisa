import pandas as pd

# CSVファイルを読み込む（エンコーディング指定）
csv_file_path = 'sample/an_clean.csv'
data = pd.read_csv(csv_file_path, encoding='shift-jis')

# カテゴリーと対応するキーワードの辞書を作成
category_keywords = {
    '恋愛関係': ['彼女', '振られ', '親'],
    '友人関係': ['友達', '嫌われ', '嫌い'],
    '職場関係': ['アルバイト', '上司', 'ストレス'],
    # 他のカテゴリーも同様に定義
}

# カテゴリー分けを行う
categorized_data = {category: [] for category in category_keywords}

# for text in data['']:
#     for category, keywords in category_keywords.items():
#         if any(keyword in text for keyword in keywords):
#             categorized_data[category].append(text)
#             break

# 結果を表示
for category, texts in categorized_data.items():
    print(f"Category: {category}")
    for text in texts:
        print(text)
    print()
