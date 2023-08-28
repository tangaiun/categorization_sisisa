import MeCab
import csv

def tokenize(text):
    mecab = MeCab.Tagger('-Owakati')  # 分かち書きのみを出力
    result = mecab.parse(text)
    return result.strip()



def process_csv(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile:
        csv_reader = csv.reader(infile)
        next(csv_reader)  # ヘッダ行をスキップ

        with open(output_filename, 'w', encoding='utf-8') as outfile:
            csv_writer = csv.writer(outfile)
            csv_writer.writerow(['Original Text', 'Tokenized Text', 'POS Analysis'])  # ヘッダを書き込む

            for row in csv_reader:
                original_text = row[0]
                tokenized_text = tokenize(original_text)
                # pos_analysis = analyze_pos(original_text)
                # csv_writer.writerow([original_text, tokenized_text, pos_analysis])

if __name__ == "__main__":
    input_csv_file = "csv/annkert.csv"  # 入力CSVファイルのパス
    output_csv_file = "output.csv"  # 出力CSVファイルのパス

    process_csv(input_csv_file, output_csv_file)
