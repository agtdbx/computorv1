from type.parenthese import Parentheses

def operator_check(left_tokens: list, right_tokens: list):

    print("\n#################[CHECK PARENTHESES]#################")
    Parentheses.parse_parentheses(left_tokens)
    Parentheses.parse_parentheses(right_tokens)

    print("\n====LEFT TOKENS====")
    for token in left_tokens:
        print(token.to_string())

    print("\n====RIGHT TOKENS====")
    for token in right_tokens:
        print(token.to_string())
