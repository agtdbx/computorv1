# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    degree_1.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/30 23:54:37 by auguste           #+#    #+#              #
#    Updated: 2024/05/14 18:49:16 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_utils import       print_error
from utils.print_equation import    print_equation
from type.token import              Token
from type.x import                  X
from type.operator import           Division
from simplification.simple import   _simple_simplification
from resolution.result import       check_result

def resolve_degree_1(save_operator_left: list,
                     save_operator_right: list,
                     left_tokens: list,
                     right_tokens: list):
    print("Equation degree : 1")

    x : X = left_tokens[0]
    if len(left_tokens) == 2:
        number = left_tokens[1].value * -1
        right_tokens[0] = Token.create_number(number)
        left_tokens.pop()
        print_equation(left_tokens, right_tokens)

    if x.multiplication != 1:
        right_tokens[0] = Division(right_tokens[0],
                                   Token.create_number(x.multiplication))
        x.multiplication = 1
        print_equation(left_tokens, right_tokens)

    _simple_simplification(right_tokens)
    print_equation(left_tokens, right_tokens)

    result = right_tokens[0].value
    if not check_result(save_operator_left, save_operator_right, result):
        print_error("the equation have no solution")

    print(f"Result : {result}")

