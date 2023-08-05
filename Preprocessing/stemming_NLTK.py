from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer
import nltk
nltk.download('punkt')

def stemming(text):
    
    snowball = SnowballStemmer(language='russian')
    
    list=[]
    for token in word_tokenize(text):
        list.append(snowball.stem(token))
    
    return ' '.join(list)

with open('Text_token_stem_lem.txt', encoding="utf8") as f:
    text=f.read()
print(stemming(text))
