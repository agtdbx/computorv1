# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parentheses.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/27 15:56:36 by auguste           #+#    #+#              #
#    Updated: 2024/04/27 16:15:39 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_utils import   print_error
from utils.math_utils import    pow
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

        if type_left == Parentheses and type_right == Token:
            return _parentheses_multiply_number(left, right)
        if type_left == Token and type_right == Parentheses:
            return _parentheses_multiply_number(right, left)

    elif type_token == Division:
        token.left = _parentheses_simplify(token.left)
        token.right = _parentheses_simplify(token.right)
        left = token.left
        right = token.right
        type_left = type(token.left)
        type_right = type(token.right)

    return token


def _parentheses_multiply_number(parentheses: Parentheses, number: Token):
    return Token()
