import language_tool_python


def grammar_check_with_replacements(text):
    tool = language_tool_python.LanguageTool('en-US')

    matches = tool.check(text)

    errors = []

    for match in matches:
        error_info = {
            'error_position': f"Error at position {match.offset}-{match.errorLength + match.offset}",
            'error_type': match.ruleIssueType,
            'original_text': match.context,
            'suggestions': match.replacements
        }
        errors.append(error_info)

    return errors
