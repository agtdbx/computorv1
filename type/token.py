# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_token.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/25 19:33:34 by auguste           #+#    #+#              #
#    Updated: 2024/04/25 19:33:34 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_utils import print_error

TOKEN_NONE = "none"                 # Value = none
TOKEN_NUMBER = "number"             # Value = number (float)
TOKEN_VARIABLE = "variable"         # Value = name
TOKEN_OPERATOR = "operator"         # Value = which operator (+ - * / ^)
TOKEN_PARENTHESE = "parentheses"    # Value = '(' or ')'
TOKEN_EQUAL = "equal"               # Value = '='

class Token:
    def __init__(self):
        self.type = TOKEN_NONE
        self.value = None

    # Overloads ################################################################

    def __str__(self) -> str:
        if self.type == TOKEN_NONE:
            return "none"
        elif self.type == TOKEN_NUMBER:
            return f"{self.value}\t: number"
        elif self.type == TOKEN_VARIABLE:
            return f"{self.value}\t: variable"
        elif self.type == TOKEN_OPERATOR:
            return f"{self.value}\t: operator"
        elif self.type == TOKEN_PARENTHESE:
            return f"{self.value}\t: parenthese"
        elif self.type == TOKEN_EQUAL:
            return "=\t: equal"
        return "unknow"


    def __eq__(self, value) -> bool:
        return self.type == value.type and self.value == value.value

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        if self.type == TOKEN_NONE:
            return ' ' * depth + "none"
        elif self.type == TOKEN_NUMBER:
            return ' ' * depth + str(self.value)
        elif self.type == TOKEN_VARIABLE:
            return ' ' * depth + str(self.value)
        elif self.type == TOKEN_OPERATOR:
            return ' ' * depth + str(self.value)
        elif self.type == TOKEN_PARENTHESE:
            return ' ' * depth + str(self.value)
        elif self.type == TOKEN_EQUAL:
            return ' ' * depth + "="
        return "unknow"

    # Is methods ###############################################################

    def is_none(self) -> bool:
        return self.type == TOKEN_NONE

    def is_number(self) -> bool:
        return self.type == TOKEN_NUMBER

    def is_variable(self) -> bool:
        return self.type == TOKEN_VARIABLE

    def is_operator(self) -> bool:
        return self.type == TOKEN_OPERATOR

    def is_parenthese(self) -> bool:
        return self.type == TOKEN_PARENTHESE

    def is_equal(self) -> bool:
        return self.type == TOKEN_EQUAL

    # Static methods ###########################################################

    def parse_number(string: str):
        token = Token()

        try:
            number = float(string)
            token.type = TOKEN_NUMBER
            token.value = number

        except:
            print_error(f"'{string}' isn't a valid number")

        return token


    def parse_variable(string: str):
        token = Token()

        for char in string:
            if not (char.isalpha() or char in "0123456789_"):
                print_error(f"'{string}' isn't a valid variable name")

        token.type = TOKEN_VARIABLE
        token.value = string

        return token


    def parse_operator(char: str):
        token = Token()

        if char not in "+-*/^":
            print_error(f"'{char}' isn't a valid operator")

        token.type = TOKEN_OPERATOR
        token.value = char

        return token


    def parse_parenthese(char: str):
        token = Token()

        if char in "()":
            token.value = char
        else:
            print_error(f"'{char}' isn't a valid parenthese")

        token.type = TOKEN_PARENTHESE

        return token


    def parse_equal(char: str):
        token = Token()

        if char != '=':
            print_error(f"'{char}' isn't a valid equal")

        token.type = TOKEN_EQUAL
        token.value = '='

        return token
