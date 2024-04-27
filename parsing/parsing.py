# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parsing.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/25 19:33:36 by auguste           #+#    #+#              #
#    Updated: 2024/04/25 19:33:36 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_utils import print_error
from type.token import Token

def get_tokens_from_input(string: str) -> list:
    tokens = []

    length = len(string)
    if length == 0:
        print_error("empty parameter")

    before = "operator"

    start = 0
    while start < length:
        start = get_end_white_spaces(string, length, start)
        if start == length:
            break

        end = 0
        token = None

        if is_begin_number(string[start])\
                or (before == "operator" and start + 1 < length\
                    and string[start] == '-'\
                    and is_begin_number(string[start + 1])):
            end = get_end_number(string, length, start)
            token = Token.parse_number(string[start:end])
            before = "number"

        elif is_operator(string[start]):
            end = start + 1
            token = Token.parse_operator(string[start:end])
            before = "operator"

        elif is_parentheses(string[start]):
            if before == "variable":
                tokens.append(Token.parse_operator('*'))
            end = start + 1
            token = Token.parse_parenthese(string[start:end])
            before = "parentheses"

        elif string[start] == '=':
            end = start + 1
            token = Token.parse_equal(string[start:end])
            before = "equal"

        else:
            if before == "number" or before == "parentheses":
                tokens.append(Token.parse_operator('*'))
            end = get_end_variable(string, length, start)
            token = Token.parse_variable(string[start:end])
            before = "variable"

        tokens.append(token)
        start = end

    return tokens

# Utils functions ##############################################################
# Is functions -----------------------------------------------------------------

def is_white_space(char: str) -> bool:
    return char in " \t"


def is_operator(char: str) -> bool:
    return char in "+-*/^"


def is_parentheses(char: str) -> bool:
    return char in "()"


def is_begin_number(char: str) -> bool:
    return char in "0123456789"


def is_begin_number_negative(char: str) -> bool:
    return char in "0123456789-"

# get end functions ------------------------------------------------------------

def get_end_white_spaces(string: str, length: int, i: int) -> int:
    while i < length:
        if not is_white_space(string[i]):
            break
        i += 1
    return i


def get_end_number(string: str, length: int, i: int) -> int:
    if string[i] == '-':
        i += 1
    while i < length:
        if string[i] not in "0123456789.":
            break
        i += 1
    return i


def get_end_variable(string: str, length: int, i: int) -> int:
    while i < length:
        if is_white_space(string[i]) or is_operator(string[i])\
            or is_parentheses(string[i]):
            break
        i += 1
    return i
