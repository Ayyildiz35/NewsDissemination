def count_authors ():
    text = open("outputFiles\posts.txt", encoding="utf8")
    d1 = dict()
    for line in text:
        words = line.split()
        if words:
            if words[0] in "author: ":
                for word in words:
                    if word in d1:
                        d1[word] = d1.get(word, 0) + 1
                    else:
                        d1[word] = 1

    del d1['[deleted]']
    del d1['author:']
    new_keys = [key for key, value in d1.items() if value > 100 ]
    new_values = [value for key, value in d1.items() if value > 100 ]

    d2 = dict()
    i = 0
    for key in new_keys:
        d2[key] = new_values[i]
        i += 1

    g = open("outputFiles\\author.txt", 'w', encoding='utf-8')
    for key, value in d2.items():
        g.write('%s: %s\n' % (key, value))
    g.close()

def check_selfttext ():
    post_to_be_ignored = {"[removed]", "[deleted]"}
    text = open("outputFiles\posts.txt", encoding="utf8")
    d1 = dict()
    for line in text:
        words = line.split()
        if words:
            if words[0] in "selftext: ":
                if len(words) < 2 or words[1] in post_to_be_ignored:
                    continue
                if line.partition(' ')[2] in d1:
                    d1[line.partition(' ')[2]] = d1.get(line.partition(' ')[2], 0) + 1
                else:
                    d1[line.partition(' ')[2]] = 1

    g = open("outputFiles\selftext.txt", 'w', encoding='utf-8')
    for key, value in d1.items():
        g.write('%s: %s\n' % (key, value))
    g.close()

def keyword_frequency_in_selftext ():
    d1 = dict()
    text = open("outputFiles\selftext.txt", encoding="utf8")
    for line in text:
        words = line.split()
        if words:
            for word in words:
                if word in d1:
                    d1[word] = d1.get(word, 0) + 1
                else:
                    d1[word] = 1
    return d1