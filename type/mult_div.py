# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mult_div.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/26 20:16:09 by auguste           #+#    #+#              #
#    Updated: 2024/04/27 00:24:20 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_utils import   print_error
from type.token import          Token
from type.parentheses import    Parentheses

class Multiplication:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.left) + " * " + str(self.right)

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        string = ' ' * depth + "mutiplication :\n"
        depth += 2

        string += self.left.to_string(depth) + '\n'
        string += self.right.to_string(depth) + '\n'

        return string


class Division:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.left) + " / " + str(self.right)

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        string = ' ' * depth + "division :\n"
        depth += 2

        string += self.left.to_string(depth) + '\n'
        string += self.right.to_string(depth) + '\n'

        return string




# Parsing function ###########################################################

def parse_mult_div(tokens: list):
    i = 0

    while i < len(tokens):
        if type(tokens[i]) == Parentheses:
            parse_mult_div(tokens[i].tokens)
            i += 1
            continue

        if not type(tokens[i]) == Token or not tokens[i].is_operator():
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

        tokens.pop(i)
        tokens.pop(i)

        if type(before) == Token:
            if before.is_operator():
                print_error("value before the operator can't be an operator")

            if before.is_number() and before.value == 0.0:
                tokens[i - 1] = Token.parse_number('0')
                i += 1
                continue


        if type(after) == Token:
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

        if operator == '*':
            tokens[i - 1] = Multiplication(before, after)
        else:
            tokens[i - 1] = Division(before, after)

        i += 1
