import collections
import MeCab
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns
sns.set(font='Hiragino Sans')

f= open('an.csv', 'r', encoding="shift-jis")
text=f.read()
f.close()
tagger =MeCab.Tagger()
tagger.parse('')
node = tagger.parseToNode(text)

word_list=[]
while node:
    word_type = node.feature.split(',')[0]
    if word_type in ["名詞",'代名詞']:
        word_list.append(node.surface)
    node=node.next
word_chain=' '.join(word_list)