# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operator.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/26 20:16:12 by auguste           #+#    #+#              #
#    Updated: 2024/04/26 20:16:12 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from type.x import              X
from type.parentheses import    Parentheses
from type.power import          Power
from type.mult_div import       parse_mult_div
from type.add_sub import        parse_add_sub

def operator_check(left_tokens: list, right_tokens: list):
    X.parse_x(left_tokens)
    X.parse_x(right_tokens)

    Parentheses.parse_parentheses(left_tokens)
    Parentheses.parse_parentheses(right_tokens)

    #print("\n###################### AFTER PARENTHESES")
    #print("\n====LEFT TOKENS====")
    #for token in left_tokens:
    #    print(token.to_string())

    #print("\n====RIGHT TOKENS====")
    #for token in right_tokens:
    #    print(token.to_string())

    #Power.parse_power(left_tokens)
    #Power.parse_power(right_tokens)

    #print("\n###################### AFTER POWER")
    #print("\n====LEFT TOKENS====")
    #for token in left_tokens:
    #    print(token.to_string())

    #print("\n====RIGHT TOKENS====")
    #for token in right_tokens:
    #    print(token.to_string())

    parse_mult_div(left_tokens)
    parse_mult_div(right_tokens)

    #print("\n###################### AFTER MULT DIV")
    #print("\n====LEFT TOKENS====")
    #for token in left_tokens:
    #    print(token.to_string())

    #print("\n====RIGHT TOKENS====")
    #for token in right_tokens:
    #    print(token.to_string())

    parse_add_sub(left_tokens)
    parse_add_sub(right_tokens)

    print("\n###################### AFTER ADD SUB")
    print("\n====LEFT TOKENS====")
    for token in left_tokens:
        print(token.to_string())

    print("\n====RIGHT TOKENS====")
    for token in right_tokens:
        print(token.to_string())

