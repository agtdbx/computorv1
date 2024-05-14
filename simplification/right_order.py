# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    right_order.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/30 22:44:45 by auguste           #+#    #+#              #
#    Updated: 2024/05/14 18:49:25 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from type.x import  X

def right_order(left_tokens: list):
    left_tokens.sort(key=_sort_function, reverse=True)


def _sort_function(token):
    if type(token) == X:
        return token.power
    return 0
