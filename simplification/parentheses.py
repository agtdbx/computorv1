# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parentheses.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/27 15:56:36 by auguste           #+#    #+#              #
#    Updated: 2024/04/28 00:26:38 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from type.token import          Token
from type.x import              X
from type.parentheses import    Parentheses
from type.operator import       Power, Multiplication, Division, Addition,\
                                Substraction

def parentheses_simplification(left_tokens: list, right_tokens: list):
    _parentheses_simplification(left_tokens)
    _parentheses_simplification(right_tokens)


def _parentheses_simplification(tokens: list):
    for i in range(len(tokens)):
        tokens[i] = _parentheses_simplify(tokens[i])


def _parentheses_simplify(token):
    type_token = type(token)

    if type_token == Multiplication:
        token.left = _parentheses_simplify(token.left)
        token.right = _parentheses_simplify(token.right)
        left = token.left
        right = token.right
        type_left = type(token.left)
        type_right = type(token.right)

        if type_left == Parentheses \
                and (type_right == Token or type_right == X):
            return _add_token_multiply_number_or_x(left.tokens[0], right)
        if (type_left == Token or type_left == X)\
                and type_right == Parentheses:
            return _add_token_multiply_number_or_x(right.tokens[0], left)
        if type_left == Parentheses and type_right == Parentheses:
            return _add_token_multiply_parentheses(left.tokens[0],
                                                   right.tokens[0])

    elif type_token == Division:
        token.left = _parentheses_simplify(token.left)
        token.right = _parentheses_simplify(token.right)
        left = token.left
        right = token.right
        type_left = type(token.left)
        type_right = type(token.right)

        if type_left == Parentheses\
                and (type_right == Token or type_right == X):
            return _add_token_divide_by_number_or_x(left.tokens[0], right)
        if (type_left == Token or type_left == X)\
                and type_right == Parentheses:
            return _add_token_divide_number_or_x(right.tokens[0], left)

    return token


def _add_token_multiply_number_or_x(token, value):
    type_token = type(token)

    if type_token == Addition or type_token == Substraction:
        token.left = _add_token_multiply_number_or_x(token.left, value)
        token.right = _add_token_multiply_number_or_x(token.right, value)
        return token

    if type_token == Multiplication or type_token == Division:
        token.left = Multiplication(token.left, value)
        token.right = Multiplication(token.right, value)
        return token

    if type_token == X or type_token == Token:
        return Multiplication(token, value)

    return token


def _add_token_divide_by_number_or_x(token, value):
    type_token = type(token)

    if type_token == Addition or type_token == Substraction:
        token.left = _add_token_divide_by_number_or_x(token.left, value)
        token.right = _add_token_divide_by_number_or_x(token.right, value)
        return token

    if type_token == Division or type_token == Division:
        token.left = Division(token.left, value)
        token.right = Division(token.right, value)
        return token

    if type_token == X or type_token == Token:
        return Division(token, value)

    return token


def _add_token_divide_number_or_x(token, value):
    type_token = type(token)

    if type_token == Addition or type_token == Substraction:
        token.left = _add_token_divide_number_or_x(token.left, value)
        token.right = _add_token_divide_number_or_x(token.right, value)
        return token

    if type_token == Division or type_token == Division:
        token.left = Division(value, token.left)
        token.right = Division(value, token.right)
        return token

    if type_token == X or type_token == Token:
        return Division(value, token)

    return token


def _add_token_multiply_parentheses(token, value):
    # (a + b) (c + d) = ac + ad + bc + bd
    return token
