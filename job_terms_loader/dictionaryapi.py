import requests
import config
def find_word_service(word: str):
    word_def = requests.get(f"{config.DICTIONARY_API_SERVICE_URL}/{word}")
    if word_def.status_code == 200:
        return word_def.json()[0]
    else:
        return False
