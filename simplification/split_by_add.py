# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    split_by_add.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/28 11:10:07 by auguste           #+#    #+#              #
#    Updated: 2024/04/28 11:57:49 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from type.token import          Token
from type.x import              X
from type.parentheses import    Parentheses
from type.operator import       Power, Multiplication, Division, Addition,\
                                Substraction

def split_by_add_simplification(tokens: list) -> list:
    new_list = []
    modify = True

    while modify:
        modify = False
        new_list = []
        for token in tokens:
            type_token = type(token)

            if type_token == Addition:
                modify = True
                new_list.append(token.left)
                new_list.append(token.right)
                continue

            if type_token == Parentheses\
                    and _is_addition_in_parentheses(token):
                modify = True
                token.tokens = split_by_add_simplification(token.tokens)
                new_list.append(token)
                continue

            if _is_addition_in_token(token):
                _split_by_add_token(token)
                new_list.append(token)
                continue

            new_list.append(token)
        tokens = new_list

    return new_list


def _is_addition_in_token(token) -> bool:
    type_token = type(token)

    if type_token == Token or type_token == X:
        return False

    if type_token == Addition:
        return True

    if type_token == Parentheses:
        return _is_addition_in_parentheses(token)

    if type_token == Power:
        if _is_addition_in_token(token.number):
            return True

        if _is_addition_in_token(token.power):
            return True

        return False

    if _is_addition_in_token(token.left):
        return True

    if _is_addition_in_token(token.right):
        return True

    return False


def _is_addition_in_parentheses(parentheses: Parentheses) -> bool:
    for token in parentheses.tokens:
        if _is_addition_in_token(token):
            return True
    return False


def _split_by_add_token(token):
    type_token = type(token)

    if type_token == Token or type_token == X:
        return

    if type_token == Parentheses:
        token.tokens = split_by_add_simplification(token.tokens)
        return

    if type_token == Power:
        _split_by_add_token(token.number)
        _split_by_add_token(token.power)
        return

    _split_by_add_token(token.left)
    _split_by_add_token(token.right)
