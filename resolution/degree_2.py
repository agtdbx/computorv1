# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    degree_2.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/01 01:36:05 by auguste           #+#    #+#              #
#    Updated: 2024/05/01 02:12:29 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_utils import   print_error
from utils.math_utils import    sqrt
from type.x import              X
from resolution.result import   check_result

def resolve_degree_2(save_operator_left: list,
                     save_operator_right: list,
                     left_tokens: list,
                     right_tokens: list):
    print("Equation degree : 2")

    x2 = left_tokens[0]
    x = None
    number = None
    if len(left_tokens) == 2:
        if type(left_tokens[1]) == X:
            x = left_tokens[1]
        else:
            number = left_tokens[1]

    elif len(left_tokens) == 3:
        x = left_tokens[1]
        number = left_tokens[2]

    a = x2.multiplication
    b = 0
    if x != None:
        b = x.multiplication
    c = 0
    if number != None:
        c = number.value

    discriminant = (b * b) - 4 * a * c
    print(f"a {a}")
    print(f"b {b}")
    print(f"c {c}")
    print(f"discriminant {discriminant}")

    if discriminant < 0:
        # TODO: make complexe number
        print_error("no solution for the equation")

    elif discriminant == 0:
        result = (-b) / (a * 2)
        if not check_result(save_operator_left, save_operator_right, result):
            print_error("no solution for the equation")
        print(f"Result : {result}")

    else:
        sqrt_discriminant = sqrt(discriminant)
        result_1 = (-b - sqrt_discriminant) / (a * 2)
        result_2 = (-b + sqrt_discriminant) / (a * 2)
        if not check_result(save_operator_left,
                            save_operator_right,
                            result_1):
            if not check_result(save_operator_left,
                              save_operator_right,
                              result_2):
                print_error("no solution for the equation")
            print(f"Result : {result_1}")

        elif not check_result(save_operator_left,
                              save_operator_right,
                              result_2):
            print(f"Result : {result_2}")

        else:
            print(f"Result 1 : {result_1}")
            print(f"Result 2 : {result_2}")


