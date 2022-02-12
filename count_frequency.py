import re
from nltk.corpus import stopwords

def count_words(key_words, text_file, frequency_results, frequency_meaningful_words):
    text = open(text_file, encoding="utf8")
    d1 = dict()
    for line in text:
        words = line.split()
        if words:
            if words[0] in "title: ":
                for word in words:
                    if word in d1:
                        d1[word] = d1.get(word, 0) + 1
                    else:
                        d1[word] = 1

    d2 = dict()
    new_keys = [frequency for words, frequency in d1.items() if frequency > 100 or is_key_word_in_subString(key_words, words)]
    new_values = [words for words, frequency in d1.items() if frequency > 100 or is_key_word_in_subString(key_words, words)]

    i = 0
    for key in new_keys:
        d2[key] = new_values[i]
        i += 1

    # we merge similar key words for example covid with covid? or covid with covid:
    d3 = merge_substrings_keys(d2, key_words)
    g = open(frequency_results, 'w', encoding='utf-8')
    for key, value in d3.items():
        g.write('%s:%s\n' % (key, value))
    g.close()

    # reverse key and value in d2
    d5 = dict()
    for key, value in d2.items():
        d5[value] = key

    meaningful_word_list = frequency_of_meaningful_words(d5, key_words)
    g = open(frequency_meaningful_words, 'w', encoding='utf-8')
    for item in meaningful_word_list:
        g.write('%s\n' % (item))
    g.close()

    return d3

def is_key_word_in_subString(key_words, phrase):
    for word in key_words:
        if re.search(phrase, word, re.IGNORECASE):
            return True
    return False

def merge_substrings_keys(dic, key_words):
    d1 = dict()
    for key_word in key_words:
        for key, value in dic.items():
            if re.search(key_word, value, re.IGNORECASE):
            #if key_word in value:
                if key_word in d1:
                    d1[key_word] = d1.get(key_word, 0) + key
                else:
                    d1[key_word] = key
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
    else: return False
