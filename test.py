from calculate_frequency import count_authors, check_selfttext,keyword_frequency_in_selftext
from count_frequency import is_key_word_in_subString
from utilize import frequency_of_meaningful_words

if __name__ == '__main__':

    count_authors()
    # list with key words
    key_words = ["corona", "epidemic", "pandemic", "covid", "vaccine", "vaccinate",
                 "anti-vax", "anti-vaccine", "vaccination", "dose", "doses", "jab",
                 "quarantine", "unvaccinated", "vaccinated", "vaccination", "health care", "COVID-19"]
    #is_key_word_in_subString(key_words, "vacc")
    check_selfttext()
    d1 = keyword_frequency_in_selftext()
    frequency_of_meaningful_words(d1, key_words)