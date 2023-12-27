import re


def lexical_analysis(code):
    tokens = []

    # Define token types
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
        'RESERVED_WORD': r'\b(for|while|if|do|return|break|continue|end)\b',
        'IDENTIFIER': r'\b(int|float|str|bool|double|char)\b',
        'NUMBER': r'\d+(\.\d+)?',
        'VARIABLE': r'\b\w+\b',
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


source_code = """
x = input("Enter anything")
if "&&" in x:
    print(x.index("&&"))
    x = x.replace("&&", "")
    print("&&", "is and")
if "||" in x:
    print(x.index("||"))
    x = x.replace("||", " ")
    print("||", "is or")
if "++" in x:
    print(x.index("++"))
    x = x.replace("++", "")
    print("++", "is increment operator")
if "--" in x:
    x = x.replace("--", "")
    print("--", "is a decrement operator")

for i in y:
    if i in ["int", "float", "str", "bool", "double", "char"]:
        print(i, "is a data type")
    elif i in ["+", "-", "/", "*", "%", "==", "!=", "<=", ">=", "||", "&&", "--", "++"]:
        print(i, "is an operator")
    elif i == "(":
        print(i, "is an opened bracket")
    elif i == ")":
        print(i, "is a closed bracket")
    elif i == "{":
        print(i, "is an open curly bracket")
    elif i == "}":
        print(i, "is a closed curly bracket")
    elif i == ",":
        print(i, "is a comma")
    elif i == ";":
        print(i, "is a semicolon")
    elif i == "&":
        continue
    elif i == "|":
        continue
    elif i == "<":
        print(i, "less than")
    elif i == ">":
        print(i, "is greater than")
    elif i == "=":
        print(i, "is equal")
    elif i == "!":
        print(i, "is not")
    elif i in ["for", "while", "if", "do", "return", "break", "continue", "end"]:
        print(i, "is a reserved word")
    elif i.isnumeric():
        print(i, "is a number")
    else:
        print(i, "is a variable")"""

token = lexical_analysis(source_code)
print("\nTokens:")
for i in token:
    print(i)
