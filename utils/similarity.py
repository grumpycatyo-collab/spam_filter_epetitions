from difflib import get_close_matches

route = r'C:\Users\Max\spam_filter_epetitions\data\md_ro.txt'
# replace route with your desired route (i have problems with route)
file = open(route, 'r', encoding='utf-8')
censored_words = file.read().splitlines()


def is_it_similar(word):
    """
    Check if a given word is similar to any of the censored words.

    Parameters:
        word (str): The word to check for similarity.

    Returns:
        bool: True if the word is similar to at least two censored words, False otherwise.
    """

    word = word.lower()
    length = len(get_close_matches(word, censored_words, cutoff=0.75))
    if length >= 2:
        return True
    else:
        return False
