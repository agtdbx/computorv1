# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    x.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/27 11:34:48 by auguste           #+#    #+#              #
#    Updated: 2024/04/27 11:37:07 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_utils import   print_error
from type.token import  Token
from type.x import      X

def parse_x(tokens: list):
    i = 0

    while i < len(tokens):
        if type(tokens[i]) != Token or not tokens[i].is_variable():
            i += 1
            continue

        if tokens[i].value != 'X':
            print_error(f"'{tokens[i].value}' is a valid variable")

        tokens[i] = X()

        i += 1
