from utils.print_utils import print_error
from type.token import Token

def split_by_equal(tokens: list) -> tuple:
    size = len(tokens)
    start = 0
    length = 0

    while length < size:
        if tokens[length].is_equal():
            break
        length += 1

    if length == 0:
        print_error("equal need values from both side")

    if length == size:
        return (tokens, [Token.parse_number('0')])

    left_tokens = tokens[start:length]

    start = length + 1
    if start == size:
        print_error("equal need values from both side")

    length = start
    while length < size:
        if tokens[length].is_equal():
            break
        length += 1

    if length != size:
        print_error("you can't have only one equal in equation")

    right_tokens = tokens[start:length]

    return (left_tokens, right_tokens)

