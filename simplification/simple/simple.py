# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    simple.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/27 11:43:37 by auguste           #+#    #+#              #
#    Updated: 2024/04/27 12:01:29 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from type.token import          Token
from type.x import              X
from type.parentheses import    Parentheses
from type.operator import       Power, Multiplication, Division, Addition,\
                                Substraction

def simple_simplification(left_tokens: list, right_tokens: list):
    _simple_simplification(left_tokens)
    _simple_simplification(right_tokens)


def _simple_simplification(tokens: list):
    for token in tokens:
        _simple_simplify(token)


def _simple_simplify(token):
    type_token = type(token)

    if type_token == Token or type_token == X:
        return

    #elif type_token == Parentheses:
    #    for tok in token.tokens:
    #        _simple_simplify()
