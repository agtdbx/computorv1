# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    power.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/27 11:28:36 by auguste           #+#    #+#              #
#    Updated: 2024/05/14 18:49:11 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_utils import   print_error
from type.token import          Token
from type.parentheses import    Parentheses
from type.operator import       Power

def parse_power(tokens: list) -> bool:
    modification = 0
    i = 0

    while i < len(tokens):
        token_type = type(tokens[i])

        if token_type == Parentheses:
            modification += parse_power(tokens[i].tokens)

        elif token_type == Power:
            modification += parse_power(tokens[i].get_tokens_left())
            modification += parse_power(tokens[i].get_tokens_right())

        if not token_type == Token or not tokens[i].is_operator()\
                or tokens[i].value != '^':
            i += 1
            continue

        if i == 0:
            print_error("need a value before the power")
        if i + 1 == len(tokens):
            print_error("need a value after the power")

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
                    tokens[i - 1] = Token.create_number(1)
                    i += 1
                    continue

        elif type_before == Parentheses:
            modification += parse_power(before.tokens)

        elif token_type == Power:
            modification += parse_power(before.get_tokens_left())
            modification += parse_power(before.get_tokens_right())

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
                    tokens[i - 1] = Token.create_number(1)
                    i += 1
                    modification += 1
                    continue

                if number == 1.0:
                    tokens.pop(i)
                    tokens.pop(i)
                    i += 1
                    modification += 1
                    continue

                elif number < 0.0:
                    number = -number

                if number != int(number):
                    print_error("number after the power can't be decimal")

        elif type_after == Parentheses:
            modification += parse_power(after.tokens)

        elif token_type == Power:
            modification += parse_power(after.get_tokens_left())
            modification += parse_power(after.get_tokens_right())

        tokens.pop(i)
        tokens.pop(i)
        modification += 1

        if type_before == Token and before.is_number() and before.value == 0.0:
            tokens[i - 1] = Token.create_number(0)
            i += 1
            continue

        power = Power(before, after)

        tokens[i - 1] = power

    return (modification > 0)
