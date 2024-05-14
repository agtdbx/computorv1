# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    print_utils.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/25 23:03:32 by auguste           #+#    #+#              #
#    Updated: 2024/05/14 18:49:34 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def print_error(error_str: str, exit_status: int = 1):
    print(f"Error : {error_str}", file=sys.stderr)
    exit(exit_status)
