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

TOKEN_NONE = "none"                # Value = none
TOKEN_NUMBER = "number"            # Value = number (float)
TOKEN_VARIABLE = "variable"        # Value = name
TOKEN_OPERATOR = "operator"        # Value = which operator (+ - * / ^)
TOKEN_PARENTHESES = "parentheses"  # Value = 'open' or 'close'
TOKEN_EQUAL = "equal"              # Value = '='

class Token:
    def __init__(self):
        self.type = TOKEN_NONE
        self.value = None

    # Overloads ################################################################

    def __str__(self) -> str:
        if self.type == TOKEN_NONE:
            return "(Token None)"
        elif self.type == TOKEN_NUMBER:
            return f"(Token number {self.value})"
        elif self.type == TOKEN_VARIABLE:
            return f"(Token variable {self.value})"
        elif self.type == TOKEN_OPERATOR:
            return f"(Token operator {self.value})"
        elif self.type == TOKEN_PARENTHESES:
            return f"(Token parentheses {self.value})"
        elif self.type == TOKEN_EQUAL:
            return "(Token equal)"
        return "(Token unknow)"


    def __eq__(self, value) -> bool:
        return self.type == value.type and self.value == value.value

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

        if char == '(':
            token.value = "open"
        elif char == ')':
            token.value = "close"
        else:
            print_error(f"'{char}' isn't a valid parenthese")

        token.type = TOKEN_PARENTHESES

        return token


    def parse_equal(char: str):
        token = Token()

        if char != '=':
            print_error(f"'{char}' isn't a valid equal")

        token.type = TOKEN_EQUAL
        token.value = '='

        return token
