"""Programming Assignment 2"""

predictive_parse_table = {
    "E": {
        "a": "TQ",
        "(": "TQ"
    },
    "Q": {
        "+": "+TQ",
        "-": "-TQ",
        ")": "ε",
        "$": "ε"
    },
    "T": {
        "a": "FR",
        "(": "FR"
    },
    "R": {
        "+": "ε",
        "-": "ε",
        "*": "*FR",
        "/": "/FR",
        ")": "ε",
        "$": "ε"
    },
    "F": {
        "a": "a",
        "(": "(E)"
    }
}


def parse(input_string):
    """Parse function to parse the input string"""
    print("Input: " + input_string)
    stack = ["$", "E"]
    i = 0
    while stack:
        print("Stack: " + "".join(stack))
        if stack[-1] == input_string[i]:
            # Match
            stack.pop()
            i += 1
        elif stack[-1] in predictive_parse_table:
            # Non-terminal
            if input_string[i] in predictive_parse_table[stack[-1]]:
                # Found in table
                temp = stack.pop()
                stack.extend(
                    predictive_parse_table[temp][input_string[i]][::-1])
            else:
                # Not found in table
                print("Error: Not found in table")
                break

        elif stack[-1] == "ε":
            # Epsilon
            stack.pop()
        else:
            # Error case
            print("Error: Not found in table")
            break

    if stack:
        print("String is NOT ACCEPTED / INVALID")
    else:
        print("String is ACCEPTED / VALID")


def main():
    """Main function"""
    print("Programming Assignment 2, Predictive Parsing")
    print("This program will parse the input string and determine if it is valid or not.")
    test_case_1 = "(a+a)*a$"
    test_case_2 = "a*(a/a)$"
    test_case_3 = "a(a+a)$"
    print("Test Case 1: " + test_case_1)
    parse(test_case_1)
    print("=========================================")
    print("Test Case 2: " + test_case_2)
    parse(test_case_2)
    print("=========================================")
    print("Test Case 3: " + test_case_3)
    parse(test_case_3)


if __name__ == "__main__":
    main()
