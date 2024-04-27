# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mult_div.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/27 11:30:18 by auguste           #+#    #+#              #
#    Updated: 2024/04/27 11:30:44 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_utils import   print_error
from type.token import          Token
from type.parentheses import    Parentheses
from type.operator import       Power, Multiplication, Division

def parse_mult_div(tokens: list):
    i = 0

    while i < len(tokens):
        token_type = type(tokens[i])

        if token_type == Parentheses:
            parse_mult_div(tokens[i].tokens)

        elif token_type == Power\
                or token_type == Multiplication or token_type == Division:
            parse_mult_div(tokens[i].get_tokens_left())
            parse_mult_div(tokens[i].get_tokens_right())

        if not token_type == Token or not tokens[i].is_operator():
            i += 1
            continue

        operator = None
        if tokens[i].value == '/':
            operator = '/'
        elif tokens[i].value == '*':
            operator = '*'
        else:
            i += 1
            continue

        if i == 0:
            print_error("need a value before the operator")

        if i + 1 == len(tokens):
            print_error("need a value after the operator")

        before = tokens[i - 1]
        after = tokens[i + 1]
        type_before = type(before)
        type_after = type(after)

        tokens.pop(i)
        tokens.pop(i)

        # Check left value
        if type_before == Token:
            if before.is_operator():
                print_error("value before the operator can't be an operator")

            if before.is_number() and before.value == 0.0:
                tokens[i - 1] = Token.parse_number('0')
                i += 1
                continue

        elif type_before == Parentheses:
            parse_mult_div(before.tokens)

        elif type_before == Power\
                or type_before == Multiplication or type_before == Division:
            parse_mult_div(before.get_tokens_left())
            parse_mult_div(before.get_tokens_right())

        # Check right value
        if type_after == Token:
            if after.is_operator():
                print_error("value after the operator can't be an operator")

            if after.is_number():
                if after.value == 0.0:
                    if operator == '/':
                        print_error("can't divide by 0")
                        i += 1
                        continue
                    tokens[i - 1] = Token.parse_number('0')
                    i += 1
                    continue

                elif after.value == 1.0 and operator == '/':
                    i += 1
                    continue

        elif type_after == Parentheses:
            parse_mult_div(after.tokens)

        elif type_after == Power\
                or type_after == Multiplication or type_after == Division:
            parse_mult_div(after.get_tokens_left())
            parse_mult_div(after.get_tokens_right())

        if operator == '*':
            tokens[i - 1] = Multiplication(before, after)
        else:
            tokens[i - 1] = Division(before, after)

        i += 1
