import zstandard as zstd
import json
import time
from datetime import datetime

def read_zst_file(file_name, key_words, timeout, output_file_name):
    total_number_of_post = dict()                                   # dictionary to track the total number of post per day
    post_per_day_dict = dict()                                      # dicttionary to track the number of post related to our key words
    #key_word_frequency_post_dict = dict()                          # dictionary to track the frequency of the key words independet to the post
    media_type_dict = dict()

    g = open(output_file_name, 'w', encoding='utf-8')
    with open(file_name, 'rb') as fh:
        dctx = zstd.ZstdDecompressor(max_window_size=2147483648)    # decompression of the zst file
        with dctx.stream_reader(fh) as reader:
            previous_line = ""
            timeout_start = time.time()
            while time.time() < timeout_start + timeout:#True:      # we restrict ourselfs to a given duration, because of testing purpose
                chunk = reader.read(2 ** 24)  # 16mb chunks
                if not chunk:
                    break
                string_data = chunk.decode('utf-8')
                lines = string_data.split("\n")
                for i, line in enumerate(lines[:-1]):
                    if i == 0:
                        line = previous_line + line
                    object = json.loads(line)

                    # here we extract all information that we want
                    title = object["title"]
                    url = object["url"]
                    author = object["author"]
                    selftext = object["selftext"]
                    subreddit_subscribers = object["subreddit_subscribers"]
                    created_utc = object["created_utc"]
                    media = object["media"]
                    date = datetime.utcfromtimestamp(created_utc)

                    # this is to know the total number of post per day
                    dt = date.strftime('%y.%m.%d')
                    if dt in total_number_of_post:
                        total_number_of_post[dt] = total_number_of_post.get(dt, 0) + 1
                    else:
                        total_number_of_post[dt] = 1

                    # this whole block has the purpose to fill the above dictionaries if the title of the post has one of our key words
                    for filter_attribute in key_words:
                        if filter_attribute in title:
                            g.write("title: " + title + '\n')
                            g.write("url: " + url + '\n')
                            g.write("author: " + author + '\n')
                            g.write("date: " + date.strftime("%m/%d/%Y, %H:%M:%S") + '\n')
                            g.write("subreddit_subscribers: " + str(subreddit_subscribers) + '\n')
                            selftext = selftext.replace('\n', ' ').replace('\r', '')
                            g.write("selftext: " + selftext + '\n')
                            if (media != None and "type" in media):
                                media_type = media["type"]
                                g.write("media_type: " + media_type + '\n')
                                if media_type in media_type_dict:
                                    media_type_dict[media_type] = media_type_dict.get(media_type, 0) + 1
                                else:
                                    media_type_dict[media_type] = 1
                            g.write('\n')
                            dt = date.strftime('%y.%m.%d')
                            if dt in post_per_day_dict:
                                post_per_day_dict[dt] = post_per_day_dict.get(dt, 0) + 1
                            else:
                                post_per_day_dict[dt] = 1
                            #if filter_attribute in key_word_frequency_post_dict:
                                #key_word_frequency_post_dict[filter_attribute] = key_word_frequency_post_dict.get(filter_attribute, 0) + 1
                            #else:
                                #key_word_frequency_post_dict[filter_attribute] = 1

                previous_line = lines[-1]
    g.close()
    #return (post_per_day_dict, key_word_frequency_post_dict, media_type_dict)
    return (post_per_day_dict, media_type_dict)
