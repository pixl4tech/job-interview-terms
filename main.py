
from pickle import load
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import re


raw_text = load(open("raw_text.pkl", 'rb'))
raw_text = re.sub(r'[^\w\s]+', '', raw_text)

text_tokens = nltk.word_tokenize(raw_text)
stopwords = stopwords.words("english")

text_tokens_flt = []
for w in text_tokens:
    if w not in stopwords:
        text_tokens_flt.append(w)

text = nltk.Text(text_tokens_flt)

fdist = FreqDist(text)

top = fdist.most_common(100)
print(top)

