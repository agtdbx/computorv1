# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#   is_there_an_x.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/02 14:56:36 by auguste           #+#    #+#              #
#    Updated: 2024/05/02 14:56:36 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from type.token import          Token
from type.x import              X
from type.parentheses import    Parentheses


def is_there_an_x(left_tokens: list, right_tokens: list) -> bool:
    return _is_there_an_x(left_tokens) or _is_there_an_x(right_tokens)


def _is_there_an_x(tokens: list)-> bool:
    for token in tokens:
        if if_token_have_x(token):
            return True

    return False


def if_token_have_x(token) -> bool:
    type_token = type(token)

    if type_token == Token:
        return False

    elif type_token == X:
        return True

    elif type_token == Parentheses:
        if _is_there_an_x(token.tokens):
            return True

    else:
        if if_token_have_x(token.left):
            return True
        if if_token_have_x(token.right):
            return True

    return False
