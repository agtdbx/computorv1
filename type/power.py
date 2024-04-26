from utils.print_utils import   print_error
from type.token import          Token
from type.parentheses import    Parentheses

class Power:
    def __init__(self, number, power) -> None:
        self.number = number
        self.power = power

    def __str__(self) -> str:
        return str(self.number) + '^' + str(self.power)

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        string = ' ' * depth + "power :\n"
        depth += 2

        string += self.number.to_string(depth) + '\n'
        string += self.power.to_string(depth) + '\n'

        return string

    # Static methods ###########################################################

    def parse_power(tokens: list):
        i = 0

        while i < len(tokens):
            if type(tokens[i]) == Parentheses:
                Power.parse_power(tokens[i].tokens)
                i += 1
                continue

            if not type(tokens[i]) == Token or not tokens[i].is_operator()\
                    or tokens[i].value != '^':
                i += 1
                continue

            if i == 0:
                print_error("need a value before the power")

            before = tokens[i - 1]

            if type(before) == Token and before.is_operator():
                print_error("value before the power can't be an operator")

            if i + 1 == len(tokens):
                print_error("need a value after the power")

            divide = None
            after = tokens[i + 1]
            if type(after) == Token:
                if after.is_operator():
                    print_error("value after the power can't be an operator")
                elif after.is_variable():
                    print_error("value after the power can't be a variable")
                elif after.is_number():
                    number = after.value

                    if number == 0:
                        tokens.pop(i)
                        tokens.pop(i)
                        tokens[i - 1] = Token.parse_number('1')
                        continue

                    if number == 1:
                        tokens.pop(i)
                        tokens.pop(i)
                        continue

                    elif number < 0:
                        number = -number
                        divide = number

                    if number - int(number) != 0:
                        print_error("number after the power can't be decimal")

            elif type(after) == Parentheses:
                Power.parse_power(after.tokens)

            tokens.pop(i)
            tokens.pop(i)

            tokens[i - 1] = Power(before, after)
