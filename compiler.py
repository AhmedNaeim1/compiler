from LexicalAnalysis import lexical_analysis


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


def check_condition(list_of_token, index):
    count = index + 1
    while True:
        if list_of_token[count + 1][0] == "VARIABLE":
            if list_of_token[count + 1][1] in indicated_variables:
                variables.append(list_of_token[count + 1][1])
                count += 1
                if list_of_token[count + 1][0] == "COMPARISON_OPERATOR":
                    count += 1
                    if list_of_token[count + 1][0] == "VARIABLE" or list_of_token[count + 1][0] == "NUMBER":
                        count += 1
                        if list_of_token[count + 1][0] == "LOGICAL_OPERATOR":
                            count += 1
                        elif list_of_token[count + 1][0] == "CLOSED_BRACKET":
                            print("Valid")
                            break
                        else:
                            print("Invalid")
                            break
                    else:
                        print("Invalid")
                        break
                else:
                    print("Invalid")
                    break
        else:
            print("Invalid variable")
            break


source_code = """
int x=5;
x=10;
x=10+9+x+5;
int y;
if(x>10)
if(x>=10||y<5){}"""

token = lexical_analysis(source_code)
print("\nTokens:")
variables = []
indicated_variables = []
data_type = []
reserved_words = []
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
    if i[0] == "RESERVED_WORD":
        if i[1] == "for":
            reserved_words.append(i[1])
            continue
        elif i[1] == "while":
            reserved_words.append(i[1])
            continue
        elif i[1] == "if":
            reserved_words.append(i[1])
            if token[index_of_variable + 1][0] == "OPENED_BRACKET":
                check_condition(token, index_of_variable)

            else:
                print("wrong syntax")
                break

print(indicated_variables, data_type)
