# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    x.py                                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: auguste <auguste@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/04/26 20:16:04 by auguste           #+#    #+#              #
#    Updated: 2024/04/26 21:52:36 by auguste          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from utils.print_utils import   print_error
from type.token import          Token

class X:
    def __init__(self) -> None:
        self.multiplication = 1
        self.power = 1

    def __str__(self) -> str:
        string = "x"
        if self.multiplication == -1:
            string = "-x"
        elif self.multiplication != 1:
            string = f"{self.multiplication}x"

        if self.power != 1:
            string += f"^{self.power}"

        return string

    # String methods ###########################################################

    def to_string(self, depth=0) -> str:
        string = ' ' * depth + f"x[{self.multiplication},{self.power}]\n"

        return string

	# Static methods ###########################################################

    def parse_x(tokens: list[Token]):
        i = 0

        while i < len(tokens):
            if type(tokens[i]) != Token or not tokens[i].is_variable():
                i += 1
                continue

            if tokens[i].value != 'X':
                print_error(f"'{tokens[i].value}' is a valid variable")

            tokens[i] = X()

            i += 1
