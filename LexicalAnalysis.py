import re


def lexical_analysis(code):
    tokens = []
    token_types = {
        'LOGICAL_OPERATOR': r'(\&\&|\|\|)',
        'ARITHMETIC_OPERATOR': r'(\+|\-|\*|\/|%)',
        'OPENED_BRACKET': r'(\()',
        'CLOSED_BRACKET': r'(\))',
        'OPEN_CURLY_BRACKET': r'(\{)',
        'CLOSED_CURLY_BRACKET': r'(\})',
        'COMMA': r',',
        'SEMICOLON': r';',
        'COMPARISON_OPERATOR': r'(\==|\!=|<=|>=|<|>)',
        'ASSIGNMENT_OPERATOR': r'=',
        'INCREMENT_OPERATOR': r'\+\+',
        'DECREMENT_OPERATOR': r'\-\-',
        'RESERVED_WORD': r'\b(for|while|if|do|return|break|continue|end|else|else if)\b',
        'DATA_TYPE': r'\b(int|float|str|bool|double|char)\b',
        'NUMBER': r'\d+(\.\d+)?',
        'VARIABLE': r'\b\w+\b',
        'STRING': r'\"[^\"]*\"',
    }

    # Regular expression to match any token
    token_regex = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_types.items()))

    # Find all matches in the input code
    matches = token_regex.finditer(code)

    for match in matches:
        for name, value in match.groupdict().items():
            if value is not None:
                tokens.append((name, value))
                break

    return tokens
