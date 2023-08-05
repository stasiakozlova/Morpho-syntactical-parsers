from textblob import TextBlob
file_content = open("Text_token_stem_lem.txt", encoding="utf8").read()
file = TextBlob(file_content)
tokens = file.words
print(tokens)
