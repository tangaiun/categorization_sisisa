import csv

# CSVファイルの読み込みと特定のワードの削除
with open('csv/output.csv', 'r', encoding='utf-8') as csvfile, open('csv/output2.csv', 'w', newline='', encoding='utf-8') as outputfile:
    reader = csv.reader(csvfile)
    writer = csv.writer(outputfile)
    
    for row in reader:
        new_row = []  # 新しい行を作成
        for cell in row:
            # 特定のワードを含まないセルの内容を新しい行に追加
            if '助動詞' not in cell:
                new_row.append(cell)
        writer.writerow(new_row)
