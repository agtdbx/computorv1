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

def operator_check(left_tokens: list, right_tokens: list):

    #print("\n#################[CHECK VARIABLE]#################")
    X.parse_x(left_tokens)
    X.parse_x(right_tokens)

    #print("\n====LEFT TOKENS====")
    #for token in left_tokens:
    #    print(token.to_string())

    #print("\n====RIGHT TOKENS====")
    #for token in right_tokens:
    #    print(token.to_string())

    #print("\n#################[CHECK PARENTHESES]#################")
    Parentheses.parse_parentheses(left_tokens)
    Parentheses.parse_parentheses(right_tokens)

    #print("\n====LEFT TOKENS====")
    #for token in left_tokens:
    #    print(token.to_string())

    #print("\n====RIGHT TOKENS====")
    #for token in right_tokens:
    #    print(token.to_string())

    #print("\n#################[CHECK POWER]#################")
    Power.parse_power(left_tokens)
    Power.parse_power(right_tokens)

    #print("\n====LEFT TOKENS====")
    #for token in left_tokens:
    #    print(token.to_string())

    #print("\n====RIGHT TOKENS====")
    #for token in right_tokens:
    #    print(token.to_string())

    #print("\n#################[CHECK MUTL-DIV]#################")
    parse_mult_div(left_tokens)
    parse_mult_div(right_tokens)

    print("\n====LEFT TOKENS====")
    for token in left_tokens:
        print(token.to_string())

    print("\n====RIGHT TOKENS====")
    for token in right_tokens:
        print(token.to_string())
