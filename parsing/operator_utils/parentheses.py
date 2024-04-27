# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parentheses.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/27 11:28:33 by auguste           #+#    #+#              #
#    Updated: 2024/04/27 11:38:12 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_utils import   print_error
from type.token import          Token
from type.parentheses import    Parentheses

def parse_parentheses(tokens: list):
    i = 0

    while i < len(tokens):
        if not type(tokens[i]) == Token or not tokens[i].is_parenthese():
            i += 1
            continue

        if tokens[i].value != '(':
            print_error("invalid close parenthese")

        depth_count = 1
        start = i + 1

        i += 1

        while i < len(tokens) and depth_count > 0:
            if tokens[i].is_parenthese():
                if tokens[i].value == '(':
                    depth_count += 1
                else:
                    depth_count -= 1
            i += 1

        if depth_count != 0:
            print_error("unclose parenthese")

        end = i

        if start + 1 == end:
            print_error("empty parentheses")

        sub_tokens = tokens[start:end - 1]
        parse_parentheses(sub_tokens)
        parentheses = Parentheses(sub_tokens)

        for _ in range(start, end):
            tokens.pop(start)

        tokens[start - 1] = parentheses

        i = start


