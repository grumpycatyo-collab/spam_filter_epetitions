import language_tool_python

tool = language_tool_python.LanguageTool('ro-RO')


def check_grammar_mistakes(seq):
    """
       Checks for grammar mistakes in a given sequence.

       Parameters:
           seq (str): The input sequence to be checked for grammar mistakes.

       Returns:
           bool: True if grammar mistakes are found, False otherwise.

       Notes:
           This function uses a grammar checking tool to analyze the input sequence.
           It returns True if one or more grammar mistakes are found, and False otherwise.
       """
    errors = tool.check(seq)
    if len(errors) == 0:
        return False
    else:
        return True


def print_suggestions(seq):
    """
        Generate a list of error suggestions for a given sequence.

        Args:
            seq (str): The input sequence to be checked for errors.

        Returns:
            list: A list of dictionaries containing error message and suggestions (json).
                Each dictionary has the following format:
                {
                    "message": str,             # The error message.
                    "suggestions": list[str]    # List of suggested replacements.
                }
    """
    matches_data = []
    errors = tool.check(seq)
    for error in errors:
        matches_data.append({
            "message": error.message,
            "suggestions": error.replacements
        })
    return matches_data


def print_error_location(seq):
    """
       Generate error location information for a given sequence.

       Args:
           seq (str): The input sequence to be checked for errors.

       Returns:
           list: A list of dictionaries containing error location details (json).
               Each dictionary has the following format:
               {
                   "offsetInContext": int,  # The offset of the error within the context.
                   "offset": int,           # The offset of the error.
                   "errorLength": int       # The length of the error.
               }
    """
    matches_data = []
    errors = tool.check(seq)
    for error in errors:
        matches_data.append({
            "offsetInContext": error.offsetInContext,
            "offset": error.offset,
            "errorLength": error.errorLength
        })
    return matches_data
