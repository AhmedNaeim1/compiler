from LexicalAnalysis import lexical_analysis


def check_variables(list_of_tokens, index):
    if list_of_tokens[index + 1][0] == "ASSIGNMENT_OPERATOR":
        count = index + 1
        while True:
            if list_of_tokens[count + 1][0] == "NUMBER" or list_of_tokens[count + 1][0] == "VARIABLE":
                count += 1


                if list_of_tokens[count + 1][0] == "SEMICOLON":

                    count += 1
                    print("Valid syntax of variable")
                    return count
                elif list_of_tokens[count + 1][0] == "ARITHMETIC_OPERATOR":
                    count += 1
                else:
                    print("Invalid syntax of a variable senicolon")
                    return count
            else:
                print("Invalid")
                return count
    elif list_of_tokens[index + 1][0] == "SEMICOLON":
        print("Valid")
        return index + 1
    elif list_of_tokens[index - 1][0] == "SEMICOLON" and list_of_tokens[index + 1][0] != "ASSIGNMENT_OPERATOR":
        print("Invalid")
        return index + 1
    else:
        return "Variable in use"


def check_condition(list_of_token, index, fororif):
    count = index
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
                        elif fororif == "for":
                            if list_of_token[count + 1][0] == "SEMICOLON":
                                return count + 1
                        elif fororif == "if":
                            if list_of_token[count + 1][0] == "CLOSED_BRACKET":
                                if list_of_token[count + 2][0] == "OPEN_CURLY_BRACKET":
                                    brackets.append(list_of_token[count + 2][1])
                                    print("Valid")
                                    return count + 2
                                else:
                                    print("Forgot opened curly bracket")
                                    return count + 1
                            elif list_of_token[count + 1][0] == "LOGIC_OPERATOR":
                                print("error in the logical operator")
                                return count + 1
                            else:
                                print("Forgot closed bracket")
                                return count + 1
                        else:
                            print("Forgot the closed bracket or semicolon")
                            return count + 1
                    else:
                        print("There should be a number or variable here to compare with")
                        return count + 1
                else:
                    print("missing comparison operator")
                    return count + 1
            else:
                print("Variable " + str(list_of_token[count + 1][1]) + " is not defined")
                return count + 1
        else:
            print("Expected a variable")
            return count + 1


source_code = """

 int x=2;
 int y=10;
 x=10;
if (x==5 &&  y>10) {}
for(x=0;x <=10 ;x++){}"""

token = lexical_analysis(source_code)
print("\nTokens:")
variables = []
indicated_variables = []
data_type = []
reserved_words = []
brackets = []
index_of_variable = 0
memory = {}

while index_of_variable < len(token):
    i = token[index_of_variable]
    if i[0] == "VARIABLE":
        if i[1] in indicated_variables:
            variables.append(i[1])
            memory[i[1]] = token[index_of_variable+2][0] == "NUMBER" and token[index_of_variable+2][
                1] or None
            index_of_variable = check_variables(token, index_of_variable)
        else:
            if token[index_of_variable - 1][0] == "DATA_TYPE":
                data_type.append(token[index_of_variable - 1][1])
                indicated_variables.append(i[1])
                memory[i[1]] = token[index_of_variable + 2][0] == "NUMBER" and token[index_of_variable + 2][
                    1] or None
                variables.append(i[1])
                index_of_variable = check_variables(token, index_of_variable)
            else:
                print(i[1], "is not an indicated variable")
    if i[0] == "RESERVED_WORD":
        if i[1] == "for":
            reserved_words.append(i[1])
            count_index = index_of_variable + 1
            if token[count_index][0] == "OPENED_BRACKET":
                count_index += 1
                index_of_variable = count_index
                if token[count_index][0] == "VARIABLE":
                    if token[count_index][1] in indicated_variables:
                        count_index += 1
                        index_of_variable = count_index
                        if token[count_index][0] == "ASSIGNMENT_OPERATOR":
                            count_index += 1
                            index_of_variable = count_index
                            if token[count_index][0] == "NUMBER":
                                count_index += 1
                                index_of_variable = count_index
                                if token[count_index][0] == "SEMICOLON":
                                    count_index = check_condition(token, count_index, "for")
                                    count_index += 1
                                    index_of_variable = count_index
                                    if token[count_index][0] == "VARIABLE":
                                        count_index += 1
                                        index_of_variable = count_index
                                        if (token[count_index][0] == "INCREMENT_OPERATOR" or token[count_index][0]
                                                == "DECREMENT_OPERATOR"):
                                            count_index += 1
                                            index_of_variable = count_index
                                            if token[count_index][0] == "CLOSED_BRACKET":
                                                count_index += 1
                                                index_of_variable = count_index
                                                if token[count_index][0] == "OPEN_CURLY_BRACKET":
                                                    index_of_variable = count_index + 1
                                                    brackets.append(token[count_index][1])
                                                    print("Valid")
                                                else:
                                                    print("Forgot opened curly bracket")
                                                    index_of_variable = count_index
                                            else:
                                                print("Forgot closed bracket")
                                                index_of_variable = count_index
                                        else:
                                            print("Invalid, expected an increment or decrement operator")
                                            index_of_variable = count_index
                                    else:
                                        print("Invalid, expected a variable")
                                        index_of_variable = count_index
                                else:
                                    print("Invalid, expected a semicolon")
                                    index_of_variable = count_index
                            else:
                                print("Invalid, expected a number")
                                index_of_variable = count_index
                        else:
                            print("Invalid, expected an equal sign")
                            index_of_variable = count_index
                    else:
                        print("undefined variable")
                        index_of_variable = count_index
                else:
                    print("Invalid, expected a variable")
                    index_of_variable = count_index
            else:
                print("Invalid, expected an open bracket")
                index_of_variable = count_index
        elif i[1] == "while" or "if" or "else if":
            reserved_words.append(i[1])
            if token[index_of_variable + 1][0] == "OPENED_BRACKET":
                count_index = check_condition(token, index_of_variable + 1, "if")
                index_of_variable = count_index + 1
            else:
                print("wrong syntax")
                index_of_variable += 1
                break
    elif i[0] == "CLOSED_CURLY_BRACKET":
        if len(brackets) > 0 and brackets[len(brackets) - 1] == '{':
            brackets.pop()
            index_of_variable += 1
        else:
            print("error closed curly bracket without opened curly bracket")
            index_of_variable += 1
    else:
        print(i)
        index_of_variable += 1

print(indicated_variables, memory)
