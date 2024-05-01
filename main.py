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
from utils.print_equation import            print_equation
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

    # Simplify the equation
    operator_check(left_tokens, right_tokens)
    save_operator_left = []
    for tok in left_tokens:
        save_operator_left.append(tok.copy())
    save_operator_right = []
    for tok in right_tokens:
        save_operator_right.append(tok.copy())
    inverse_negative_simplification(left_tokens, right_tokens)
    left_tokens = split_by_add_simplification(left_tokens)
    right_tokens = split_by_add_simplification(right_tokens)
    parentheses_simplification(left_tokens, right_tokens)
    simple_simplification(left_tokens, right_tokens)
    join_left_right(left_tokens, right_tokens)
    simple_simplification(left_tokens, right_tokens)
    remove_division(left_tokens)
    remove_parentheses(left_tokens)
    simple_simplification(left_tokens, right_tokens)
    right_order(left_tokens)

    # Get degree of the equation
    degree = get_degree(left_tokens)

    if degree == 0:
        print("Equation degree : 0")
        if not check_result(save_operator_left,
                            save_operator_right,
                            left_tokens[0]):
            print_error("the equation have no result")
        print(f"Result : {left_tokens[0]}")
        exit()

    # Print the simplified equation
    print("Simplify : ", end='')
    print_equation(left_tokens, right_tokens)

    # Resolve the equation
    if degree == -1:
        print_error("the equation have no solution")
    elif degree == 1:
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
