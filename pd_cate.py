import pandas as pd

# CSVファイルを読み込む（エンコーディング指定）
csv_file_path = 'sample/an_clean.csv'
data = pd.read_csv(csv_file_path, encoding='shift-jis')

# データの最初の数行を表示して確認
print(data.head())


# # 実際のカラム名を指定してカテゴリー別にデータを分ける
# # 例: 'Category' というカラム名が存在する場合
# grouped = data.groupby('Category')

# # グループごとにデータを表示
# for group_name, group_data in grouped:
#     print(f"Category: {group_name}")
#     print(group_data)
