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

from parsing.parsing import                 get_tokens_from_input
from parsing.split_equal import             split_by_equal
from parsing.operator import                operator_check
from simplification.simple.simple import    simple_simplification

if __file__ != "__main__":
    if len(sys.argv) != 2:
        print("Error: Bad number of argument", file=sys.stderr)
        print("Usage : python3 main.y <mathematical equation>")
        exit(1)

    print(f"Input : {sys.argv[1]}")

    tokens = get_tokens_from_input(sys.argv[1])

    #print("\n#################[PARSE INPUT]#################")
    #print("\n====TOKENS====")
    #for token in tokens:
    #    print(token.to_string())

    left_tokens, right_tokens = split_by_equal(tokens)

    operator_check(left_tokens, right_tokens)

    print("\n#################[BEFORE SIMPLIFICATION]#################")
    print("\n====LEFT TOKENS====")
    for token in left_tokens:
        print(token.to_string())

    print("\n====RIGHT TOKENS====")
    for token in right_tokens:
        print(token.to_string())

    #print("\n====LEFT TOKENS====")
    #for token in left_tokens:
    #    print(token, end=' ')
    #print()

    #print("\n====RIGHT TOKENS====")
    #for token in right_tokens:
    #    print(token, end=' ')
    #print()

    simple_simplification(left_tokens, right_tokens)

    print("\n#################[AFTER SIMPLIFICATION]#################")
    print("\n====LEFT TOKENS====")
    for token in left_tokens:
        print(token.to_string())

    print("\n====RIGHT TOKENS====")
    for token in right_tokens:
        print(token.to_string())

    print("\n====LEFT TOKENS====")
    for token in left_tokens:
        print(token, end=' ')
    print()

    print("\n====RIGHT TOKENS====")
    for token in right_tokens:
        print(token, end=' ')
    print()
