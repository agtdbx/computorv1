# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    get_degree.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/30 23:24:30 by auguste           #+#    #+#              #
#    Updated: 2024/05/01 00:53:18 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_utils import   print_error
from type.x import              X
from type.operator import       Power, Multiplication

def get_degree(left_tokens: list):
    degree = 0

    for token in left_tokens:
        type_token = type(token)
        if type_token == X:
            if token.power > degree:
                degree = token.power
        elif type_token == Power or type_token == Multiplication:
            print_error("cannot have a power by x")

    return degree
