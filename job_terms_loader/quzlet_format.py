import json
import pandas

with open("files/job_interview_terms_dict.json", 'r') as j:
    dictionary = json.loads(j.read())

quz_dict = []
for i in dictionary:
    for k in i:
        term = i[k]
        for m in term["meanings"]:
            print(f"""  "{term['word']} - {m['partOfSpeech'][:3]}: ({term.get('phonetic', 'N/A')})" ; "{m['definitions'][0]['definition']} EX: {m['definitions'][0].get('example', 'N/A')}"  """)



