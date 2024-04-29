# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parentheses.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/27 15:56:36 by auguste           #+#    #+#              #
#    Updated: 2024/04/29 23:02:22 by auguste          ###   ########.fr        #
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
            sub_tokens = []
            for tok in left.tokens:
                sub_tokens.append(_add_token_multiply_number_or_x(tok, right))
            return Parentheses(sub_tokens)

        if (type_left == Token or type_left == X)\
                and type_right == Parentheses:
            sub_tokens = []
            for tok in right.tokens:
                sub_tokens.append(_add_token_multiply_number_or_x(tok, left))
            return Parentheses(sub_tokens)
        if type_left == Parentheses and type_right == Parentheses:
            return _add_token_multiply_parentheses(left, right)

    elif type_token == Division:
        token.left = _parentheses_simplify(token.left)
        token.right = _parentheses_simplify(token.right)
        left = token.left
        right = token.right
        type_left = type(token.left)
        type_right = type(token.right)

        if type_left == Parentheses\
                and (type_right == Token or type_right == X):
            sub_tokens = []
            for tok in left.tokens:
                sub_tokens.append(_add_token_divide_by_number_or_x(tok, right))
            return Parentheses(sub_tokens)

    elif type_token == Power:
        token.left = _parentheses_simplify(token.left)
        token.right = _parentheses_simplify(token.right)
        left = token.left
        right = token.right
        type_left = type(token.left)
        type_right = type(token.right)

        if type_left == Parentheses and type_right == Token:
            return _add_token_parentheses_power_by_number(left, right)

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


def _add_token_multiply_parentheses(left: Parentheses, right: Parentheses):
    sub_tokens = []
    for ltok in left.tokens:
        for rtok in right.tokens:
            print(f"TKT {ltok} * {rtok} ")
            sub_tokens.append(Multiplication(ltok, rtok))

    print("CHECK")
    for tok in sub_tokens:
        print("   ", tok)

    ret = Parentheses(sub_tokens)
    print("CHECK 2")
    print(ret)

    return ret


def _add_token_parentheses_power_by_number(token: Parentheses, value: Token):
    divide = False
    if value.value < 0:
        value.value = -value.value
        divide = True

    copy_subtokens = token.tokens.copy()
    result = token
    for _ in range(1, int(value.value)):
        result = Multiplication(result, Parentheses(copy_subtokens.copy()))

    result = _parentheses_simplify(result)

    if divide:
        result = Division(Token.create_number(1), result)

    return result
