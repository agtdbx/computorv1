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

from parsing.operator_utils.x import            parse_x
from parsing.operator_utils.parentheses import  parse_parentheses
from parsing.operator_utils.power import        parse_power
from parsing.operator_utils.mult_div import     parse_mult_div
from parsing.operator_utils.add_sub import      parse_add_sub


def operator_check(left_tokens: list, right_tokens: list):
    parse_x(left_tokens)
    parse_x(right_tokens)

    parse_parentheses(left_tokens)
    parse_parentheses(right_tokens)

    while parse_power(left_tokens): pass
    while parse_power(right_tokens): pass

    while parse_mult_div(left_tokens): pass
    while parse_mult_div(right_tokens): pass

    while parse_add_sub(left_tokens): pass
    while parse_add_sub(right_tokens): pass
