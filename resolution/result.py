# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    result.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/01 00:58:14 by auguste           #+#    #+#              #
#    Updated: 2024/05/01 01:32:45 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.math_utils import        pow
from type.token import              Token
from type.x import                  X
from type.parentheses import        Parentheses
from simplification.simple import   _simple_simplification

def check_result(save_operator_left, save_operator_right, result: float) -> bool:
    try:
        result_left = _check_result(save_operator_left, result)
        result_right = _check_result(save_operator_right, result)
        return result_left == result_right
    except:
        return False

def _check_result(save_operator, result: float) -> float:
    check_operator = []
    for tok in save_operator:
        check_operator.append(_replace_x(tok, result))
    _simple_simplification(check_operator)
    if len(check_operator) > 0:
        return check_operator[0].value
    return Token.create_number(0)


def _replace_x(token, result: float):
    if type(token) == Token:
        return token.copy()
    if type(token) == X:
        value = pow(result, token.power) * token.multiplication
        return Token.create_number(value)
    if type(token) == Parentheses:
        sub_tokens = []
        for i in range(len(token.tokens)):
            sub_tokens.append(_replace_x(token.tokens[i]))
        return Parentheses(sub_tokens)
    new_token = token.copy()
    new_token.left = _replace_x(token.left, result)
    new_token.right = _replace_x(token.right, result)
    return new_token
