import MeCab

# 形態素解析のパーサーの設定
tagger = MeCab.Tagger("-wakati")

# 例文
test_string = '「すもも」もももももものうち'

# 形態素解析
print(tagger.parse(test_string))