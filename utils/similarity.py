from difflib import get_close_matches
import re

route_ro = r'C:\Users\Max\spam_filter_epetitions\data\md_ro.txt'
route_ru = r'C:\Users\Max\spam_filter_epetitions\data\rus.txt'

file1 = open(route_ro, 'r', encoding='utf-8')
censored_words_ro = file1.read().splitlines()

file2 = open(route_ru, 'r', encoding='utf-8')
censored_words_ru = file2.read().splitlines()


def has_cyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


def is_it_similar(word):
    """
    Check if a given word is similar to any of the censored words.

    Parameters:
        word (str): The word to check for similarity.

    Returns:
        bool: True if the word is similar to at least two censored words, False otherwise.
    """

    word = word.lower()
    if has_cyrillic(word):
        print("rus")
        length = len(get_close_matches(word, censored_words_ru, cutoff=0.60))
    else:
        print("ro")
        length = len(get_close_matches(word, censored_words_ro, cutoff=0.75))
    if length >= 2:
        return True
    else:
        return False
