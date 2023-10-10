from src.censore.censore_main import check_censoring
from src.grammar_correction.grammar_correction_main import print_all_necessary
from utils.similarity import has_cyrillic


def filter_spam(message):
    if has_cyrillic(message):
        grammar_result = print_all_necessary(message, 'ru-RU')
    else:
        grammar_result = print_all_necessary(message, 'ro-RO')
    censoring_result = check_censoring(message)
    string = f'{censoring_result} / {grammar_result}'
    return string
