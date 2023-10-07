import language_tool_python


def print_all_necessary(seq, lang):
    """
    Print all necessary information for a given sequence in a specified language.

    Args:
        seq (str): The sequence to check for errors.
        lang (str): The language of the sequence.

    Returns:
        bool or list:
        - If there are no errors in the sequence, return False.
        - If there are errors in the sequence, return a list of dictionaries containing the error information.
          Each dictionary includes the offset of the error, the length of the error, and suggestions for replacement.

    """
    tool = language_tool_python.LanguageTool(lang)
    matches_data = []
    errors = tool.check(seq)
    if len(errors) == 0:
        return False
    else:
        for error in errors:
            matches_data.append({
                "offset": error.offset,
                "errorLength": error.errorLength,
                "suggestions": error.replacements
            })
        return matches_data
