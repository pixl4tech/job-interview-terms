
from pickle import load
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import re
import csv, json
from nltk.stem import WordNetLemmatizer

# TODO: Create config file

# CONFIG
MAX_FREQ_WORDS = 300

# Read job interviews text from pickle file
raw_text = load(open("raw_text.pkl", 'rb'))
# clearing file from special chars
raw_text = re.sub(r'[^a-zA-Z\s]', '', raw_text).lower()

# get tokens
text_tokens = nltk.word_tokenize(raw_text)
# transform words to right form (single, present form etc)
wnl = WordNetLemmatizer()
text_tokens = list(map(lambda x: wnl.lemmatize(x, 'n'), text_tokens))
text_tokens = list(map(lambda x: wnl.lemmatize(x, 'v'), text_tokens))
text_tokens = list(map(lambda x: wnl.lemmatize(x, 'a'), text_tokens))
text_tokens = list(map(lambda x: wnl.lemmatize(x, 'r'), text_tokens))
text_tokens = list(map(lambda x: wnl.lemmatize(x, 's'), text_tokens))

# find stop words
stopwords = stopwords.words("english")
freq_words = []
with open('freq_words.csv') as File:
    reader = csv.reader(File, delimiter=';')
    for row in reader:
        freq_words.append(row[1].strip())

# todo: move to incorrect words csv file
extends = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'le', 'cant', 'p', 'i', 'u', 'ill', 'abc', 'age', 'ago', 'wa', 'ha', 'bos', 'five', 'within', 'four', 'six', 'ididnt', 'lot', 'anywhere', 'one', 'ive', 'im', 'years', 'id', 'worked', 'working', 'first', 'two', 'three', 'thats', 'better', 'done', 'projects', 'hours', 'alot', 'best', 'ideas']
usual_words = list(map(lambda x: x.replace("'", ""), list(set(freq_words[:MAX_FREQ_WORDS] + stopwords + extends))))

# delete stop words
text_tokens_flt = list(filter(lambda x: x not in usual_words, text_tokens))
# get text
text = nltk.Text(text_tokens_flt)

# counting word's freq
fdist = FreqDist(text)
top = fdist.most_common()
print(top)

# write output json
json_object = json.dumps(top)
with open("top_job_interview_words.json", "w") as outfile:
    outfile.write(json_object)

