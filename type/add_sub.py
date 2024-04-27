# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    add_sub.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/26 20:16:09 by auguste           #+#    #+#              #
#    Updated: 2024/04/27 02:24:56 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_utils import   print_error
from type.token import          Token
from type.parentheses import    Parentheses
from type.power import          Power
from type.mult_div import       Multiplication, Division

class Addition:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.left) + " + " + str(self.right)

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        string = ' ' * depth + "addition :\n"
        depth += 2

        string += self.left.to_string(depth) + '\n'
        string += self.right.to_string(depth)

        return string

    # Getters ##################################################################

    def get_tokens_left(self) -> list:
        if type(self.left) == Parentheses:
            return self.left.tokens
        return []

    def get_tokens_right(self) -> list:
        if type(self.right) == Parentheses:
            return self.right.tokens
        return []


class Substraction:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.left) + " - " + str(self.right)

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        string = ' ' * depth + "substraction :\n"
        depth += 2

        string += self.left.to_string(depth) + '\n'
        string += self.right.to_string(depth)

        return string

    # Getters ##################################################################

    def get_tokens_left(self) -> list:
        left_type = type(self.left)

        if left_type == Parentheses:
            return self.left.tokens

        elif left_type == Power\
                or left_type == Multiplication or left_type == Division\
                or left_type == Addition or left_type == Substraction:
            return self.left.get_tokens_left()

        return []

    def get_tokens_right(self) -> list:
        right_type = type(self.right)

        if right_type == Parentheses:
            return self.right.tokens

        elif right_type == Power\
                or right_type == Multiplication or right_type == Division\
                or right_type == Addition or right_type == Substraction:
            return self.left.get_tokens_left()

        return []

# Parsing function ###########################################################

def parse_add_sub(tokens: list):
    i = 0

    while i < len(tokens):
        token_type = type(tokens[i])

        if token_type == Parentheses:
            parse_add_sub(tokens[i].tokens)

        elif token_type == Power\
                or token_type == Multiplication or token_type == Division\
                or token_type == Addition or token_type == Substraction:
            parse_add_sub(tokens[i].get_tokens_left())
            parse_add_sub(tokens[i].get_tokens_right())

        if not token_type == Token or not tokens[i].is_operator():
            i += 1
            continue

        operator = None
        if tokens[i].value == '-':
            operator = '-'
        elif tokens[i].value == '+':
            operator = '+'
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

            if before.is_number() and before.value == 0.0 and operator == '+':
                tokens[i - 1] = after
                i += 1
                continue

        elif type_before == Parentheses:
            parse_add_sub(before.tokens)

        elif type_before == Power\
                or type_before == Multiplication or type_before == Division\
                or type_before == Addition or type_before == Substraction:
            parse_add_sub(before.get_tokens_left())
            parse_add_sub(before.get_tokens_right())

        # Check right value
        if type_after == Token:
            if after.is_operator():
                print_error("value after the operator can't be an operator")

            if after.is_number():
                if after.value == 0.0:
                    i += 1
                    continue

        elif type_after == Parentheses:
            parse_add_sub(after.tokens)

        elif type_after == Power\
                or type_after == Multiplication or type_after == Division\
                or type_after == Addition or type_after == Substraction:
            parse_add_sub(after.get_tokens_left())
            parse_add_sub(after.get_tokens_right())

        if operator == '+':
            tokens[i - 1] = Addition(before, after)
        else:
            tokens[i - 1] = Substraction(before, after)

        i += 1
