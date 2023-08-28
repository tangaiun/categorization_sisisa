from janome.tokenizer import Tokenizer
import csv

# Janomeの初期化
t = Tokenizer()

# CSVファイルの読み込みと形態素解析
with open('csv/annkert.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        text = row[0]  # CSVファイルの1列目をテキストとして扱う
        tokens = t.tokenize(text)
        for token in tokens:
            surface = token.surface
            part_of_speech = token.part_of_speech
            print("形態素:", surface, "\t品詞:", part_of_speech)