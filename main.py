from read_zst_file import read_zst_file
from count_frequency import count_words
from draw_diagram import draw, draw2
from calculate_frequency import count_authors, check_selfttext,keyword_frequency_in_selftext
from utilize import frequency_of_meaningful_words, merge_substrings_keys

if __name__ == '__main__':
    file_name = "zstFiles/RS_2021-06.zst"

    # timeout variable
    timeout = 10  # [seconds]

    #list with key words
    key_words = ["corona", "epidemic", "pandemic", "covid", "vaccine", "vaccinate",
                 "anti-vax", "anti-vaccine", "vaccination", "dose", "doses", "jab",
                 "quarantine", "unvaccinated", "vaccinated", "vaccination", "health care", "COVID-19"]

    output_file = 'outputFiles/posts.txt'

    d1, media_type_dict, total_number_of_post, key_word_frequency_post_dict = read_zst_file(file_name, key_words, timeout, output_file)
    d2 = count_words(key_words, output_file, 'outputFiles/frequency_keywords.txt', 'outputFiles/frequency_meaningful_words.txt')

    # draw scatter or bar
    draw(d1, "outputFiles/number_of_posts_per_day.png", "scatter", "days", "posts", "number_of_posts_per_day", 18.5, 10.5)
    draw(key_word_frequency_post_dict, "outputFiles/key_words_per_post.png", "scatter", "key_words", "posts", "key_words_per_posts", 18.5, 10.5)
    draw(d2, "outputFiles/key_words_frequency.png", "bar", "key_words", "frequency", "frequency_of_key_words", 18.5, 10.5)
    draw(media_type_dict, "outputFiles/media_source.png", "scatter", "media_source", "number_of_posts", "media_source", 38, 12)
    draw2(d1, total_number_of_post, "outputFiles/number_of_posts_per_day2.png", "scatter", "days", "posts", "number_of_posts_per_day", 18.5, 10.5)

    count_authors()
    check_selfttext()
    d1 = keyword_frequency_in_selftext()
    frequency_of_meaningful_words(d1, key_words)

    # frequency of key words in selftext:
    d3 = merge_substrings_keys(d1, key_words)
    g = open("outputFiles\\frequency_key_words_in_selftext.txt", 'w', encoding='utf-8')
    for key, value in d3.items():
        g.write('%s: %s\n' % (key, value))
    g.close()