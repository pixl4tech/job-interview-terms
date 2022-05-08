
from pickle import load
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import re
import csv


raw_text = load(open("raw_text.pkl", 'rb'))
raw_text = re.sub(r'[^\w\s]+', '', raw_text).lower()

text_tokens = nltk.word_tokenize(raw_text)
stopwords = stopwords.words("english")

freq_words = []
with open('freq_words.csv') as File:
    reader = csv.reader(File, delimiter=';')
    for row in reader:
        freq_words.append(row[1].strip())

usual_words = list(map(lambda x: x.replace("'", ""), list(set(freq_words[:150] + stopwords))))

print(usual_words)



text_tokens_flt = []
for w in text_tokens:
    if w not in usual_words:
        text_tokens_flt.append(w)

text = nltk.Text(text_tokens_flt)

fdist = FreqDist(text)

top = fdist.most_common(100)
print(top)

