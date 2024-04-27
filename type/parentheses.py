from utils.print_utils import   print_error
from type.token import          Token

class Parentheses:

    def __init__(self, sub_tokens: list) -> None:
        self.tokens = sub_tokens
        Parentheses.parse_parentheses(sub_tokens)


    def __str__(self) -> str:
        string = "("

        for i in range(len(self.tokens)):
            if i != 0:
                string += ' '
            string += str(self.tokens[i])

        string += ')'

        return string

    def contains_variable(self) -> bool:
        for token in self.tokens:
            if type(token) == Token and token.is_variable():
                return True
            if type(token) == Parentheses and token.contains_variable():
                return True
        return False

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        string = ' ' * depth + "parentheses :\n"
        depth += 2

        for i in range(len(self.tokens)):
            if i != 0:
                string += '\n'
            string += self.tokens[i].to_string(depth)

        return string

    # Static methods ###########################################################

    def parse_parentheses(tokens: list):
        i = 0

        while i < len(tokens):
            if not type(tokens[i]) == Token or not tokens[i].is_parenthese():
                i += 1
                continue

            if tokens[i].value != '(':
                print_error("invalid close parenthese")

            depth_count = 1
            start = i + 1

            i += 1

            while i < len(tokens) and depth_count > 0:
                if tokens[i].is_parenthese():
                    if tokens[i].value == '(':
                        depth_count += 1
                    else:
                        depth_count -= 1
                i += 1

            if depth_count != 0:
                print_error("unclose parenthese")

            end = i

            if start + 1 == end:
                print_error("empty parentheses")

            parentheses = Parentheses(tokens[start:end - 1])

            for _ in range(start, end):
                tokens.pop(start)

            tokens[start - 1] = parentheses

            i = start


