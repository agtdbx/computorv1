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

            after = tokens[i + 1]
            if type(after) == Token:
                if after.is_operator():
                    print_error("value after the power can't be an operator")
                elif after.is_variable():
                    print_error("value after the power can't be a variable")
                elif after.is_number():
                    number = after.value

                    if number > 0 and number - int(number):
                        print_error("number after the power can't be decimal")
                    elif number < 0 and number + int(number):
                        print_error("number after the power can't be decimal")

            # elif type(after) == Parentheses and after.contains_variable():
            #     print_error("value after the power can't contains a variable")

            # end = i

            # if start + 1 == end:
            #     print_error("empty parentheses")

            # parentheses = Parentheses(tokens[start:end - 1])

            # for _ in range(start, end):
            #     tokens.pop(start)

            # tokens[start - 1] = parentheses

            # i = start
