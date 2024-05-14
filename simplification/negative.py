# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    negative.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/27 23:09:20 by auguste           #+#    #+#              #
#    Updated: 2024/05/14 18:49:24 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from type.token import          Token
from type.x import              X
from type.parentheses import    Parentheses
from type.operator import       Addition, Substraction

def inverse_negative_simplification(left_tokens: list, right_tokens: list):
    _inverse_negative_in_list(left_tokens)
    _inverse_negative_in_list(right_tokens)


def _inverse_negative_in_list(tokens: list):
    for i in range(len(tokens)):
        tokens[i] = _inverse_negative(tokens[i])


def _inverse_negative(token):
    type_token = type(token)

    if type_token == Token or type_token == X:
        return token

    if type_token == Parentheses:
        _inverse_negative_in_list(token.tokens)
        return token

    if type_token == Substraction:
        token.right = _inverse(token.right)
        return Addition(token.left, token.right)

    token.left = _inverse_negative(token.left)
    token.right = _inverse_negative(token.right)

    return token


def _inverse(token):
    type_token = type(token)

    if type_token == Token:
        token.value *= -1

    elif type_token == X:
        token.multiplication *= -1

    elif type_token == Parentheses:
        for i in range(len(token.tokens)):
            token.tokens[i] = _inverse(token.tokens[i])

    elif type_token == Addition:
        token.left = _inverse(token.left)
        token.right = _inverse(token.right)

    else:
        token.left = _inverse(token.left)

    return token
