# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/25 19:13:36 by auguste           #+#    #+#              #
#    Updated: 2024/04/25 19:13:36 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

from utils.print_utils import               print_error
from utils.print_equation import            print_equation, print_test_equation,\
                                            print_test_token
from parsing.parsing import                 get_tokens_from_input
from parsing.split_equal import             split_by_equal
from parsing.operator import                operator_check
from simplification.negative import         inverse_negative_simplification
from simplification.split_by_add import     split_by_add_simplification
from simplification.parentheses import      parentheses_simplification,\
                                            remove_parentheses
from simplification.simple import           simple_simplification
from simplification.join_left_right import  join_left_right
from simplification.remove_division import  remove_division
from simplification.right_order import      right_order
from resolution.get_degree import           get_degree
from resolution.is_there_an_equal import    is_there_an_equal
from resolution.is_there_an_x import        is_there_an_x
from resolution.result import               check_result
from resolution.degree_1 import             resolve_degree_1
from resolution.degree_2 import             resolve_degree_2


if __file__ != "__main__":
    if len(sys.argv) != 2:
        print("Error: Bad number of argument", file=sys.stderr)
        print("Usage : python3 main.y <mathematical equation>")
        exit(1)

    # Parse input
    print(f"Input : {sys.argv[1]}")
    tokens = get_tokens_from_input(sys.argv[1])

    # Split the equation into two part arround the equal
    left_tokens, right_tokens = split_by_equal(tokens)

    # Transform token into operator with priority
    operator_check(left_tokens, right_tokens)
    #print_test_equation(left_tokens, "AFTER REMOVE +")
    #print_test_token(left_tokens, "AFTER REMOVE +")

    # Save tokens list
    save_operator_left = []
    for tok in left_tokens:
        save_operator_left.append(tok.copy())
    save_operator_right = []
    for tok in right_tokens:
        save_operator_right.append(tok.copy())

    # Replace minus by add invert. a - b = a + (b * -1)
    inverse_negative_simplification(left_tokens, right_tokens)

    # Instead of keep add as operator, just have multiple element in list
    left_tokens = split_by_add_simplification(left_tokens)
    right_tokens = split_by_add_simplification(right_tokens)

    # Make the parenthese calculation :
    # - scale : (a + b) * c = (a * c + b * c)
    # - multiplication : (a + b) * (c + d) = (a*c + a*d + b*c + b*d)
    # - power : (a + b)^2 = (a*a + a*b + b*a + b*b)
    parentheses_simplification(left_tokens, right_tokens)

    # Simplify all calulation. Calculate all numbers. (1 + 3) * x -> 4 * x
    simple_simplification(left_tokens, right_tokens)

    # Move the right part of the equation (equal is the middle) to the lef.
    # a = b -> a - b = 0
    join_left_right(left_tokens, right_tokens)

    # Another simplification
    simple_simplification(left_tokens, right_tokens)

    # Remove the division by X : 4 / x + 3 = 0 -> 4 + 3x = 0
    remove_division(left_tokens)

    # Remove parentheses : (1 + X * 2) + -3 = 0 -> 1 + X * 2 + -3 = 0
    remove_parentheses(left_tokens)

    # Another simplification
    simple_simplification(left_tokens, right_tokens)

    # Make the higher power from left to right
    right_order(left_tokens)

    # Get degree of the equation and make error for ^X
    degree = get_degree(left_tokens)

    # If this is degree 0, do not print the equation. It will be like 1 = 0
    if degree == 0:
        check = check_result(save_operator_left,
                            save_operator_right,
                            left_tokens[0].value)

        if is_there_an_x(save_operator_left, save_operator_right):
            if not check:
                print_error("the equation have no result")
            print("X can have any Real value, like 42 !")
        else:
            if not check:
                print_error("the equation is false")
            if is_there_an_equal(tokens):
                print("The equation is true")
            print(f"Equation degree : 0\nResult : {left_tokens[0]}")
        exit()

    # Print the simplified equation
    print("Simplify : ", end='')
    print_equation(left_tokens, right_tokens)

    # Resolve the equation
    if degree == 1:
        resolve_degree_1(save_operator_left,
                         save_operator_right,
                         left_tokens,
                         right_tokens)
    elif degree == 2:
        resolve_degree_2(save_operator_left,
                         save_operator_right,
                         left_tokens,
                         right_tokens)
    else:
        print_error(f"cannot resolve equation with {degree} degree")
