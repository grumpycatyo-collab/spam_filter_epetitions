from utils.tokenizer import tokenize_sentence
from utils.similarity import is_it_similar


def check_censoring(sentence_str):
    """
    Check if a given sentence contains any bad words.

    Args:
        sentence_str (str): The sentence to be checked.

    Returns:
        bool or list:
        - If the sentence does not contain any bad words, return False.
        - If the sentence contains bad words, return a list of the bad words.
    """
    words_list = tokenize_sentence(sentence_str)
    bad_words = []
    for word in words_list:
        if is_it_similar(word):
            bad_words.append(word)
    if len(bad_words) == 0:
        return False
    return bad_words
