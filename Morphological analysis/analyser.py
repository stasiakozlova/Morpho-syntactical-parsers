import json
from pymystem3 import Mystem

text = open("Text 3.txt", encoding = 'UTF-8')
file = text.read()
m = Mystem()
lemmas = m.lemmatize(file)
print ("lemmas:", ''.join(lemmas))
print ("full info:", json.dumps(m.analyze(file), ensure_ascii=False))
