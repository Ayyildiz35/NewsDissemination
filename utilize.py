import re
from nltk.corpus import stopwords

def is_key_word_in_subString(key_words, phrase):
    for key_word in key_words:
        if phrase.upper() in key_word.upper():
            return True;
    return False

def merge_substrings_keys(dic, key_words):
    d1 = dict()
    for key_word in key_words:
        for key, value in dic.items():
            if re.search(key_word, key, re.IGNORECASE):
                if key_word in d1:
                    d1[key_word] = d1.get(key_word, 0) + value
                else:
                    d1[key_word] = value
    return d1

def frequency_of_meaningful_words(dic, key_words):
    for key, value in dic.items():
        if is_key_word_in_subString(key_words, key) or not meaningful_word(key) or key == "titel:" or key == "-":
            dic[key] = 0

    newDic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    #sorted(dic.items(), key=operator.itemgetter(1), reverse=True)[:12]
    dict_items = newDic.keys()
    meaningful_word_list = list(dict_items)[:18]
    return meaningful_word_list

def meaningful_word(phrase):
    stop_words = set(stopwords.words('english'))
    #word_tokens = word_tokenize(phrase)
    if not phrase in stop_words:
        return True
    return False