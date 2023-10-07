from utils.tokenizer import tokenize_sentence
from utils.similarity import is_it_similar


def check_censoring(sentence_str):
    words_list = tokenize_sentence(sentence_str)
    bad_words = []
    for word in words_list:
        if is_it_similar(word):
            bad_words.append(word)
    if len(bad_words) == 0:
        return False
    return bad_words
