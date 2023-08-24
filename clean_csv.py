#csvファイルをテキストクリーニング
import csv

# csvファイルにある\tを除去
def remove_tabs(input_file, output_file):
    with open(input_file, encoding="shift-jis") as infile, \
            open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            cleaned_row = [cell.replace('\t', '') for cell in row]
            cleaned_row2 = [cell.replace('NaN', '') for cell in row]
            writer.writerow(cleaned_row)
            writer.writerow(cleaned_row2)

if __name__ == "__main__":
    input_file = "an.csv"  # 元のCSVファイル名を指定
    output_file = "an_clean.csv"  # クリーニングした結果を書き込むCSVファイル名を指定
    remove_tabs(input_file, output_file)
