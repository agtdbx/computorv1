# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#   is_there_an_equal.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/05/02 16:27:42 by auguste           #+#    #+#              #
#    Updated: 2024/05/02 16:27:42 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def is_there_an_equal(tokens: list) -> bool:
    for token in tokens:
        if token.is_equal():
            return True
    return False
