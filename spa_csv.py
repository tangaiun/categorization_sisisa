# coding: utf-8
import spacy
nlp = spacy.load('ja_ginza_nopn')
import pandas as pd
import matplotlib.pyplot as plt
import collections
from wordcloud import WordCloud

def ginza(word):
    doc = nlp(word)
    # 調査結果
    total_ls = []
    Noun_ls = [chunk.text for chunk in doc.noun_chunks]
    Verm_ls = [token.lemma_ for token in doc if token.pos_ == "VERB"]
    for n in Noun_ls:
        total_ls.append(n)
    for v in Verm_ls:
        total_ls.append(v)
    return total_ls, Noun_ls, Verm_ls


"""---------------     CSV読み込みと前セット     --------------"""
csv_read_path = "list.csv"
df = pd.read_csv(csv_read_path)

target_categories = ["歌詞"]
black_list = ["test"]
"""-------------------------------------------------------------"""



"""---------------      形態素の処理------------------------"""
for target in target_categories:
    total_voc = []#文字を入れる箱を用意
    for data in df[target]:
        try:
            word_ls, noun_ls, verm_ls = ginza(data)
        except:#もし、分解できない場合は、一単語とする。
            word_ls = [data]
        for w in word_ls:
            if not w in black_list:#その単語がブラックリストに入っていないかチェックする。
                total_voc.append(w)

    print("単語数は、", len(total_voc), "でした。")

    # 最頻単語を順位づけ
    c = collections.Counter(total_voc)

    # CSVに書き込む
    c_data = (c.most_common())
    csvdf = pd.DataFrame(c_data)
    filename = target + ".csv"
    csvdf.to_csv(filename, encoding='utf_8_sig')
    print("----------------------------")

    # 一応グラフ化する
    # 追加部分 フォントを指定する。
    plt.rcParams["font.family"] = "IPAexGothic"
    plt.title(target)
    plt.grid(True)
    graph_x_list = []
    graph_y_list = []
    top_num = 0
    for key, value in c.most_common():
        graph_x_list.append(key)
        graph_y_list.append(value)
        if top_num >= 10:
            break
        top_num += 1
    try:
        plt.bar(graph_x_list, graph_y_list)
        # グラフの表示
        plt.show()
    except:
        print(target, " に関して、データを描画できませんでした。")

    # WordCloud で描画する
    font = 'C:/Windows/Fonts/YuGothM.ttc'
    wordcloud = WordCloud(background_color="white", width=1000, height=600, font_path=font)

    wordcloud.generate(" ".join(wordcloud_ls))
    wordcloud.to_file(target+'.png')

"""-------------------------------------------------------------"""

