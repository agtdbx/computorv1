from type.token import              Token
from type.parentheses import        Parentheses
from simplification.negative import _inverse

def join_left_right(left_tokens: list, right_tokens: list):
    if len(right_tokens) == 0:
        return

    if len(right_tokens) == 1 and type(right_tokens[0]) == Token\
        and right_tokens[0].value == 0:
        return

    subtokens = []
    for tok in right_tokens:
        subtokens.append(tok.copy())

    right = _inverse(Parentheses(subtokens))

    left_tokens.append(right)
    right_tokens.clear()
    right_tokens.append(Token.create_number(0))
