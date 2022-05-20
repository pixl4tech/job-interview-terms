import json
import pymongo
import pandas

with open("files/job_interview_terms_dict.json", 'r') as j:
    dictionary = json.loads(j.read())

term_list = []
for term in dictionary:
    term_name = term[list(term.keys())[0]].pop("word")
    term_obj = dict(name=term_name, dictionary=term[term_name], likes=0, dislikes=0, views=0)
    term_list.append(term_obj)

print("Transform done.")

json_object = json.dumps(term_list)
with open("files/terms_mongo_dump.json", "w") as outfile:
    outfile.write(json_object)

# todo: url to config
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient.jobTerm
term_collection = db.term

term_collection.delete_many({})
term_collection.insert_many(term_list)

print("Load done.")

