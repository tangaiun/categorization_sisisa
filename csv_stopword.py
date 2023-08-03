from ja_stopword_remover.remover import StopwordRemover
import pprint
import pandas as pd

df = pd.read_csv('an.csv', encoding="shift-jis")

stopwordRemover = StopwordRemover()

text_list = df['text1'].tolist()
text_list_result = stopwordRemover.remove(text_list)

pprint.pprint(text_list_result)

