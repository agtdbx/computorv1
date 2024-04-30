# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_equation.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/30 23:35:07 by auguste           #+#    #+#              #
#    Updated: 2024/04/30 23:37:12 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from type.token import  Token
from type.x import      X

def print_test_token(tokens: list, side):
    print(f"\n===={side} TOKENS====")
    for token in tokens:
        print(token.to_string())


def print_test_equation(tokens: list, side):
    print(f"\n===={side} PART====")
    for i in range(len(tokens)):
        if i != 0:
            print(" + ", end='')
        print(tokens[i], end='')
    print()


def print_equation(left_tokens, right_tokens):
    print("Simplify : ", end='')

    _print_equation_part(left_tokens)
    print(" = ", end='')
    _print_equation_part(right_tokens)

    print()


def _print_equation_part(tokens):
    for i in range(len(tokens)):
        token = tokens[i]
        if i > 0:
            if type(token) == Token and token.value < 0:
                print(f" - {-token.value}", end='')
                continue
            elif type(token) == X and token.multiplication < 0:
                token.multiplication * -1
                print(f" - {token}", end='')
                token.multiplication * -1
                continue
            print(" + ", end='')
        print(token, end='')
