import sys
from utils import is_it_similar, tokenize_sentence
def check_censoring(sentence):
    """
    Check if the given sentence contains any censoring words.
    
    Args:
        sentence (str): The sentence to check for censoring words.
    
    Returns:
        list: A list of censoring words found in the sentence.
    """

    words_list = tokenize_sentence(sentence)
    bad_words = []
    for word in words_list:
        if is_it_similar(word):
            bad_words.append(word)
    
    return bad_words


sentence = ""

print(check_censoring(sentence))
            

