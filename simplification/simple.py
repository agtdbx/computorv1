# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    simple.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: aderouba <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/27 11:43:37 by auguste           #+#    #+#              #
#    Updated: 2024/10/28 11:50:02 by aderouba         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_equation import            print_test_equation, print_test_token
from utils.print_utils import   print_error
from utils.math_utils import    pow
from type.token import          Token
from type.x import              X
from type.parentheses import    Parentheses
from type.operator import       Power, Multiplication, Division, Addition,\
                                Substraction

def simple_simplification(left_tokens: list, right_tokens: list, doprint=False):
    try:
        _simple_simplification(left_tokens, doprint)
        _simple_simplification(right_tokens)
    except ValueError as error:
        print_error(str(error))


def _simple_simplification(tokens: list, doprint=False):
    for i in range(len(tokens)):
        tokens[i] = _simple_simplify(tokens[i])

    idLeft = 0
    while idLeft < len(tokens):
        left = tokens[idLeft]

        idRight = 0
        while idRight < len(tokens):
            if idLeft == idRight:
                idRight += 1
                continue
            right = tokens[idRight]

            test = _simple_simplify(Addition(left, right))
            if type(test) == Addition:
                idRight += 1
            else:
                tokens[idLeft] = test
                tokens.pop(idRight)
                idLeft -= 1
                break

        idLeft += 1

def _simple_simplify(token):
    type_token = type(token)

    if type_token == Token or type_token == X:
        return token

    if type_token == X:
        if token.power == 0:
            return Token.create_number(1)
        if token.multiplication == 0:
            return Token.create_number(0)
        return token

    # Power ####################################################################
    elif type_token == Power:
        token.left = _simple_simplify(token.left)
        token.right = _simple_simplify(token.right)
        left = token.left
        right = token.right
        type_left = type(token.left)
        type_right = type(token.right)

        if type_left == Token and type_right == Token:
            if int(right.value) != right.value:
                raise ValueError("power by decimal")
            result = pow(left.value, right.value)
            return Token.create_number(result)

        elif type_left == X and type_right == Token:
            if right.value == 0.0:
                return Token.create_number(1)
            left.power *= right.value
            return left

    # Multiplication ###########################################################
    elif type_token == Multiplication:
        token.left = _simple_simplify(token.left)
        token.right = _simple_simplify(token.right)
        left = token.left
        right = token.right
        type_left = type(token.left)
        type_right = type(token.right)

        if type_left == Token and type_right == Token:
            result = left.value * right.value
            return Token.create_number(result)

        elif type_left == X and type_right == Token:
            left.multiplication *= right.value
            return left

        elif type_left == Token and type_right == X:
            right.multiplication *= left.value
            return right

        elif type_left == X and type_right == X:
            left.power += right.power
            left.multiplication *= right.multiplication
            return left

        elif type_left == Division and type_right != Division:
            left.left = Multiplication(left.left, right)
            return left

        elif type_left != Division and type_right == Division:
            right.left = Multiplication(right.left, left)
            _simple_simplify(right)
            return right

    # Division #################################################################
    elif type_token == Division:
        token.left = _simple_simplify(token.left)
        token.right = _simple_simplify(token.right)
        left = token.left
        right = token.right
        type_left = type(token.left)
        type_right = type(token.right)

        if type_left == Token and type_right == Token:
            if right.value == 0:
                raise ValueError("division by 0")
            result = left.value / right.value
            return Token.create_number(result)

        elif type_left == X and type_right == Token:
            left.multiplication /= right.value
            return left

        elif type_left == Token and type_right == X:
            if left.value == 0:
                return left
            return token

        elif type_left == X and type_right == X:
            if left == right:
                return Token.create_number(1)
            left.power -= right.power
            left.multiplication *= right.multiplication
            return left

        elif type_left == Parentheses and type_right == Parentheses:
            if left == right:
                return Token.create_number(1)
            return token

    # Addition #################################################################
    elif type_token == Addition:
        token.left = _simple_simplify(token.left)
        token.right = _simple_simplify(token.right)
        left = token.left
        right = token.right
        type_left = type(token.left)
        type_right = type(token.right)

        if type_left == Token and type_right == Token:
            result = left.value + right.value
            return Token.create_number(result)

        elif type_left == X and type_right == X:
            if left.power != right.power:
                return token
            left.multiplication += right.multiplication
            if left.multiplication == 0:
                return Token.create_number(0)
            return left

    # Substraction #############################################################
    elif type_token == Substraction:
        token.left = _simple_simplify(token.left)
        token.right = _simple_simplify(token.right)
        left = token.left
        right = token.right
        type_left = type(token.left)
        type_right = type(token.right)

        if type_left == Token and type_right == Token:
            result = left.value - right.value
            return Token.create_number(result)

        elif type_left == X and type_right == X:
            if left.power != right.power:
                return token
            left.multiplication -= right.multiplication
            if left.multiplication == 0:
                return Token.create_number(0)
            return left

    # Parentheses ##############################################################
    elif type_token == Parentheses:
        _simple_simplification(token.tokens)

        if len(token.tokens) == 1:
            return token.tokens[0]

        return token

    return token
