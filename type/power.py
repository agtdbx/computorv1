# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    power.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/26 20:16:09 by auguste           #+#    #+#              #
#    Updated: 2024/04/26 20:16:09 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
        string += self.power.to_string(depth)

        return string

    # Getters ##################################################################

    def get_tokens_left(self) -> list:
        number_type = type(self.number)

        if number_type == Parentheses:
            return self.number.tokens

        elif number_type == Power:
            return self.number.get_tokens_left()

        return []

    def get_tokens_right(self) -> list:
        power_type = type(self.power)

        if power_type == Parentheses:
            return self.power.tokens

        elif power_type == Power:
            return self.number.get_tokens_right()

        return []

    # Static methods ###########################################################

    def parse_power(tokens: list):
        i = 0

        while i < len(tokens):
            token_type = type(tokens[i])

            if token_type == Parentheses:
                Power.parse_power(tokens[i].tokens)

            elif token_type == Power:
                Power.parse_power(tokens[i].get_tokens_left())
                Power.parse_power(tokens[i].get_tokens_right())

            if not token_type == Token or not tokens[i].is_operator()\
                    or tokens[i].value != '^':
                i += 1
                continue

            if i == 0:
                print_error("need a value before the power")
            if i + 1 == len(tokens):
                print_error("need a value after the power")

            divide = None
            before = tokens[i - 1]
            after = tokens[i + 1]
            type_before = type(before)
            type_after = type(after)

            # Check left value
            if type_before == Token:
                if before.is_operator():
                    print_error("value before the power can't be an operator")
                elif before.is_number():
                    if before.value == 1.0:
                        tokens.pop(i)
                        tokens.pop(i)
                        tokens[i - 1] = Token.parse_number('1')
                        i += 1
                        continue

            elif type_before == Parentheses:
                Power.parse_power(before.tokens)

            elif token_type == Power:
                Power.parse_power(before.get_tokens_left())
                Power.parse_power(before.get_tokens_right())

            # Check right value
            if type_after == Token:
                if after.is_operator():
                    print_error("value after the power can't be an operator")
                elif after.is_variable():
                    print_error("value after the power can't be a variable")
                elif after.is_number():
                    number = after.value

                    if number == 0.0:
                        tokens.pop(i)
                        tokens.pop(i)
                        tokens[i - 1] = Token.parse_number('1')
                        i += 1
                        continue

                    if number == 1.0:
                        tokens.pop(i)
                        tokens.pop(i)
                        i += 1
                        continue

                    elif number < 0.0:
                        number = -number
                        divide = number

                    if number != int(number):
                        print_error("number after the power can't be decimal")

            elif type_after == Parentheses:
                Power.parse_power(after.tokens)

            elif token_type == Power:
                Power.parse_power(after.get_tokens_left())
                Power.parse_power(after.get_tokens_right())

            tokens.pop(i)
            tokens.pop(i)

            if type_before == Token and before.is_number() and before.value == 0.0:
                tokens[i - 1] = Token.parse_number('0')
                i += 1
                continue

            power = Power(before, after)

            if divide != None:
                pass #TODO: add the division

            tokens[i - 1] = power
