import language_tool_python


def print_all_necessary(seq, lang):
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
