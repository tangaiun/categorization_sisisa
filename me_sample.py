

import MeCab
wakati = MeCab.Tagger("-Owakati")
print(wakati.parse("pythonが大好きです").split())

import MeCab

# MeCabの初期化
mecab = MeCab.Tagger("-Owakati")  # 分かち書きの形式で解析

# 解析するテキスト
text = "こんにちは、私の名前はChatGPTです。"

# テキストを形態素解析して分かち書きを得る
parsed_text = mecab.parse(text)
print(parsed_text)