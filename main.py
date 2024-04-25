# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/25 19:13:36 by auguste           #+#    #+#              #
#    Updated: 2024/04/25 19:13:36 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

from parsing.parsing import get_tokens_from_input

if __file__ != "__main__":
    if len(sys.argv) != 2:
        print("Error: Bad number of argument", file=sys.stderr)
        print("Usage : python3 main.y <mathematical equation>")
        exit(1)

    tokens = get_tokens_from_input(sys.argv[1])

    print("TOKENS")
    for token in tokens:
        print(token)
