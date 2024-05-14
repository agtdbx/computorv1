# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parentheses.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/27 11:35:01 by auguste           #+#    #+#              #
#    Updated: 2024/04/27 11:35:01 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from type.token import          Token

class Parentheses:

    def __init__(self, sub_tokens: list) -> None:
        self.tokens = sub_tokens

    def __str__(self) -> str:
        string = "("

        for i in range(len(self.tokens)):
            if i != 0:
                string += " + "
            string += str(self.tokens[i])

        string += ')'

        return string

    def __eq__(self, value) -> bool:
        if type(value) != Parentheses:
            return False

        length = len(self.tokens)
        if len(value.tokens) != length:
            return False

        copy_tokens = []
        for val in value.tokens:
            copy_tokens.append(val.copy())

        for val in self.tokens:
            i = 0
            while i < length:
                if val == copy_tokens[i]:
                    copy_tokens.pop(i)
                    break
                i += 1

            if i == length:
                return False

        return True

    def contains_variable(self) -> bool:
        for token in self.tokens:
            if type(token) == Token and token.is_variable():
                return True
            if type(token) == Parentheses and token.contains_variable():
                return True
        return False

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        string = ' ' * depth + "parentheses :\n"
        depth += 2

        for i in range(len(self.tokens)):
            if i != 0:
                string += '\n'
            string += self.tokens[i].to_string(depth)

        return string

    # Public methods ###########################################################

    def copy(self):
        subtokens = []
        for token in self.tokens:
            subtokens.append(token.copy())
        return Parentheses(subtokens)
