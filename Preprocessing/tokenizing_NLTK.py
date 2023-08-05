import nltk
file_content = open("Text_token_stem_lem.txt", encoding="utf8").read()
tokens = nltk.word_tokenize(file_content)
print(tokens)
