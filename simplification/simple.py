# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    simple.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/27 11:43:37 by auguste           #+#    #+#              #
#    Updated: 2024/04/27 20:52:43 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_utils import   print_error
from utils.math_utils import    pow
from type.token import          Token
from type.x import              X
from type.parentheses import    Parentheses
from type.operator import       Power, Multiplication, Division, Addition,\
                                Substraction

def simple_simplification(left_tokens: list, right_tokens: list):
    _simple_simplification(left_tokens)
    _simple_simplification(right_tokens)


def _simple_simplification(tokens: list):
    for i in range(len(tokens)):
        tokens[i] = _simple_simplify(tokens[i])


def _simple_simplify(token):
    type_token = type(token)

    if type_token == Token or type_token == X:
        return token

    # Power ####################################################################
    elif type_token == Power:
        token.number = _simple_simplify(token.number)
        token.power = _simple_simplify(token.power)
        number = token.number
        power = token.power
        type_number = type(token.number)
        type_power = type(token.power)

        if type_number == Token and type_power == Token:
            if int(power.value) != power.value:
                print_error("power by decimal")
            result = pow(number.value, power.value)
            return Token.create_number(result)

        elif type_number == X and type_power == Token:
            if power.value == 0.0:
                return Token.create_number(1)
            number.power *= power.value
            return number

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
                print_error("division by 0")
            result = left.value / right.value
            return Token.create_number(result)

        elif type_left == X and type_right == Token:
            left.multiplication /= right.value
            return left

        elif type_left == X and type_right == X:
            if left == right:
                return Token.create_number(1)
            left.power -= right.power
            left.multiplication *= right.multiplication
            return left

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
            return left

    # Parentheses ##############################################################
    elif type_token == Parentheses:
        for i in range(len(token.tokens)):
            token.tokens[i] = _simple_simplify(token.tokens[i])

        if len(token.tokens) == 1\
            and (type(token.tokens[0]) == Token or type(token.tokens[0]) == X):
            return token.tokens[0]

        return token

    return token
