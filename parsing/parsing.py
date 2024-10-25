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

    before = "start"
    isSpaceBetweenBefore = False

    start = 0
    while start < length:
        tmp = start
        start = get_end_white_spaces(string, length, start)
        if start > tmp:
            isSpaceBetweenBefore = True
        if start == length:
            break

        end = 0
        token = None

        if is_begin_number(string[start]):
            end = get_end_number(string, length, start)
            token = Token.parse_number(string[start:end])

            if not isSpaceBetweenBefore:
                if before == "operator" \
                        and len(tokens) > 0 and tokens[-1].value == '-':
                    strNumber = '-' + string[start:end]
                    token = Token.parse_number(strNumber)
                    tokens.pop()

                elif before == "parentheses" \
                        and len(tokens) > 0 and tokens[-1].value == ')':
                    tokens.append(Token.parse_operator("*"))

            before = "number"
            isSpaceBetweenBefore = False
            tokens.append(token)

        elif is_operator(string[start]):
            end = start + 1
            token = Token.parse_operator(string[start:end])
            before = "operator"
            isSpaceBetweenBefore = False
            tokens.append(token)

        elif is_parentheses(string[start]):
            end = start + 1
            token = Token.parse_parenthese(string[start:end])

            if not isSpaceBetweenBefore and token.value == '(':
                if before == "number" or before == "variable":
                    tokens.append(Token.parse_operator("*"))


            before = "parentheses"
            isSpaceBetweenBefore = False
            tokens.append(token)

        elif string[start] == '=':
            end = start + 1
            token = Token.parse_equal(string[start:end])
            before = "equal"
            isSpaceBetweenBefore = False
            tokens.append(token)

        else:
            end = get_end_variable(string, length, start)
            token = Token.parse_variable(string[start:end])

            if not isSpaceBetweenBefore:
                if before == "operator" \
                        and len(tokens) > 0 and tokens[-1].value == '-':
                    tokens.pop()
                    tokens.append(Token.parse_parenthese("("))
                    tokens.append(Token.parse_number("-1"))
                    tokens.append(Token.parse_operator("*"))
                    tokens.append(token)
                    tokens.append(Token.parse_parenthese(")"))

                elif before == "parentheses" \
                        and len(tokens) > 0 and tokens[-1].value == ')':
                    tokens.append(Token.parse_operator("*"))
                    tokens.append(token)

                elif before == "number":
                    tokens.append(Token.parse_operator("*"))
                    tokens.append(token)

                else:
                    tokens.append(token)

            else:
                tokens.append(token)

            before = "variable"
            isSpaceBetweenBefore = False

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
            or is_parentheses(string[i]) or string[i] == '=':
            break
        i += 1
    return i
