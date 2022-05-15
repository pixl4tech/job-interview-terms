
from pickle import load
import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import re
import json
from nltk.stem import WordNetLemmatizer
import pandas as pd
import config
import dictionaryapi

# Read job interviews text from pickle file
raw_text = load(open(r'files/raw_text.pkl', 'rb'))

stopwords = stopwords.words("english")
freq_words = pd.read_csv(r'files/freq_words.csv', delimiter=";")
known_words = pd.read_csv(r'files/known_words.csv', delimiter=";")
sents = load(open('files/sents.pkl', 'rb'))
sentences_df = pd.DataFrame(sents)
sentences_df[1] = ""
find_terms = []
drop_ids = []
terms = []
for index, sentence in sentences_df.iterrows():
    # clearing file from special chars
    raw_text = re.sub(r'[^a-zA-Z\s]', '', sentence[0]).lower()

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
    usual_words = list(map(lambda x: x.replace("'", ""),
                           list(set(
                               list(freq_words[:config.MAX_FREQ_WORDS]["WORD"]) +
                               stopwords +
                               list(known_words["WORD"])
                               + find_terms
                           ))))

    # delete stop words
    text_tokens_flt = list(filter(lambda x: x not in usual_words, text_tokens))
    # get text
    text = nltk.Text(text_tokens_flt)


    # counting word's freq
    fdist = FreqDist(text)
    uniq_words = list(fdist.keys())
    if uniq_words == []:
        continue
    find_terms = list(set(uniq_words + find_terms))
    for t in uniq_words:
        dict_term = dictionaryapi.find_word_service(t)
        if dict_term:
            dict_term["context"] = sentence[0]
            terms.append({t: dict_term})


# write output json
json_object = json.dumps(terms)
with open("files/job_interview_terms_dict.json", "w") as outfile:
    outfile.write(json_object)





