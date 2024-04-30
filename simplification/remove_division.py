# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    remove_division.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/30 19:49:38 by auguste           #+#    #+#              #
#    Updated: 2024/04/30 20:05:25 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from type.operator import           Division, Multiplication
from simplification.simple import   _simple_simplification

def remove_division(left_tokens: list):
    i = 0
    while i < len(left_tokens):
        token = left_tokens[i]
        if type(token) == Division:
            for j in range(len(left_tokens)):
                left_tokens[j] = Multiplication(left_tokens[j],
                                                token.right.copy())
            _simple_simplification(left_tokens)
            _simple_simplification(left_tokens)
        i += 1

