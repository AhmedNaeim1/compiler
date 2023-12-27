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


def check_variables(list_of_tokens, index):
    if list_of_tokens[index + 1][0] == "ASSIGNMENT_OPERATOR":
        count = index + 1
        while True:
            if list_of_tokens[count + 1][0] == "NUMBER" or list_of_tokens[count + 1][0] == "VARIABLE":

                count += 1
                if list_of_tokens[count + 1][0] == "SEMICOLON":

                    count += 1
                    return "Valid"
                elif list_of_tokens[count + 1][0] == "ARITHMETIC_OPERATOR":

                    count += 1
                else:
                    return "Invalid"

            else:
                return "Invalid"
    elif list_of_tokens[index + 1][0] == "SEMICOLON":
        return "Valid"
    elif list_of_tokens[index - 1][0] == "SEMICOLON" and list_of_tokens[index + 1][0] != "ASSIGNMENT_OPERATOR":
        return "Invalid"
    else:
        return "Variable in use"


source_code = """
int x=5;
x=10;
x=10+9+x+5;
int y;"""

token = lexical_analysis(source_code)
print("\nTokens:")
variables = []
indicated_variables = []
data_type = []
for index_of_variable, i in enumerate(token):
    if i[0] == "VARIABLE":
        if i[1] in indicated_variables:
            variables.append(i[1])
            # print("Index:", index_of_variable)
            print(check_variables(token, index_of_variable))
        else:
            if token[index_of_variable - 1][0] == "DATA_TYPE":
                data_type.append(token[index_of_variable - 1][1])
                indicated_variables.append(i[1])
                variables.append(i[1])
                # print("Here. Index:", index_of_variable)
                print(check_variables(token, index_of_variable))
            else:
                print(i[1], "is not an indicated variable")

print(indicated_variables, data_type)
