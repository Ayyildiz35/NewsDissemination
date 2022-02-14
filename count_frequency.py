from utilize import is_key_word_in_subString, merge_substrings_keys, frequency_of_meaningful_words


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

    new_keys = [words for words, frequency in d1.items() if frequency > 100 or is_key_word_in_subString(key_words, words)]
    new_values = [frequency for words, frequency in d1.items() if frequency > 100 or is_key_word_in_subString(key_words, words)]

    d2 = dict()
    i = 0
    for key in new_keys:
        d2[key] = new_values[i]
        i += 1

    del d2['title:']

    # we merge similar key words for example covid with covid? or covid with covid:
    d3 = merge_substrings_keys(d2, key_words)
    g = open(frequency_results, 'w', encoding='utf-8')
    for key, value in d3.items():
        g.write('%s: %s\n' % (key, value))
    g.close()

    meaningful_word_list = frequency_of_meaningful_words(d2, key_words)
    g = open(frequency_meaningful_words, 'w', encoding='utf-8')
    for item in meaningful_word_list:
        g.write('%s\n' % (item))
    g.close()

    return d3