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

from parsing.parsing import             get_tokens_from_input
from parsing.split_equal import         split_by_equal
from parsing.operator import            operator_check
from simplification.negative import     inverse_negative_simplification
from simplification.split_by_add import split_by_add_simplification
from simplification.parentheses import  parentheses_simplification
from simplification.simple import       simple_simplification


def print_token(tokens: list, side):
    print(f"\n===={side} TOKENS====")
    for token in tokens:
        print(token.to_string())


def print_equation(tokens: list, side):
    print(f"\n===={side} PART====")
    for i in range(len(tokens)):
        if i != 0:
            print(" + ", end='')
        print(tokens[i], end='')
    print()



if __file__ != "__main__":
    if len(sys.argv) != 2:
        print("Error: Bad number of argument", file=sys.stderr)
        print("Usage : python3 main.y <mathematical equation>")
        exit(1)

    print(f"Input : {sys.argv[1]}")

    tokens = get_tokens_from_input(sys.argv[1])

    left_tokens, right_tokens = split_by_equal(tokens)

    operator_check(left_tokens, right_tokens)

    print("\n#################[BEFORE SIMPLIFICATION]#################")
    print_token(left_tokens, "LEFT")
    print_token(right_tokens, "RIGHT")
    print_equation(left_tokens, "LEFT")
    #print_equation(left_tokens, "RIGHT")

    inverse_negative_simplification(left_tokens, right_tokens)
    left_tokens = split_by_add_simplification(left_tokens)
    right_tokens = split_by_add_simplification(right_tokens)
    parentheses_simplification(left_tokens, right_tokens)
    #simple_simplification(left_tokens, right_tokens)

    print("\n#################[AFTER SIMPLIFICATION]#################")
    print_token(left_tokens, "LEFT")
    print_token(right_tokens, "RIGHT")
    print_equation(left_tokens, "LEFT")
    #print_equation(left_tokens, "RIGHT")

