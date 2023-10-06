from utils.tokenizer import tokenize_sentence
from utils.similarity import is_it_similar


def check_censoring(sentence_str):
    """
    Check if the given sentence contains any censoring words.
    
    Args:
        sentence_str (str): The sentence to check for censoring words.
    
    Returns:
        list: A list of censoring words found in the sentence.
    """

    words_list = tokenize_sentence(sentence_str)
    bad_words = []
    for word in words_list:
        if is_it_similar(word):
            bad_words.append(word)

    return bad_words


sentence = "mata e curva"

print(check_censoring(sentence))
