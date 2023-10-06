import nltk
import re
from nltk.tokenize import word_tokenize


def remove_special_symbols(text):
    """
    Removes special symbols from the given text.
    Args:
        text (str): The input text containing special symbols.
    Returns:
        str: The cleaned text with special symbols removed.
    """
    pattern = r'[^\w\sа-яА-Яa-zA-Z0-9]'

    cleaned_text = re.sub(pattern, ' ', text)
    return cleaned_text


def tokenize_sentence(sentence):
    """
    Tokenizes a given sentence into a list of words.

    Args:
        sentence (str): The sentence to be tokenized.

    Returns:
        list: A list of words obtained after tokenization.
    """

    nltk.download('punkt', quiet=True)

    words = word_tokenize(remove_special_symbols(sentence))
    return words
