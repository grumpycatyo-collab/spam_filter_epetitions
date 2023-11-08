import phunspell
from utils.tokenizer import tokenize_sentence
from utils.tokenizer import remove_special_symbols


def print_all_necessary(seq_dirt, lang):
    """
    Print all necessary information for a given sequence in a specified language.

    Args:
        seq_dirt (str): The sequence to check for errors.
        lang (str): The language of the sequence.

    Returns:
        list:
        - If there are no errors in the sequence, return empty.
        - If there are errors in the sequence, return a list of suggestions.

    """

    pspell = phunspell.Phunspell(lang)

    seq = remove_special_symbols(seq_dirt)
    arr_seq = tokenize_sentence(seq)
    clean_seq = []
    [clean_seq.append(x) for x in arr_seq if x not in clean_seq]
    listWords = []
    mispelled = pspell.lookup_list(clean_seq)
    for word in mispelled:
        suggestions = []
        for suggestion in pspell.suggest(word):
            suggestions.append(suggestion)
        listWords.append({word: suggestions[:2]})
    return listWords
