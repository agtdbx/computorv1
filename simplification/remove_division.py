# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    remove_division.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/30 19:49:38 by auguste           #+#    #+#              #
#    Updated: 2024/04/30 21:05:33 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from type.token import                  Token
from type.x import                      X
from type.parentheses import            Parentheses
from type.operator import               Division, Multiplication
from simplification.parentheses import  _parentheses_simplification
from simplification.simple import       _simple_simplification

def remove_division(left_tokens: list):
    i = 0
    while i < len(left_tokens):
        token = left_tokens[i]
        if type(token) == Division:
            for j in range(len(left_tokens)):
                left_tokens[j] = Multiplication(left_tokens[j],
                                                token.right.copy())

            _simple_simplification(left_tokens)
            _parentheses_simplification(left_tokens)
            _simple_simplification(left_tokens)

            j = 0
            while j < len(left_tokens):
                if type(left_tokens[j]) == Parentheses:
                    left_tokens.extend(left_tokens[j].tokens)
                    left_tokens.pop(j)
                else:
                    j += 1

            # TODO: ADD ALL TOGETHER, NO MATTER THE PLACE
        i += 1

    i = 0
    while i < len(left_tokens):
        token = left_tokens[i]
        type_token = type(token)
        j = i + 1
        while j < len(left_tokens):
            tok = left_tokens[j]
            type_tok = type(tok)
            if type_token == Token and type_tok == Token:
                token.value += tok.value
                left_tokens.pop(j)
            elif type_token == X and type_tok == X\
                    and token.power == tok.power:
                token.multiplication += tok.multiplication
                left_tokens.pop(j)
            else:
                j += 1
        i += 1
